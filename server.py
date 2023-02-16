from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")  # Do not add the templates parent directory, Flask will automatically look for index.html in the templates directory


if __name__ == "__main__":
    app.run(debug=True)
