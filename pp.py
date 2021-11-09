from flask import Flask
from flask_sslify import SSLify
 
app = Flask(__name__)
sslify = SSLify(app)
 
@app.route('/hello')
def hello_world():
    return 'Custom Hello from Flask!'

if __name__ == "__main__":
    app.run()