import pprint


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, resp):
        error_log = environ['wsgi.errors']

        pprint.pprint(('REQUEST', environ), stream=error_log)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=error_log)
            return resp(status, headers, *args)

        return self._app(environ, log_response)
