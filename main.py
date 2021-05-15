from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about-me')
def about_me():
    return 'this is a new test!!'


if __name__ == "__main__":
    app.run()
