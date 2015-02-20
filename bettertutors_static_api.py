from os import environ, path
from sys import platform

from bottle import Bottle, response, static_file

static_app = Bottle(catchall=False, autojson=True)


@static_app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'  # Take out '*' in production!


@static_app.route('<pathname:path>')  # No namespacing is asking for trouble!
def static_router(pathname):
    if not path.isdir('static'):
        response.status = 404
        return {'error': 'NotFound', 'error_message': 'static directory not existent'}
    return static_file(pathname, 'static')


if __name__ == '__main__':
    static_app.run(server='wsgiref' if platform == 'win32' else 'gunicorn',
                   host='0.0.0.0', port=int(environ.get('PORT', 5555)), debug=True)
