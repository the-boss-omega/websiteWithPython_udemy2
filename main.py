from flask import Flask
# אימפורט למדול פלאסק ליצירת אתרים
app = Flask(__name__)
@app.route('/')
def homepage():
  return ''\
  'wanna be a billionaire?'
  #function for the home page
app.run(host = '0.0.0.0')
# define host and listen any other website in this url an create yours