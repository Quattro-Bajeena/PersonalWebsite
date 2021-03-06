from . import db
from sqlalchemy import ForeignKey
from datetime import date

class Nickname(db.Model):
    nickname = db.Column(db.String(32), primary_key=True, nullable=False)
    create_date_str = db.Column(db.String(64))
    create_date = db.Column(db.Date)
    history = db.Column(db.String(2048))

    accounts = db.relationship('Account', backref = 'nick', lazy='dynamic')
    def __repr__(self):
        return f"Nickname: {self.nickname};"

class Account(db.Model):
    website = db.Column(db.String(32), primary_key=True, nullable=False)
    nickname = db.Column(db.String(32), ForeignKey('nickname.nickname'))
    alternative_nickname = db.Column(db.String(32))
    link = db.Column(db.String(120))
    profile_pic = db.Column(db.String(120))
    logo = db.Column(db.String(120))

    activities = db.relationship('Activity', backref = 'account', lazy='dynamic')

    def __repr__(self):
        return f"Site: {self.website}; Nickname: {self.nickname}."


class Art(db.Model):
    name = db.Column(db.String(60), primary_key=True, nullable=False)
    src = db.Column(db.String(128))

    category = db.Column(db.String(32))
    description = db.Column(db.String(1024))
    size = db.Column(db.String(32))

    def __repr__(self):
        return f"Art Piece: {self.name}"

class Video(db.Model):
    title = db.Column(db.String(300), primary_key=True, nullable=False)
    id = db.Column(db.String(300))
    link = db.Column(db.String(200), nullable=False)
    thumbnail = db.Column(db.String(60))
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime)
    history = db.Column(db.String(2000))

    def __repr__(self):
        return f"Video: {self.title}"

class Activity(db.Model):
    id = db.Column(db.String(200), primary_key=True, nullable=False)
    website = db.Column(db.String(100), ForeignKey('account.website'))
    title = db.Column(db.String(200))
    link = db.Column(db.String(200))
    description = db.Column(db.String(1000))
    date = db.Column(db.DateTime)
    enclosure = db.Column(db.String(200))

    def __repr__(self):
        return f"Activity: {self.title}"

