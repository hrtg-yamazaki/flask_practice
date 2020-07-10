from flask import Flask

app = Flask(__name__)


html = """\
<h1 style='margin:0; color:steelblue;'>Hello, world!</h1>
"""


@app.route("/")
def index():
    return html


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5020)
