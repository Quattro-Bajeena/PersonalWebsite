from app import app, db
from app.models import Nickname, Account
from flask import render_template, url_for
import pathlib

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nicknames/<nick>')
def nick_page(nick : str):
    nickname = Nickname.query.get_or_404(nick)
    accounts = nickname.accounts.all()
    path = pathlib.Path().parent.joinpath('Images/Icons/')
    return render_template('nick.html', nickname = nickname, accounts = accounts, path = path.as_posix())

# Work Pages

@app.route('/Art')
def art_page():
    return render_template('Work/art.html')

@app.route('/Art/<category>')
def art_category_page(category : str):
    return render_template(f'Work/Work_piece/Art/{category}.html', category = category)


@app.route('/Programming')
def programming_page():
    return render_template('Work/programming.html')

@app.route('/Programming/<project>')
def programming_projects_page(project : str):
    return render_template(f'Work/Work_piece/Programming/{project}.html', project = project)

@app.route('/Games')
def games_page():
    return render_template('Work/games.html')

@app.route('/Games/<game>')
def games_game(game : str):
    return render_template(f'Work/Work_piece/Games/{game}.html', game = game)

@app.route('/Videos')
def videos_page():
    return render_template('Work/videos.html')