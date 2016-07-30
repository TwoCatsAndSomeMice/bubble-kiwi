#!/usr/bin/env python2

from flask import Flask, request, render_template, redirect, url_for
app = Flask("Bubble Kiwi")

@app.errorhandler(404)
def not_found(error):
    return redirect("http://bubble.kiwi/")

@app.route("/")
@app.route("/<refer>")
def referal(refer=None):
    title = request.args.get("t", "Bubble")
    image_url = request.args.get("i", "Bursting the Bubble")
    description = request.args.get("d", "")

    return render_template("redirect.html", title=title, image=image_url, description=description)

if __name__ == "__main__":
    app.run()
