import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from app.update_github import update_github_rss
from app.update_mal import update_mal_rss
from app.update_twitter import update_tweets_rss
from app.update_yt import update_yt_rss, feed_url
from app.update_img import add_files, remove_files, art_folder, categories

def say_hello():
    print("Hello World")

scheduler = BackgroundScheduler()
scheduler.add_job(func=update_github_rss, args=['Quattro-Bajeena'], trigger='interval', hours=24)
scheduler.add_job(func=update_mal_rss, args=['Paraon'], trigger='interval', hours=24)
scheduler.add_job(func=update_tweets_rss, args=[30], trigger='interval', hours=24)
scheduler.add_job(func=update_yt_rss, args=[feed_url], trigger='interval',hours=24)
scheduler.add_job(func=add_files, args=[art_folder, categories], trigger='interval', seconds=10)
scheduler.add_job(func=remove_files, args=[art_folder], trigger='interval', seconds=20)

#scheduler.add_job(func=say_hello, trigger='interval', seconds=3)


atexit.register(lambda: scheduler.shutdown())
scheduler.start()


