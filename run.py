
#only thing needed to start the app
from app import app


from app import db
from app.models import Nickname, Account, Art, Video, Activity

@app.shell_context_processor
def make_shell_context():
    return{'db' : db, 'Nickname' : Nickname, 'Account' : Account, 'Art' : Art, 'Video' : Video, 'Activity' : Activity}