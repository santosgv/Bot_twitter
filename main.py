from distutils.command.config import config
import tweepy
from decouple import config

auth = tweepy.OAuth1UserHandler(
    config('API_Key'),config('API_Key_Secret'),config('Bearer_Token')
    )


api = tweepy.API(auth)

print(api.verify_credentials().screen_name)