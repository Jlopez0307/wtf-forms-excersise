from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app

    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f"<Pet id = {p.id} | name = {p.name} | species = {p.species} | photo_url = {p.photo_url} | age = {p.age} | notes = {p.notes} | available = {p.available}"

    id = db.Column( db.Integer, primary_key=True, autoincrement=True )
    name = db.Column( db.String(20), nullable = False)
    species = db.Column( db.String(50), nullable = False)
    photo_url = db.Column( db.String(200) )
    age = db.Column( db.Integer )
    notes = db.Column( db.String(100) )
    available = db.Column( db.Boolean, nullable = False, server_default = 'True')

