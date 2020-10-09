from . import app, db
from .models import Nickname, Account, Art, Activity, Video
from .celery_tasks import update_activities_async
from flask import render_template, url_for, redirect, request, send_from_directory, jsonify, make_response
from pathlib import Path
import os


@app.context_processor
def feed_activities():
    activities = Activity.query.order_by(Activity.date.desc())
    icon_path = app.config['ICONS_FOLDER']
    return dict(activities = activities, icon_path = icon_path.as_posix())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update-activities')
def update_activities():
    print('start update activities')
    task = update_activities_async.apply_async()
    
    return {"status_url" : url_for('task_status', task_id=task.id)}, 201
    

@app.route('/status/<task_id>')
def task_status(task_id):
    task = update_activities_async.AsyncResult(task_id)
    print(task.state)
    
    if task.state == "PENDING":
        response={
            'finished': False,
            'state' : task.state,
            'current':0,
            'total': 1,
            'status': "pending"
        }
    elif not task.ready():
        response={
            'finished': False,
            'state' : task.state,
            'current':task.info.get('current', 0),
            'total': task.info.get('total', 0),
            'status': task.info.get('status', '')
        }
    else:
        response={
            'finished': True,
            'state' : task.state,
            'current': 1,
            'total':  1,
            'status': 'Update Completed'
        }
    
    return response
    
@app.route('/nicknames/<nick>')
def nick_page(nick : str):
    nickname = Nickname.query.get_or_404(nick)
    accounts = nickname.accounts.all()
    path = app.config['ICONS_FOLDER']
    return render_template('nick.html', nickname = nickname, accounts = accounts, path = path.as_posix())

# Work Pages

@app.route('/Art')
def art_page():
    return render_template('Work/art.html')

@app.route('/Art/<category>')
def art_category_page(category : str):
    from .db_updates import categories

    try:
        art_category = next(item for item in categories if item["page"] == category)['category']
        path = next(item for item in categories if item["page"] == category)['folder_path']
        art_pieces = Art.query.filter(Art.category==art_category).order_by(Art.name)
        return render_template(f'Work/Work_piece/Art/{category}.html', path = path.as_posix(), category = category, art_pieces = art_pieces)
    except:
        return redirect(url_for('art_page'))
    # path = Path().parent.joinpath(f'Images/Art/{category}')
    
    
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
    return send_from_directory(Path('static') / path, image.src)

@app.route('/text_files/<name>')
def articles_raw(name : str):
    path = Path('static') / app.config['ARTICLES_FOLDER']
    return send_from_directory(path, name)
    
