import os
# from os import time, path
from flask import Flask, render_template, request

file_path = None

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, "images")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        file_path = os.path(r"destination")
        print(destination, file_path)
        file.save(destination)
    return render_template("complete.html")


@app.route('/no_of_lines') 
def no_of_lines(): 
    return render_template("no_of_lines.html", no_of_lines = no_of_lines())

@app.route('/file_size') 
def file_size(): 
    return render_template("file_size.html", file_size = file_size())

@app.route('/date_modified') 
def date_modified(): 
    return render_template("date_modified.html", date_modified = last_modified())

@app.route('/all_three') 
def all_three(): 
    return render_template("all_three.html", no_of_lines = no_of_lines(), file_size = file_size(), date_modified = last_modified())

def no_of_lines():
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    return i+1

def last_modified():
    return("Last modified: %s" % os.time.ctime(os.path.getmtime("file_path")))

def file_size():
    return(os.path.getsize("file_path"))

if __name__=="__main__":
    app.run(port=9876, debug=True)