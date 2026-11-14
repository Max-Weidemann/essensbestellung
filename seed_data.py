from database import SessionLocal
from models import User, Order

with SessionLocal.begin() as session:
    alice = User(name="Alice")
    bob = User(name="Bob")

    session.add_all([alice, bob])
    session.flush()

    print(f"Alice ID: {alice.id}")
    print(f"Bob ID: {bob.id}")

    order_alice = Order(
        user_id=alice.id,
        date="2026-11-16",
        menu="menu_1",
    )

    order_bob = Order(
        user_id=bob.id,
        date="2026-11-16",
        menu="menu_2",
    )

    session.add_all([order_alice, order_bob])

print("Test data saved successfully.")