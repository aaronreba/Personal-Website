import sys

import os
import platform
import flask

import datetime

app = flask.Flask(__name__)

start_time = datetime.datetime.utcnow()

def get_directory_structure(directory_structure, rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """

    directory_structure[rootdir] = {}
    try:
      for child in os.listdir(rootdir):
        child_path = os.path.join(rootdir, child)
        if os.path.isdir(child_path):
          get_directory_structure(directory_structure, child_path)
        else:
          directory_structure[rootdir][child_path] = {}
    except PermissionError as e:
      print('Could not list {}'.format(rootdir))

@app.route('/')
def index():
    now = datetime.datetime.utcnow()
    os_name = os.name
    platform_system = platform.system()
    platform_release = platform.release()

    directory_structure = {}
    get_directory_structure(directory_structure, '/')

    page_data = {}
    page_data['now'] = now
    page_data['start_time'] = start_time
    page_data['os_name'] = os_name
    page_data['platform_system'] = platform_system
    page_data['platform_release'] = platform_release
    page_data['directory_structure'] = directory_structure

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
