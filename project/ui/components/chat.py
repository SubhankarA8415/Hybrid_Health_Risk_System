# ============================================
# 💬 PREMIUM AI WELLNESS CHAT COMPONENT
# ============================================

import streamlit as st


# ============================================
# 🌐 API CLIENT
# ============================================

from project.ui.services.api_client import (

    send_chat_message,

    get_chat_history,

    clear_chat_history
)


# ============================================
# 🤖 CHAT INTRO
# ============================================

def render_chat_intro():

    st.markdown("""

<div class="glass-card">

<h2>
🤖 AI Wellness Assistant
</h2>

<p style="
line-height:1.9;
opacity:0.92;
font-size:1rem;
">

Your AI-powered wellness companion can help with:

• 🥗 Nutrition guidance  
• 🏋 Fitness suggestions  
• 😴 Sleep improvement  
• 🧘 Stress management  
• ❤️ Heart wellness  
• ⚖ Weight management  
• 🌿 Healthy lifestyle habits  
• 📚 Preventive wellness education  

</p>

</div>

""", unsafe_allow_html=True)


# ============================================
# 🌿 SUGGESTED PROMPTS
# ============================================

def render_suggestions():

    st.markdown("""

<div class="glass-card">

<h4>
✨ Suggested Wellness Questions
</h4>

<div style="
margin-top:1rem;
">

<span class="suggestion-pill">
🥗 Suggest healthy breakfast ideas
</span>

<span class="suggestion-pill">
😴 How can I improve sleep?
</span>

<span class="suggestion-pill">
🏋 Home workout routine
</span>

<span class="suggestion-pill">
🧘 Stress reduction techniques
</span>

<span class="suggestion-pill">
❤️ Tips for heart wellness
</span>

<span class="suggestion-pill">
⚖ Weight management advice
</span>

</div>

</div>

""", unsafe_allow_html=True)


# ============================================
# 🚀 MAIN CHAT COMPONENT
# ============================================

