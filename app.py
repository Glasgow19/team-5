from flask import Flask,render_template,request
import json
import googleTTS

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
    with open('db.json') as json_file:
        data = json.load(json_file)
    exhibit_id = request.args.get('id',default=1,type=int)

    test = data[exhibit_id]['HOH']

    if data[exhibit_id]['HOH'] == 'True':
       hearing = 'style = "color : purple"'
    else:
        hearing = ""
    if data[exhibit_id]['HOS'] == "True":
       hearing = 'style = "color : purple"'
    else:
        sight = ""
    if data[exhibit_id]['HOM'] == "True":
       hearing = 'style = "color : purple"'
    else:
        other = ""

    return render_template("exhibit.html", exhibit_description=data[exhibit_id]['Description'],exhibit_name=data[exhibit_id]['Exhibit name'],sight=sight,hearing=hearing,other=other)


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


@app.route('/tts')
def tts():
    return render_template("tts.html")

@app.route('/api/tts',methods=['POST'])
def tts_api():
    req_data = request.get_json()
    response = googleTTS.tts(req_data['text'])
    return response

if __name__ == '__main__':
    app.run()
