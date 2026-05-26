from project.database.connection import engine

from project.database.models import Base


print("\n🚀 Creating database tables...\n")

Base.metadata.create_all(
    bind=engine
)

print("✅ Database initialized successfully")