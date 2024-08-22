from __future__ import annotations

import flask

app = flask.Flask(__name__)


@app.get("/")
def index() -> flask.Response:
    template = flask.render_template("index.html")
    return flask.make_response(template)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=9090,
        debug=True,
        load_dotenv=False,
    )
