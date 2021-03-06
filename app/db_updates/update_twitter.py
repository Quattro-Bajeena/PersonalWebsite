import tweepy
import datetime
import os
from dotenv import load_dotenv
#from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from flask_sqlalchemy import SQLAlchemy
load_dotenv('.env')

auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCES_KEY'), os.environ.get('ACCES_SECRET'))

api = tweepy.API(auth, wait_on_rate_limit=True)
turtle_guy = api.get_user('turtle_guy_')


def update_tweets_rss(days_back : int, Activity, db : SQLAlchemy):
    any_added = False
    now = datetime.datetime.now()
    cutoff_date = now - datetime.timedelta(days=days_back)

    for tweet in tweepy.Cursor(api.user_timeline, id = turtle_guy.id, tweet_mode='extended').items():

        #!!! its gonna itarate through like 6000 tweets if it doesnt break
        if tweet.created_at < cutoff_date:
            #print("older tweets")
            break

        if not tweet.in_reply_to_status_id and not Activity.query.get(tweet.id_str):
            id = tweet.id_str
            title = tweet.full_text[:50] + (tweet.full_text[50:] and '..')
            link = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            description = tweet.full_text
            date = tweet.created_at

            if 'media' in tweet.entities:
                enclosure = tweet.entities['media'][0]['media_url']
            else:
                enclosure = None

            new_activity = Activity(id = id, title = title, link = link, description = description, date = date, enclosure = enclosure, website="Twitter")

            db.session.add(new_activity)
            any_added = True
            print(f'tweet added - {title}')
        
    if not any_added:
        print("no new tweets")
    
    db.session.commit()
        
        
if __name__ == '__main__':
    update_tweets_rss(30)

        

    


