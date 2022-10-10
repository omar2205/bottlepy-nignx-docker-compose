from bottle import Bottle

v1_app = Bottle()

@v1_app.route('/')
def home():
  return '/api/v1/ home'

