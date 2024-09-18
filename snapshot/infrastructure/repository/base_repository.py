from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from snapshot.config import DB_CONFIG

engine = create_engine(
    f"{DB_CONFIG['DB_DRIVER']}://{DB_CONFIG['DB_USER']}:"
    f"{DB_CONFIG['DB_PASSWORD']}"
    f"@{DB_CONFIG['DB_HOST']}:"
    f"{DB_CONFIG['DB_PORT']}/{DB_CONFIG['DB_NAME']}", echo=False)


Session = sessionmaker(bind=engine)
default_session = Session()


class BaseRepository:

    def __init__(self):
        self.session = default_session

    def add_item(self, item, auto_commit=True):
        return self.add_all_items([item], auto_commit)

    def add_all_items(self, items, auto_commit=True):
        try:
            self.session.add_all(items)
            if auto_commit:
                self.session.commit()
        except Exception as e:
            if auto_commit:
                self.session.rollback()
            raise e
