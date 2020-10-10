import feedparser
import json
import urllib.request


import datetime
from app import db
from app.models import Activity

from flask_sqlalchemy import SQLAlchemy

def update_github_rss(username : str, Activity, db : SQLAlchemy):
    any_added = False
    repos_url = f'https://api.github.com/users/{username}/repos'
    repo_names = []

    with urllib.request.urlopen(repos_url) as url:
        repos = json.loads(url.read().decode())
        for repo in repos:
            repo_names.append(repo['name'])
            

    repo_feed_urls = {f'{name}' : f'https://github.com/{username}/{name}/commits/master.atom' for name in repo_names }



    for repo_name, repo_url in repo_feed_urls.items():
        feed = feedparser.parse(repo_url)

        for commit in feed.entries:
            print(f'{repo_name} - {commit.title}')
            if not Activity.query.get(commit.id):
                id = commit.id
                title = f'{repo_name} - {commit.title}'
                link = commit.link
                date = datetime.datetime(*(commit.updated_parsed[0:6]))
                
                new_activity = Activity(id = id, title=title, link = link, date = date, website = 'GitHub')
                db.session.add(new_activity)
                any_added = True
                print(f'added: {title}')
            
    if not any_added:
        print('no new commits')
        
    db.session.commit()

if __name__=='__main__':
    update_github_rss('Quattro-Bajeena')
    
        