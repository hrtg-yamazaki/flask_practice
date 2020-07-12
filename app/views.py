from flask import Flask, render_template
from config.settings import get_secret


app = Flask(__name__)
app.secret_key = get_secret()


@app.route("/")
def index():
    return render_template("layout.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5020)
