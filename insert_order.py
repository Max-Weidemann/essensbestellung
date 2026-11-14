from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Order

engine = create_engine("sqlite:///essensbestellung.db", echo=True)

order = Order(
    date="2026-11-16",
    menu="menu_1"
)

with Session(engine) as session:
    session.add(order)
    session.commit()

print("Order saved successfully")