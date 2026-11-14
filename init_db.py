from database import engine
from models import Base, Order, User

Base.metadata.create_all(engine)

print("Database initialized successfully.")