def render_chat():

    st.markdown("---")

    st.header(
        "💬 AI Wellness Assistant"
    )

    st.caption("""
Conversational AI-powered wellness support and preventive lifestyle guidance.
""")


    # ========================================
    # 🤖 INTRO
    # ========================================

    render_chat_intro()


    # ========================================
    # 🚨 LOGIN CHECK
    # ========================================

    if not st.session_state.user:

        st.info(
            "🔐 Login to enable persistent AI conversations and saved chat history."
        )

        return


    # ========================================
    # 👤 USER EMAIL
    # ========================================

    user_email = (
        st.session_state.user["email"]
    )


    # ========================================
    # 💾 INITIALIZE CHAT
    # ========================================

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []


    # ========================================
    # 🔄 LOAD CHAT HISTORY
    # ========================================

    if len(st.session_state.chat_history) == 0:

        try:

            response = get_chat_history(
                user_email
            )


            if (

                response

                and response.status_code == 200
            ):

                chats = response.json()

                cleaned_history = []


                for item in chats:

                    role = item.get(
                        "role",
                        "assistant"
                    )

                    message = item.get(
                        "message",
                        ""
                    )

                    if not message:

                        continue


                    cleaned_history.append({

                        "role": role,

                        "message": message
                    })


                st.session_state.chat_history = (
                    cleaned_history
                )

        except Exception:

            pass


    # ========================================
    # 🌿 CHAT ACTIONS
    # ========================================

    action_col1, action_col2, action_col3 = st.columns(
        [1, 1, 4]
    )


    # ========================================
    # 🗑 CLEAR CHAT
    # ========================================

    with action_col1:

        if st.button(

            "🗑 Clear Chat",

            use_container_width=True
        ):

            try:

                response = clear_chat_history(
                    user_email
                )


                if (

                    response

                    and response.status_code == 200
                ):

                    st.session_state.chat_history = []

                    st.success(
                        "Chat history cleared successfully."
                    )

                    st.rerun()

                else:

                    st.error(
                        "Unable to clear chat history."
                    )

            except Exception as e:

                st.error(
                    f"Clear Chat Error: {str(e)}"
                )


    # ========================================
    # 🔄 REFRESH CHAT
    # ========================================

    with action_col2:

        if st.button(

            "🔄 Refresh",

            use_container_width=True
        ):

            st.session_state.chat_history = []

            st.rerun()


    st.markdown("<br>", unsafe_allow_html=True)


    # ========================================
    # 🌿 EMPTY CHAT STATE
    # ========================================

    if len(st.session_state.chat_history) == 0:

        render_suggestions()


    # ========================================
    # 💬 CHAT CONTAINER
    # ========================================

    st.markdown(
        '<div class="chat-wrapper">',
        unsafe_allow_html=True
    )


    # ========================================
    # 💬 DISPLAY CHAT HISTORY
    # ========================================

    for message in st.session_state.chat_history:

        role = message.get(
            "role",
            "assistant"
        )

        content = message.get(
            "message",
            ""
        )

        if not content:

            continue


        with st.chat_message(role):

            st.markdown(content)


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================
    # 💬 CHAT INPUT
    # ========================================

    user_chat = st.chat_input(
        "Ask your wellness question..."
    )


    # ========================================
    # 🚀 CHAT PIPELINE
    # ========================================

    if user_chat:

        # ====================================
        # 👤 USER MESSAGE
        # ====================================

        user_message = {

            "role": "user",

            "message": user_chat
        }

        st.session_state.chat_history.append(
            user_message
        )


        with st.chat_message("user"):

            st.markdown(user_chat)


        # ====================================
        # 🤖 ASSISTANT RESPONSE
        # ====================================

        with st.chat_message("assistant"):

            st.markdown("""

<div class="ai-thinking">

🧠 Generating personalized wellness guidance...

</div>

""", unsafe_allow_html=True)


            try:

                response = send_chat_message({

                    "message": user_chat,

                    "history": st.session_state.chat_history[:-1],

                    "user_email": user_email
                })


                # ============================
                # ❌ CONNECTION FAILURE
                # ============================

                if response is None:

                    fallback_reply = """

⚠ Unable to connect to the AI backend currently.

Please try again in a few moments.
"""

                    st.warning(
                        fallback_reply
                    )

                    st.session_state.chat_history.append({

                        "role": "assistant",

                        "message": fallback_reply
                    })


                # ============================
                # ✅ SUCCESS
                # ============================

                elif response.status_code == 200:

                    response_json = (
                        response.json()
                    )


                    ai_reply = response_json.get(

                        "response",

                        """
I'm here to support your wellness journey.
Could you please rephrase or provide more detail about your question?
"""
                    )


                    if not ai_reply:

                        ai_reply = """

I'm here to support your wellness journey.
Could you please rephrase your question?
"""


                    st.markdown(
                        ai_reply
                    )


                    st.session_state.chat_history.append({

                        "role": "assistant",

                        "message": ai_reply
                    })


                # ============================
                # ❌ API FAILURE
                # ============================

                else:

                    fallback_reply = """

⚠ The AI assistant encountered difficulty processing your request.

Please try rephrasing your question or ask another wellness-related query.
"""

                    st.warning(
                        fallback_reply
                    )

                    st.session_state.chat_history.append({

                        "role": "assistant",

                        "message": fallback_reply
                    })


            # =================================
            # ❌ GLOBAL EXCEPTION
            # =================================

            except Exception:

                fallback_reply = """

⚠ The AI wellness assistant is temporarily unavailable.

Please try again shortly.
"""

                st.warning(
                    fallback_reply
                )

                st.session_state.chat_history.append({

                    "role": "assistant",

                    "message": fallback_reply
                })


    # ========================================
    # 🌿 FOOTNOTE
    # ========================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("""
💙 Your AI wellness assistant provides educational wellness guidance and preventive lifestyle recommendations.

⚠ This system is not a substitute for professional medical advice, diagnosis, or treatment.
""")