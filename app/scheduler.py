import atexit
import os
import threading
import concurrent.futures

from apscheduler.schedulers.background import BackgroundScheduler

from . import app, db
from .models import Activity, Art, Video
from .db_updates import *




def say_hello():
    print("Hello World")



def update_all():
    print('update started')
    try:
        update_github_rss('Quattro-Bajeena', Activity, db)
        # update_mal_rss('Paraon', Activity, db)
        # update_tweets_rss(30, Activity, db)
        # update_yt_rss(feed_url, Activity, db)
        # update_videos_db(Video, db)
        # add_files(art_folder, categories, Art, db)
        # remove_files(art_folder, Art, db)
        print('update finished')
        return True
    except:
        print('couldnt update')
        return False
    


def update_all_thread():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(update_all)
        app.logger.info(f'update status: {f1.result()}')
        return f1.result()
        

@app.before_first_request
def schedule_start():
    print('schedule start')
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_github_rss, args=['Quattro-Bajeena', Activity, db], trigger='interval', hours=12)
    scheduler.add_job(func=update_mal_rss, args=['Paraon', Activity, db], trigger='interval', hours=12)
    scheduler.add_job(func=update_tweets_rss, args=[30, Activity, db], trigger='interval', hours=12)
    scheduler.add_job(func=update_yt_rss, args=[feed_url, Activity, db], trigger='interval',hours=12)
    scheduler.add_job(func=update_videos_db, args=[Video, db], trigger='interval', hours=24)
    scheduler.add_job(func=add_files, args=[art_folder, categories, Art, db], trigger='interval', hours=24)
    scheduler.add_job(func=remove_files, args=[art_folder, Art, db], trigger='interval', hours=24)
    

    #scheduler.add_job(func=say_hello, trigger='interval', seconds=3)

    atexit.register(lambda: scheduler.shutdown())
    scheduler.start()


#print('consumer key: ',os.environ.get('YO'))


