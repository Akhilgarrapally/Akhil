from flask import Flask, session
from flask_session import Session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisscecretkey'
app.config["SESSION_TYPE"] = "filesystem"
sess = Session(app)
@app.route('/set')
def set():
    session['key'] = 'Akhil'
    return 'ok'
@app.route('/get')
def get():
    return session.get('key')


if __name__ == "__main__":
	app.run()
