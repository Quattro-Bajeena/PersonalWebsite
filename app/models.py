from app import db
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

    def __repr__(self):
        return f"Site: {self.website}; Nickname: {self.nickname}."


class Art(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    category = db.Column(db.String(32), nullable=False)
    src = db.Column(db.String(128))
    description = db.Column(db.String(1024))
    orientation = db.Column(db.String(32))
