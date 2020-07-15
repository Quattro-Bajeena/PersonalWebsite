from app import app, db
from app.models import Nickname, Account, Art, Video, Activity

@app.shell_context_processor
def make_shell_context():
    return{'db' : db, 'Nickname' : Nickname, 'Account' : Account, 'Art' : Art, 'Video' : Video, 'Activity' : Activity}

if __name__ == "__main__":
    app.run(debug=True)