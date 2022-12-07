from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_IMAGE="https://cdn.vectorstock.com/i/1000x1000/08/66/cute-maltese-dog-avatar-vector-20670866.webp"

class Pet(db.Model):
    """Pet class."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=True, default=True)

    def __repr__(self):
        return f"<pet {self.id} name={self.name} species={self.species} url={self.photo_url} age={self.age} notes={self.notes} available={self.available}>"