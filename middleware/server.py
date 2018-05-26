from wsgiref.simple_server import make_server
from middleware.wsgi import application

httpd = make_server('127.0.0.1', 8000, application)
print("Serving HTTP on port 8000...")

httpd.handle_request()