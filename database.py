from pathlib import Path

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "essensbestellung.db"

engine = create_engine(f"sqlite:///{DATABASE_PATH.as_posix()}", echo=True)

@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    old_autocommit = getattr(dbapi_connection, "autocommit", None)

    if old_autocommit is False:
        dbapi_connection.autocommit = True

    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys=ON")
    finally:
        cursor.close()

        if old_autocommit is False:
            dbapi_connection.autocommit = old_autocommit

SessionLocal = sessionmaker(bind=engine)