import os
from pathlib import Path

basedir = Path(__file__).resolve().parent


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nevel-guess'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + basedir.joinpath('app.db').as_posix()

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ofc they're inside static folder, but they will be got by a url_for('static', path...) function
    ARTICLES_FOLDER = Path('articles')
    IMAGES_FOLDER = Path('Images')
    ART_FOLDER = IMAGES_FOLDER / 'Art'
    ICONS_FOLDER = IMAGES_FOLDER / 'Icons'
    PROFILE_PICS_FOLDER = IMAGES_FOLDER / 'Profile_Pics'
    WEBSITE_LOGOS_FOLDER = IMAGES_FOLDER / 'Website_Logos'


