import tweepy
from decouple import config

cliente = tweepy.Client(
    consumer_key=config('API_Key'),
    consumer_secret=config('API_Key_Secret'),
    access_token=config('Access_Token'),
    access_token_secret=config('Access_Token_Secret')
)



try:
    #postando Tweet pelo script
    response = cliente.create_tweet(text="My Fisrt Tweet for Bot !")
    print(response)
    # pesquisando por tweets recentes
    #query ='python'
    #tweet = cliente.search_recent_tweets(query=query,user_auth=True , max_results=100)
    #for i in tweet.data:    
    #    print(i.id , i.text)
        
    
    #retweet 
    #retweet = cliente.retweet(tweet_id=1587858741478785029,user_auth=True)
    #print(retweet)
    # curtindo tweet 
    # like = cliente.like(tweet_id=1587858741478785029, user_auth=True)

    # comentando tweet
    #response = cliente.create_tweet(in_reply_to_tweet_id=1587858741478785029,text='Hello')
    #print(response)

    # comentando tweets da pesquisa recente
    #query ='python'
    #tweet = cliente.search_recent_tweets(query=query,user_auth=True , max_result=100)
    #for i in tweet.data:    
    #    print(i.id , i.text)
    #    response = cliente.create_tweet(in_reply_to_tweet_id=i.id,text='Hello !')

    # Obtendo quantidade de Seguidores por usuario
    #for i in cliente.get_users_followers(id=1133209118511128576,user_auth=True):
    #    print(i)

    # Obtendo Id de usuario
    #cliente.get_users(usernames='vitim_gone', user_auth=True)

     
except tweepy.TweepyException as e:
    print(e)