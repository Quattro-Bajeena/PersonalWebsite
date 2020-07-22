from . import app, db
from .models import Nickname, Account, Art, Activity, Video
from .scheduler import update_all_thread
from flask import render_template, url_for, redirect, request, send_from_directory
from pathlib import Path
import os
@app.context_processor
def feed_activities():
    activities = Activity.query.order_by(Activity.date.desc())
    icon_path = Path().parent.joinpath('Images/Icons/')
    return dict(activities = activities, icon_path = icon_path.as_posix())




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update-activities')
def update_activities():
    result = update_all_thread()
    return result



@app.route('/nicknames/<nick>')
def nick_page(nick : str):
    nickname = Nickname.query.get_or_404(nick)
    accounts = nickname.accounts.all()
    path = Path().parent.joinpath('Images/Icons/')
    return render_template('nick.html', nickname = nickname, accounts = accounts, path = path.as_posix())

# Work Pages

@app.route('/Art')
def art_page():
    return render_template('Work/art.html')

@app.route('/Art/<category>')
def art_category_page(category : str):
    from .db_updates import categories

    art_category = next(item for item in categories if item["page"] == category)['category']
    path = next(item for item in categories if item["page"] == category)['folder_path']

    art_pieces = Art.query.filter(Art.category==art_category).order_by(Art.name)
    # path = Path().parent.joinpath(f'Images/Art/{category}')
    print(path)
    return render_template(f'Work/Work_piece/Art/{category}.html', path = path.as_posix(), category = category, art_pieces = art_pieces)

#
@app.route('/Programming')
def programming_page():
    return render_template('Work/programming.html')

@app.route('/Programming/<project>')
def programming_projects_page(project : str):
    return render_template(f'Work/Work_piece/Programming/{project}.html', project = project)

#
@app.route('/Games')
def games_page():
    return render_template('Work/games.html')

@app.route('/Games/<game>')
def games_game(game : str):
    return render_template(f'Work/Work_piece/Games/{game}.html', game = game)

#
@app.route('/Videos')
def videos_page():
    videos = Video.query.order_by(Video.date.desc())
    return render_template('Work/videos.html', videos=videos)

@app.route('/Videos/<video>')
def video_page(video : str):
    video = Video.query.get_or_404(video)
    return render_template('/Work/Work_piece/video.html', video=video)

@app.route('/Images/<name>')
def image_display(name : str):
    image = Art.query.get_or_404(name)
    category = image.category
    from .db_updates import categories
    path = next(item for item in categories if item["category"] == category)['folder_path']
    return send_from_directory(Path('static').joinpath(path), image.src)

@app.route('/text_files/<name>')
def articles_raw(name : str):
    path = Path('static/articles')
    return send_from_directory(path, name)
    
