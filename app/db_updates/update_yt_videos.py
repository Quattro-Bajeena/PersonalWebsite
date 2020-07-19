import os
from datetime import datetime
from youtube_api import YouTubeDataAPI, youtube_api_utils
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv('.env')
API_KEY = os.environ.get('YT_API_KEY')
yt = YouTubeDataAPI(API_KEY)


def update_videos_db(Video, db : SQLAlchemy):
    my_videos_id = yt.get_videos_from_playlist_id(playlist_id='UUINPzzjxRzGOq4Pex5r3EKg')
    my_videos = [yt.get_video_metadata(video['video_id']) for video in my_videos_id]

    any_new = False
    for video in my_videos:
        if not Video.query.get(video['video_title']):
            title = video['video_title']
            id = video['video_id']
            link = f"https://www.youtube.com/watch?v={video['video_id']}"
            thumbanil = video['video_thumbnail']
            description = video['video_description']
            date = datetime.fromtimestamp(video['video_publish_date']) 
            
            new_video = Video(id= id,title=title, link=link, thumbnail=thumbanil, description=description, date = date)
            db.session.add(new_video)
            any_new = True
            print(f'video added: {title}')

    if not any_new:
        print("no new videos")

    db.session.commit()


if __name__=='__main__':
    update_videos_db(Video, db)


    
    
    
    



