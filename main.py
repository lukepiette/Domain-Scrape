
from flask import Flask, escape, url_for, request, render_template, redirect, session, g
import random
import csv


app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def index():
	with open('./static/domains.csv','r') as CSV:
		data = CSV.read()
	data = data.replace('\n','|')
	return render_template('index.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)
