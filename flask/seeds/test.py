from flask_seeder import Seeder

from app.db import db


class DatabaseInitializer(Seeder):

    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 0

    def run(self):
        db.drop_all()
        print(f" - database dropped")

        db.create_all()
        print(f" - database created")
