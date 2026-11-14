from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database import SessionLocal
from models import User, Order

with SessionLocal() as session:
    alice = session.scalar(
        select(User).where(User.name == "Alice")
    )

    if alice is None:
        raise RuntimeError("Alice does not exist.")

    duplicate_order = Order(
        user_id=alice.id,
        date="2026-11-16",
        menu="menu_2",
    )

    session.add(duplicate_order)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        print("UNIQUE constraint works!")
        print(error.orig)