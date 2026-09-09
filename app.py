import os

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

all_episodes = [
    Episode("S1", "E1", "The Good Son", "16 September 1993"),
    Episode("S1", "E2", "Space Quest", "23 September 1993"),
    Episode("S1", "E3", "Dinner At Eight", "30 September 1993"),
    Episode("S1", "E4", "I Hate Frasier Crane", "7 October 1993"),
    Episode("S1", "E5", "Here's Looking At You", "14 October 1993"),
    Episode("S1", "E6", "The Crucible", "21 October 1993"),
    Episode("S1", "E7", "Call Me Irresponsible", "28 October 1993"),
    Episode("S1", "E8", "Beloved Infidel", "4 November 1993"),
    Episode("S1", "E9", "Selling Out", "11 November 1993"),
    Episode("S1", "E10", "Oops", "18 November 1993"),
    Episode("S1", "E11", "Death Becomes Him", "2 December 1993"),
    Episode("S1", "E12", "Miracle On Third Or Fourth Street", "16 December 1993"),
    Episode("S1", "E13", "Guess Who's Coming To Breakfast", "6 January 1994"),
    Episode("S1", "E14", "Can't Buy Me Love", "20 January 1994"),
    Episode("S1", "E15", "You Can't Tell A Crook By His Cover", "27 January 1994"),
    Episode("S1", "E16", "The Show Where Lilith Comes Back", "3 February 1994"),
    Episode("S1", "E17", "A Mid-Winter Night's Dream", "10 February 1994"),
    Episode("S1", "E18", "And The Whimper Is...", "17 February 1994"),
    Episode("S1", "E19", "Give Him The Chair!", "17 March 1994"),
    Episode("S1", "E20", "Fortysomething", "31 March 1994"),
    Episode("S1", "E21", "Travels With Martin", "14 April 1994"),
    Episode("S1", "E22", "Author, Author", "5 May 1994"),
    Episode("S1", "E23", "Frasier Crane's Day Off", "12 May 1994"),
    Episode("S1", "E24", "My Coffee With Niles", "19 May 1994"),
    Episode("S2", "E1", "Slow Tango In South Seattle", "20 SEPTEMBER 1994"),
    Episode("S2", "E2", "The Unkindest Cut Of All", "27 SEPTEMBER 1994"),
    Episode("S2", "E3", "The Matchmaker", "4 OCTOBER 1994"),
    Episode("S2", "E4", "Flour Child", "11 OCTOBER 1994"),
    Episode("S2", "E5", "Duke's, We Hardly Knew Ye", "18 OCTOBER 1994"),
    Episode("S2", "E6", "The Botched Language Of Cranes", "1 NOVEMBER 1994"),
    Episode("S2", "E7", "The Candidate", "8 NOVEMBER 1994"),
    Episode("S2", "E8", "Adventures In Paradise: Part 1", "15 NOVEMBER 1994"),
    Episode("S2", "E9", "Adventures In Paradise: Part 2", "22 NOVEMBER 1994"),
    Episode("S2", "E10", "Burying A Grudge", "29 NOVEMBER 1994"),
    Episode("S2", "E11", "Seat Of Power", "13 DECEMBER 1994"),
    Episode("S2", "E12", "Roz In The Doghouse", "3 JANUARY 1995"),
    Episode("S2", "E13", "Retirement Is Murder", "10 JANUARY 1995"),
    Episode("S2", "E14", "Fool Me Once, Shame On You, Fool Me Twice...", "7 FEBRUARY 1995"),
    Episode("S2", "E15", "You Scratch My Book...", "14 FEBRUARY 1995"),
    Episode("S2", "E16", "The Show Where Sam Shows Up", "21 FEBRUARY 1995"),
    Episode("S2", "E17", "Daphne's Room", "28 FEBRUARY 1995"),
    Episode("S2", "E18", "The Club", "21 MARCH 1995"),
    Episode("S2", "E19", "Someone To Watch Over Me", "28 MARCH 1995"),
    Episode("S2", "E20", "Breaking The Ice", "18 APRIL 1995"),
    Episode("S2", "E21", "An Affair To Forget", "2 MAY 1995"),
    Episode("S2", "E22", "Agents In America: Part 3", "9 MAY 1995"),
    Episode("S2", "E23", "The Innkeepers", "16 MAY 1995"),
    Episode("S2", "E24", "Dark Victory", "23 MAY 1995"), 
    Episode("S3", "E1", "She's The Boss", "19 September 1995"),
    Episode("S3", "E2", "Shrink Rap", "26 September 1995"),
    Episode("S3", "E3", "Martin Does It His Way", "10 October 1995"),
    Episode("S3", "E4", "Leapin' Lizards", "31 October 1995"),
    Episode("S3", "E5", "Kisses Sweeter Than Wine", "7 November 1995"),
    Episode("S3", "E6", "Sleeping With The Enemy", "14 November 1995"),
    Episode("S3", "E7", "The Adventures of Bad Boy and Dirty Girl", "21 November 1995"),
    Episode("S3", "E8", "The Last Time I Saw Maris", "28 November 1995"),
    Episode("S3", "E9", "Frasier Grinch", "19 December 1995"),
    Episode("S3", "E10", "It's Hard To Say Goodbye If You Won't Leave", "9 January 1996"),
    Episode("S3", "E11", "The Friend", "16 January 1996"),
    Episode("S3", "E12", "Come Lie With Me", "30 January 1996"),
    Episode("S3", "E13", "Moon Dance", "6 February 1996"),
    Episode("S3", "E14", "The Show Where Diane Comes Back", "13 February 1996"),
    Episode("S3", "E15", "A Word To The Wiseguy", "20 February 1996"),
    Episode("S3", "E16", "Look Before You Leap", "27 February 1996"),
    Episode("S3", "E17", "High Crane Drifter", "12 March 1996"),
    Episode("S3", "E18", "Chess Pains", "26 March 1996"),
    Episode("S3", "E19", "Crane vs. Crane", "9 April 1996"),
    Episode("S3", "E20", "Police Story", "23 April 1996"),
    Episode("S3", "E21", "Where There's Smoke, There's Fired", "30 April 1996"),
    Episode("S3", "E22", "Frasier Loves Roz", "7 May 1996"),
    Episode("S3", "E23", "The Focus Group", "14 May 1996"),
    Episode("S3", "E24", "You Can Go Home Again", "21 May 1996")
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/episodes", methods=["GET", "POST"])
def episodes_page():
    results = all_episodes
    query = ""

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

votes = {
"Frasier": 0,
"Niles": 0,
"Martin": 0,
"Daphne": 0,
"Roz": 0
}

@app.route("/ranking", methods=["GET", "POST"])
def ranking():
    if request.method == "POST":
        character = request.form.get("character")
        if character in votes:
            votes[character] += 1
        return redirect("/ranking")

    sorted_votes = dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))

    return render_template("ranking.html", votes=sorted_votes)



@app.route("/contact", methods=("GET", "POST"))
def contact():
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
            return render_template("contact.html", errors=[], name=name, email=email, subject=subject, message=message)

        flash("Thank you for your message")
        return redirect("/contact")
    return render_template("contact.html", errors=[], name="", email="", subject="", message="")
                    
if __name__ == "__main__":
    app.run(debug=True)

