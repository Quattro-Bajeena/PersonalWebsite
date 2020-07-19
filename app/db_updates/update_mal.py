from time import sleep
import datetime
from jikanpy import Jikan
import json


from flask_sqlalchemy import SQLAlchemy

def update_mal_rss(user : str, Activity, db : SQLAlchemy):
    any_added = False
    jikan = Jikan()
    sleep(0.5)
    history = jikan.user(username=user, request = 'history')


    entry = history['history'][0]

    for entry in history['history']:
        name = entry['meta']['name']
        number = entry['increment']

        id = f'mal_{name}_ep_{number}'

        if not Activity.query.get(id):
            if entry['meta']['type'] == 'anime':
                action = 'Watched'
                increment = 'episode'
            else:
                action = 'Read'
                increment = 'chapter'

            title = f"{action} {name} {increment} {number}"
            link = entry['meta']['url']

            date = datetime.datetime.fromisoformat(entry['date'])

            new_activity = Activity(id = id, title=title, link = link, date = date, website = 'My Anime List')
            db.session.add(new_activity)
            any_added = True
            print(f'entry added - {title}')


    if not any_added:
        print('no new MAL entires')
    db.session.commit()

if __name__ =='__main__':
    update_mal_rss('Paraon')


