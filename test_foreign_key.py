from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError

from database import SessionLocal
from models import User, Order

with SessionLocal() as session:
    max_user_id = session.scalar(
        select(func.max(User.id))
    )

    invalid_user_id = (max_user_id or 0) + 1

    invalid_order = Order(
        user_id=invalid_user_id,
        date="2026-11-16",
        menu="menu_1",
    )

    session.add(invalid_order)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        print("FOREIGN KEY constraint works!")
        print(error.orig)