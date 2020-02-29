from flask import Flask
from LoggingMiddleware import LoggingMiddleware

app = Flask(__name__)

@app.route('/')
def print_request():
    app.logger.info("Print the request!")
    return "Check log for request info.\n"


if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run(host='0.0.0.0', port=5000)



