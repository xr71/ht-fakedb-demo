from flask import Flask
from flask import render_template
from flask import jsonify
from backend.fakedbapi import apifetchall
from backend.fakedbapi import sendtodom

app = Flask(__name__)

@app.route("/")
def index():
    data = sendtodom()
    return render_template("index.html", data=data)


@app.route("/api/")
def backend():

    jsondata = apifetchall()

    return jsonify(jsondata)

if __name__ == "__main__":
    app.run()
