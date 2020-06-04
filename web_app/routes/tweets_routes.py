# web_app/routes/tweets_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from web_app.models import db, Tweet, parse_records


tweets_routes = Blueprint("tweets_routes", __name__)

@tweets_routes.route("/tweets")
def list_tweets():
    tweets_records = Tweet.query.all()
    print(tweets_records)
    tweets = parse_records(tweets_records)
    return render_template("tweets.html", message="Here are the Tweets", tweets=tweets)

@tweets_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweets_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    
    new_tweet = Tweet(tweet=request.form['tweet'], user_id=request.form["user_id"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })