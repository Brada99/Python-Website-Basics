from flask import Flask, render_template

print ('HELLO')
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/Social')
def social():
  return render_template('social.html')
  
# this if command runs the app rather than changing the run command to work with flask
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)