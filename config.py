import os
from pathlib import Path

basedir = Path(__file__).resolve().parent

#twitter keys
CONSUMER_KEY = 'RVfL3Z1KEOTEWeDFQJdSzhE0Z'
CONSUMER_SECRET = 'gyJlTGV00o0eoAoXKj7xvgysNNW19asqlImWL4ov1LRV3QQFbm'
ACCESS_KEY = '1170068040911859712-HS9ynYpqEuc8PTIAVKCutNcmeBedjy'
ACCESS_SECRET = 'RVQgyULZNWUqTegEvyP45Omcbo5oCkkfss57hk04rYEHh'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nevel-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + basedir.joinpath('app.db').as_posix()

    SQLALCHEMY_TRACK_MODIFICATIONS = False


