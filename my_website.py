from app import app, db
from app.models import Nickname, Account

@app.shell_context_processor
def make_shell_context():
    return{'db' : db, 'Nickname' : Nickname, 'Account' : Account}

if __name__ == "__main__":
    app.run(debug=True)