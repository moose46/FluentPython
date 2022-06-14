__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# tracking.py was created on June 10 2022 @ 10:52 AM
# Project: FluentPython
#
from http import HTTPStatus

from flask import Flask, request, Response
from flask_injector import FlaskInjector

from interfaces import ViewsStorageBackend
import di


app = Flask(__name__)

PIXEL = (
    b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00"
    b"\x00\x00\xff\xff\xff!\xf9\x04\x01\x00"
    b"\x00\x00\x00,\x00\x00\x00\x00\x01\x00"
    b"\x01\x00\x00\x02\x01D\x00;"
)


@app.route("/track")
def track(storage: ViewsStorageBackend):
    try:
        referer = request.headers["Referer"]
    except KeyError:
        return Response(status=HTTPStatus.BAD_REQUEST)
    try:
        storage.increment(referer)
    except Exception as e:
        print(e)

    return Response(
        PIXEL,
        headers={
            "Content-Type": "image/gif",
            "Expires": "Mon, 01 Jan 1990 00:00:00 GMT",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
        },
    )


@app.route("/stats")
def stats(storage: ViewsStorageBackend):
    try:
        print(type(storage))
        return storage.most_common(5)
    except Exception as e:
        print(e)


@app.route("/")
def index():
    return """
    <html>
    <head></head>
    <body>
    <a href="/poke">/poke</a></br>
    <a href="/stats">/stats</a>
    </body>
    </html>
    """


@app.route("/poke")
def poke():
    return """
    <html>
    <head></head>
    <body><img src="/track">
    <h1>Poke Me Again</h1>
    <a href="/poke">/poke</a></br>
    <a href="/stats">/stats</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    FlaskInjector(app=app, modules=[di.SQLiteModule()])
    print(type(app))
    app.run(host="0.0.0.0", port=8003)