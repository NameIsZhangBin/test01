from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello python"


if __name__ == '__main__':
    app.run()


a1 = 1
a2 = 2