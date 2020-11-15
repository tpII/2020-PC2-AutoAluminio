from flask import redirect, render_template, request, url_for, session, abort
from app.helpers.vehicle import get_vehicle

def index():
    return render_template("home.html", vehicle=get_vehicle())

def stop():
    get_vehicle().stop()
    return redirect(url_for("index"))

def up():
    get_vehicle().up()
    return redirect(url_for("index"))

def down():
    get_vehicle().down()
    return redirect(url_for("index"))

def right():
    get_vehicle().right()
    return redirect(url_for("index"))

def left():
    get_vehicle().left()
    return redirect(url_for("index"))


