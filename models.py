from app import app
from extension import db


class Producer(db.Model):
    __tablename__ = 'producers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Producer({self.name})"

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    imdb = db.Column(db.Float, nullable=False)
    producer_id = db.Column(db.Integer, db.ForeignKey('producers.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    producer = db.relationship('Producer', backref=db.backref('movies', lazy=True))

    def __init__(self, name, year, imdb, producer_id, status=True):
        self.name = name
        self.year = year
        self.imdb = imdb
        self.producer_id = producer_id
        self.status = status

    def __repr__(self):
        return f"Movie('{self.name}', {self.year}, {self.imdb}, {self.producer_id}, {self.status})"

if __name__ == '__main__':
    db.create_all()




