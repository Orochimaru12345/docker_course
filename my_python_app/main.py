import cherrypy
import os


class MyPythonApp(object):
    @cherrypy.expose
    def index(self):
        return "<h1>HELLO</h1>"


if __name__ == '__main__':
    host = os.getenv("APP_HOST") if os.getenv("APP_HOST") is not None else "0.0.0.0"

    cherrypy.server.socket_host = host

    cherrypy.quickstart(MyPythonApp())
