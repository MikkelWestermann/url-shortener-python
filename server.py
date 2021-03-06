from flask import Flask, request, redirect
from redis import Redis
import string
import random
import re

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def root(): 
  return 'Working!'

@app.route('/<code>')
def get_code (code): 
  if redis.exists(code): 
    url = redis.get(code)
    return redirect(url, code=302)
  return 'Code doesn\'t exist'

@app.route('/create-tiny', methods=['POST'])
def create_tiny(): 
  if request.method == 'POST':
    url, duration = request.get_json().values()
    if re.match(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$", url): 
      safety = 0
      while safety < 10: 
        url_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        if not redis.exists(url_code): 
          redis.set(url_code, url, duration)
          return url_code 
        safety += 1 
      return 'Could not add link'
    else: 
      return 'not a valid url'