from time import sleep
import datetime
from jikanpy import Jikan
import json

from app import db
from app.models import Activity

def update_mal_rss(user : str):
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

            new_activity = Activity(id = id, title=title, link = link, date = date, website = 'MAL')
            db.session.add(new_activity)
            print(f'entry added - {title}')

    db.session.commit()

if __name__ =='__main__':
    update_mal_rss('Paraon')


