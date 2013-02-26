import sys
sys.path.append('./lib/python2.7/site-packages/')

import os
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/resume')
def resume():
    return flask.render_template('resume.html')

@app.route('/images')
def images():
    return flask.render_template('images.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
