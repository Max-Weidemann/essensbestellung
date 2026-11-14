from sqlalchemy import create_engine

from models import Base, Order

engine = create_engine("sqlite:///essensbestellung.db", echo=True)

Base.metadata.create_all(engine)

print("Database initialized successfully.")