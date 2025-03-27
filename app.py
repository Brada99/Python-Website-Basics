from flask import Flask

print ('HELLO')
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"
  
# this if command runs the app rather than changing the run command to work with flask
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)