from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Order

engine = create_engine('sqlite:///essensbestellung.db', echo=True)

with Session(engine) as session:
    statement = select(Order).where(Order.date == "2026-11-16")

    existing_order = session.execute(statement).scalar_one_or_none()