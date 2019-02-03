'''
Shin Tran
Python 230
Assignment 5

A microservice that provides the current Unix time or epoch time.
'''

import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    the_time = int(round(time.time()))
    return str(the_time)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)
