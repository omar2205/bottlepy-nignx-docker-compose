import os
from bottle import Bottle, route, run, response

from routes import v1

DEBUG = os.environ.get('ENV', False) != 'prod'
PORT = os.environ.get('PORT', 8080)

app = Bottle()
app.mount('/api/v1', v1.v1_app)

@app.route('/api')
def home():
  return 'Hello World'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=PORT, server='cheroot',
      debug=DEBUG)

