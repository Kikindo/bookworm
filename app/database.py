from pony.orm import Database, Required, Optional
from datetime import datetime

db = Database()

class Book(db.Entity):
    naslov_knjige = Required(str)
    vrijeme_dodavanja = Required(datetime, default=datetime.now)
    zanr = Required(str)
    autor = Required(str)
    ocjena = Required(int)
    biljeske = Optional(str)

def init_db():
    db.bind(provider='sqlite', filename='/data/bookworm.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
