import atexit
import os
import threading
import time

from concurrent.futures import ThreadPoolExecutor, Future
from apscheduler.schedulers.background import BackgroundScheduler


from . import app, db
from .models import Activity, Art, Video
from .db_updates import *

update_functions = {
    #update_github_rss : ('Quattro-Bajeena', Activity, db),
    #update_mal_rss : ('Paraon', Activity, db),
    #update_tweets_rss : (30, Activity, db),
    #update_yt_rss : (feed_url, Activity, db),
    #update_videos_db : (Video, db),
    add_files : (art_folder, categories, Art, db),
    remove_files : (art_folder, Art, db)
}

def update_all() -> dict:
    print('update started')
    func_num = len(update_functions)
    
    for i, (func, args) in enumerate(update_functions.items()) :
        func(*args)
        yield {'progress' : True, 'current' : i, 'total' : func_num, 'status' : func.__name__}

    # for i in range(10):
    #     time.sleep(1)
    #     print(i)
    #     yield {'progress' : True,'current':i ,'total': 10, 'status' : f'Update nr. {i}'}
    
    print('update finished')
    return {'progress' : False}
    


def update_all_thread() -> dict:
    print("update all thred")
    with ThreadPoolExecutor() as executor:
        future = executor.submit(update_all, Activity, Video, Art, db)
        # app.logger.info(f'update status: {f1.result()}')
        return future.result()
        

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
    
    atexit.register(lambda: scheduler.shutdown())
    scheduler.start()




