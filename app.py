from pathlib import Path

from flask import Flask, render_template, request
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Order

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "essensbestellung.db"

engine = create_engine(f"sqlite:///{DATABASE_PATH.as_posix()}", echo=True)

menus = [
    {"day": "Montag", "date": "09.11.2026", "date_iso": "2026-11-09", "menu_1": "Spaghetti Bolognese", "menu_2": "Gemüse-Curry"},
    {"day": "Dienstag", "date": "10.11.2026", "date_iso": "2026-11-10", "menu_1": "Kartoffelauflauf", "menu_2": "Gemüselasagne"},
    {"day": "Mittwoch", "date": "11.11.2026", "date_iso": "2026-11-11", "menu_1": "Chili sin Carne", "menu_2": "Nudelauflauf"},
    {"day": "Donnerstag", "date": "12.11.2026", "date_iso": "2026-11-12", "menu_1": "Kürbissuppe", "menu_2": "Pilzrisotto"},
    {"day": "Freitag", "date": "13.11.2026", "date_iso": "2026-11-13", "menu_1": "Ofenkartoffeln", "menu_2": "Gemüsepfanne"},
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        orders = {}

        for menu in menus:
            date = menu["date_iso"]
            field_name = f"essen_{date}"
            selection = request.form.get(field_name)

            if selection in ("menu_1", "menu_2", "none"):
                orders[date] = selection

        with Session(engine) as session:
            for date, selection in orders.items():
                statement = select(Order).where(Order.date == date)

                existing_order = session.execute(statement).scalar_one_or_none()

                if selection == "none":
                    if existing_order is not None:
                        session.delete(existing_order)
                elif existing_order is None:
                    order = Order(date=date, menu=selection)
                    session.add(order)
                else:
                    existing_order.menu = selection

            session.commit()

        print("Submitted orders:")
        print(orders)

    return render_template("index.html", menus=menus)


if __name__ == "__main__":
    app.run(debug=True)
