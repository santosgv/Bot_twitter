import tweepy
from decouple import config

api = tweepy.Client(
    consumer_key=config('API_Key'),
    consumer_secret=config('API_Key_Secret'),
    access_token=config('Access_Token'),
    access_token_secret=config('Access_Token_Secret')
)

try:
    # postando Tweet pelo script
    tweet = api.create_tweet(text="My Second Tweet for Bot !")
    print(tweet)
except:
    print('Algo deu errado')