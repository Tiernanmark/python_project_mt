from flask import Flask, render_template, abort



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/episodes")
def episodes():
    return render_template("episodes.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__== "__main__":
    app.run(debug=True)

