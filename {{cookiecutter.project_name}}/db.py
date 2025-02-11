import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

load_dotenv()


class Base(DeclarativeBase):
    pass


db_url = os.getenv("DB_URL")
if db_url is not None:
    engine = create_engine(db_url, echo=True)
else:
    raise Exception("DB_URL variable not set")
