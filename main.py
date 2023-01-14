import os
import json
import tweepy


def get_daily_quote():
    daily_quote = None

    with open("quotes.json", "r+") as file:
        quotes = json.load(file)
        daily_quote = quotes[0]["quote"]
        quotes.pop(0)
        file.seek(0)
        json.dump(quotes, file)
        file.truncate()

    return daily_quote


def get_authorized_api():
    # authenticate API request
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api


def post_tweet(api, tweet):
    api.update_status(tweet)


if __name__ == "__main__":
    # get data from environment variables
    API_KEY = os.getenv("TWITTER_API_KEY", "NOT FOUND")
    API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET", "NOT FOUND")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "NOT FOUND")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "NOT FOUND")

    quote = get_daily_quote()
    api = get_authorized_api()
    post_tweet(api, quote)
