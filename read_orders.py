from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Order

engine = create_engine('sqlite:///essensbestellung.db', echo=True)

with Session(engine) as session:
    statement = select(Order)

    orders = session.scalars(statement).all()

    for order in orders:
        print(
            f"ID: {order.id}, "
            f"Date: {order.date}, "
            f"Menu: {order.menu}, "
        )

