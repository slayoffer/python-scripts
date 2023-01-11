#!/usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def html_page():
    return render_template('site.html')

app.run()
# app.run(debug=True)