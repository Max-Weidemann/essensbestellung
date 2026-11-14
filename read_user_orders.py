from sqlalchemy import select

from database import SessionLocal
from models import Order, User

with SessionLocal() as session:
    statement = (
        select(User.name, Order.date, Order.menu)
        .join(Order, User.id == Order.user_id)
    )

    results = session.execute(statement).all()

    for name, date, menu in results:
        print(f"{name}: {date} - {menu}")