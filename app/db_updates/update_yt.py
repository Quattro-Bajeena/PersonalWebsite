import feedparser
import datetime
from flask_sqlalchemy import SQLAlchemy

feed_url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCINPzzjxRzGOq4Pex5r3EKg'

def update_yt_rss(feed_url : str, Activity, db : SQLAlchemy):
    any_added = False
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        if not Activity.query.get(entry.id):
            id = entry.id
            title = entry.title
            link = entry.link
            description = entry.description
            date = datetime.datetime(*(entry.published_parsed[0:6]))
            enclosure = entry.media_thumbnail[0]['url']

            new_activity = Activity(id = id, title=title, link = link, description = description, date = date, enclosure = enclosure, website = 'YouTube')
            db.session.add(new_activity)
            any_added = True
            print(f'added: {title}')
    
    if not any_added:
        print('no new videos')
        
    db.session.commit()


if __name__ == '__main__':
    update_yt_rss(feed_url)
        
    


