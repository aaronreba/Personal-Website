import sys

import os
import platform
import flask

import datetime

app = flask.Flask(__name__)

start_time = datetime.datetime.utcnow()

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    Stolen from http://code.activestate.com/recipes/577879-create-a-nested-dictionary-from-oswalk/
    """
    directory_tree = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], directory_tree)
        parent[folders[-1]] = subdir
    return directory_tree

@app.route('/')
def index():
    now = datetime.datetime.utcnow()
    os_name = os.name
    platform_system = platform.system()
    platform_release = platform.release()

    directory_structure = get_directory_structure('/')

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
