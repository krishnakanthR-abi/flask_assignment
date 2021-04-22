""" Flask application that uploads file and displays the properties"""
import os
import time
from flask import Flask, render_template, request

FILE_NAME = ""

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    """function to call upload html template"""
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    """function to upload the file at the given path"""
    global FILE_NAME
    target = os.path.join(APP_ROOT, "images")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        FILE_NAME = destination
        file.save(destination)
    return render_template("complete.html")


@app.route("/no_of_lines")
def no_of_lines():
    """function to call the no_of_lines html template"""
    return render_template("no_of_lines.html", no_of_lines=no_of_lines())


@app.route("/file_size")
def file_size():
    """function to call the file_size html template"""
    return render_template("file_size.html", file_size=file_size())


@app.route("/date_modified")
def date_modified():
    """function to call the date_modified html template"""
    return render_template("date_modified.html", date_modified=last_modified())


@app.route("/all_three")
def all_three():
    """ function to call three properties at single occurence"""
    return render_template(
        "all_three.html",
        no_of_lines=no_of_lines(),
        file_size=file_size(),
        date_modified=last_modified(),
    )


def no_of_lines():
    """Function to find number of lines in the uploaded file"""
    number_of_lines = len(open(FILE_NAME).readlines())
    return number_of_lines


def last_modified():
    """Function to find the date last modified of the uploaded file"""
    return "Last modified: %s" % time.ctime(os.path.getmtime(FILE_NAME))


def file_size():
    """Function to find the file size of the uploaded file"""
    return os.path.getsize(FILE_NAME)


if __name__ == "__main__":
    app.run(port=9876, debug=True)
