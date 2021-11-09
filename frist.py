# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:05:14 2021

@author: indin
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index:
    return 'Index Page'

@app.route('/hello')
def hello():
   return 'Hi Akhil'
           
if __name__ == '__main__':
        app.run()
        
        
        
   