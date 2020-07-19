import os
from pathlib import Path

basedir = Path(__file__).resolve().parent


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nevel-guess'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + basedir.joinpath('app.db').as_posix()

    SQLALCHEMY_TRACK_MODIFICATIONS = False


