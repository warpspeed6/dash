#!/usr/bin/python
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import boto3

app = Flask(__name__)


 
@app.route("/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    bpmvalue = "300"
    return render_template('chart.html', values=values, labels=labels, bpmvalue=bpmvalue)

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
