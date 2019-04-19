from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(): 
  print('Shit has been hit')
  return 'Hello World!!!!'
 