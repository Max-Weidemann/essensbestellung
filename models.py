from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name:  Mapped[str]

class Order(Base):
    __tablename__ = "orders"

    __table_args__ = (
        UniqueConstraint("user_id", "date", name="uq_order_user_date"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    date: Mapped[str]
    menu: Mapped[str]