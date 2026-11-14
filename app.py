from flask import Flask, render_template, request
from sqlalchemy import select

from database import SessionLocal
from models import Order, User

app = Flask(__name__)

TEST_USER_ID = 1

menus = [
    {"day": "Montag", "date": "16.11.2026", "date_iso": "2026-11-16", "menu_1": "Spaghetti Bolognese", "menu_2": "Gemüse-Curry"},
    {"day": "Dienstag", "date": "17.11.2026", "date_iso": "2026-11-17", "menu_1": "Kartoffelauflauf", "menu_2": "Gemüselasagne"},
    {"day": "Mittwoch", "date": "18.11.2026", "date_iso": "2026-11-18", "menu_1": "Chili sin Carne", "menu_2": "Nudelauflauf"},
    {"day": "Donnerstag", "date": "19.11.2026", "date_iso": "2026-11-19", "menu_1": "Kürbissuppe", "menu_2": "Pilzrisotto"},
    {"day": "Freitag", "date": "20.11.2026", "date_iso": "2026-11-20", "menu_1": "Ofenkartoffeln", "menu_2": "Gemüsepfanne"},
]


@app.route("/", methods=["GET"])
def index():
    with SessionLocal() as session:
        user = session.get(User, TEST_USER_ID)

        if user is None:
            return  "User not found", 404

        statement = select(Order).where(
            Order.user_id == TEST_USER_ID
        )

        orders = session.scalars(statement).all()

        selected_menus = {}

        for order in orders:
            selected_menus[order.date] = order.menu

    return render_template(
        "index.html",
        menus=menus,
        selected_menus=selected_menus,
    )


if __name__ == "__main__":
    app.run(debug=True)
