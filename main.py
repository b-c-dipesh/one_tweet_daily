import os
import json
import tweepy
import sqlite3

conn = sqlite3.connect('quotes.sqlite')
cur = conn.cursor()


def get_daily_quote():
    daily_quote = None

    cur.execute(
        "SELECT * from Quotes WHERE is_posted = 0 LIMIT 1")
    daily_quote = cur.fetchone()

    return daily_quote


def get_authorized_api():
    # authenticate API request
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api


def post_tweet(api, tweet):
    api.update_status(tweet[1])
    cur.execute("UPDATE Quotes SET is_posted = 1 WHERE id = ?", (tweet[0],))


if __name__ == "__main__":
    # get data from environment variables
    API_KEY = os.getenv("TWITTER_API_KEY", "NOT FOUND")
    API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET", "NOT FOUND")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "NOT FOUND")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "NOT FOUND")

    # Uncomment these lines if you are running this app for the first time

    # cur.execute('''CREATE TABLE IF NOT EXISTS Quotes (
    # "id" INTEGER NOT NULL UNIQUE,
    # "quote" TEXT NOT NULL UNIQUE,
    # "is_posted" NUMERIC NOT NULL DEFAULT 0,
    # PRIMARY KEY ("id" AUTOINCREMENT))''')

    # with open("quotes.json") as file:
    #     quotes = json.load(file)

    # for entry in quotes:
    #     cur.execute("INSERT INTO Quotes (quote) VALUES (?)", (entry['quote'],))
    # conn.commit()

    quote = get_daily_quote()
    api = get_authorized_api()
    post_tweet(api, quote)

    conn.commit()
    cur.close()
