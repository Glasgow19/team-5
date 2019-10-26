from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/exhibit')
def exhibit():
    return render_template("exhibit.html")

@app.route('/choice')
def choice():
    return render_template("choice.html")


@app.route('/levels')
def levels():
    return render_template("levels.html")


@app.route('/qr')
def qr():
    return render_template("qr.html")


@app.route('/yes')
def yes():
    return render_template("yes.html")

@app.route('/index')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run()
