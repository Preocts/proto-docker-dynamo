from __future__ import annotations

import logging

import flask

from .store import init_store

logging.basicConfig(level="DEBUG")

app = flask.Flask(__name__)


@app.get("/")
def index() -> flask.Response:
    print("EGG")
    init_store()
    template = flask.render_template("index.html")
    return flask.make_response(template)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=9090,
        debug=True,
        load_dotenv=False,
    )
