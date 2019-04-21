from flask import Flask, request
import re
import uuid

app = Flask(__name__)

@app.route('/')
def hello_world(): 
  return 'Working!'


@app.route('/create-tiny', methods=['POST'])
def create_tiny(): 
  if request.method == 'POST':
    url, duration = request.get_json().values()
    if re.match("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$", url): 
      safety = 0
      while safety < 100: 
        url_code = uuid.uuid4()
        print(request.get_json())
        print(url_code)
        safety += 1
      return 'working!'
    else: 
      return 'not a valid url'