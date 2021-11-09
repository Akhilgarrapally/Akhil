from flask import Flask,redirect

app = Flask(__name__)

@app.route('/hello')
def hello():
    return redirect("https://example.com", code=302)

if __name__ == '__main__':
    app.run()