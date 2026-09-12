import os, json

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = os.environ['SECRET_KEY']

class Episode:
    def __init__(self, season, episode, title, air_date):
        self.season = season
        self.episode = episode
        self.title = title
        self.air_date = air_date

    def __str__(self):
        return f"'{self.title}' is episode {self.episode} of season {self.season} originally aired {self.air_date}"

    def summary(self):
        return str(self)

# All episodes used for search on episodes.html using above class to make storing and retrieving information easier
with open("static/data/episodes.json", "r") as file:
    episode_data = json.load(file)

all_episodes = [
    Episode(
        episode["season"],
        episode["episode"],
        episode["title"],
        episode["air_date"]
    )
    for episode in episode_data
]

# votes used by home.html to determin which image is used based on the current count on ranking.html
votes = {
    "Frasier": 0,
    "Niles": 0,
    "Martin": 0,
    "Daphne": 0,
    "Roz": 0
}

@app.route("/")
def home():
    # Max used to find character with highest votes form ranking.html
    winner = max(votes, key=votes.get)
    # Allows the winning character image to be displayed on the home.html
    images = {
        "Frasier": "frasier.webp",
        "Niles": "niles.webp",
        "Martin": "martin.webp",
        "Daphne": "daphne.webp",
        "Roz": "roz.webp",
    }
    return render_template("home.html", winner=winner, winner_image=images[winner])

@app.route("/episodes", methods=["GET", "POST"])
def episodes_page():
    results = all_episodes
    query = ""

    # searches through all catorgories and generates a list of teh episodes that match the search input
    if request.method == "POST":
        query = request.form.get("search_query", "").strip()
        if query:
            results = [
                e for e in all_episodes 
                if query.lower() in e.title.lower()
                or query.lower() in e.season.lower()
                or query.lower() in e.episode.lower()
                or query.lower() in e.air_date.lower()
                ]
    return render_template("episodes.html", results=results, query=query)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ranking", methods=["GET", "POST"])
def ranking():
    # Adds 1 to selected characture and returns to ranking.html with increase in choose character counter
    if request.method == "POST":
        character = request.form.get("character")
        if character in votes:
            votes[character] += 1
        return redirect("/ranking")

    sorted_votes = dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))

    return render_template("ranking.html", votes=sorted_votes)

@app.route("/contact", methods=("GET", "POST"))
def contact():
    # Basic form with flash and error validation
    if request.method == "POST":
        name = request.form.get("name", " ").strip()
        email = request.form.get("email", " ").strip()
        subject = request.form.get("subject", " ").strip()
        message = request.form.get("message", " ").strip()

        errors = []
        if not name:
            errors.append("Name is required")
        if not email:
            errors.append("Email is required")
        if not subject:
            errors.append("Subject is required")
        if not message:
            errors.append("Message is required")

        if errors:
            return render_template("contact.html", errors=errors, name=name, email=email, subject=subject, message=message)

        flash("Thank you for your message")
        return redirect("/contact")
    return render_template("contact.html", errors=[], name="", email="", subject="", message="")

if __name__ == "__main__":
    app.run(debug=False)
