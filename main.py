import os
import tweepy


def get_authorized_api():
    # authenticate API request
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api


def post_tweet(api):
    api.update_status("Hello World!2")


if __name__ == "__main__":
    # Get data from environment variables
    API_KEY = os.getenv("TWITTER_API_KEY", "NOT FOUND")
    API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET", "NOT FOUND")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "NOT FOUND")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "NOT FOUND")

    api = get_authorized_api()
    post_tweet(api)
