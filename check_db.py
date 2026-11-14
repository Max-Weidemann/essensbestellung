from sqlalchemy import text

from database import engine

with engine.connect() as connection:
    result = connection.execute(text("PRAGMA foreign_keys"))

    print("Foreign keys enabled: ", result.scalar())