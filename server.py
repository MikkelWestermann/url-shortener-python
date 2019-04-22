from flask import Flask, request, redirect
from redis import Redis
import re
import uuid

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello_world(): 
  result = redis.get('123')
  print(result.decode('utf-8'))
  return f'Working!!! and this is the result: {result}'

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
    if re.match("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$", url): 
      safety = 0
      while safety < 1: 
        url_code = str(uuid.uuid4())
        print(url_code)
        redis.set(url_code, url)
        safety += 1 
      return 'working!' 
    else: 
      return 'not a valid url'