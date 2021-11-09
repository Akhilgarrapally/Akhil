from flask import Flask
from flask_caching import  Cache
from random import randint
cache = Cache()
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
@app.route('/')
@cache.cached(timeout=2)
def hello_world():
    randomnum =  randint(1,200)
    return f'<h1> THE NUMBER IS :{randomnum}</h1>'

if __name__ == '__main__':
    app.run()
    
    
    
    

    