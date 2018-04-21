import sys
sys.path.append('./lib/python2.7/site-packages/')

import os
import platform
import flask

import datetime

app = flask.Flask(__name__)

start_time = datetime.datetime.utcnow()

@app.route('/')
def index():
    now = datetime.datetime.utcnow()
    os_name = os.name
    platform_system = platform.system()
    platform_release = platform.release()

    page_data = {}
    page_data['now'] = now
    page_data['start_time'] = start_time
    page_data['os_name'] = os_name
    page_data['platform_system'] = platform_system
    page_data['platform_release'] = platform_release

    return flask.render_template(
        'index.html',
        **page_data)

@app.route('/resume')
def resume():
    return flask.render_template('resume.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
