import tweepy
from tweepy.auth import OAuthHandler
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

db = pd.DataFrame()

def printTweet(n, ith_tweet):
    print(f"Tweet {n}: \n")
    print(f"Usuario: {ith_tweet[0]}")
    print(f"Descripcion: {ith_tweet[1]}")
    print(f"Ubicacion: {ith_tweet[2]}")
    print(f"Siguiendo: {ith_tweet[3]}")
    print(f"Seguidores: {ith_tweet[4]}")
    print(f"Total Tweets: {ith_tweet[5]}")
    print(f"Numero de Retweets: {ith_tweet[6]}")
    print(f"Texto del tweet: {ith_tweet[7]}")
    print(f"Hashtags usados: {ith_tweet[8]} \n")

def scrape(words, date_since, numtweet):
    # Creacion del Dataframe que tendra la informacion de cada Tweet
    global db
    db = pd.DataFrame(columns=['username',
                               'description',
                               'location',
                               'following',
                               'followers',
                               'totaltweets',
                               'retweetcount',
                               'text',
                               'hashtags'])
    
    # Uso de Tweepy para atraer los tweets
    tweets  = tweepy.Cursor(api.search_tweets,
                            words, lang="en",
                            since_id=date_since,
                            tweet_mode='extended').items(numtweet)
    
    # Crear lista con cada tweet para iterar sobre cada uno y guardar su respectiva info
    list_tweets = [tweet for tweet in tweets]
    i = 1

    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try:
            text = tweet.retweeted_status.full_Text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0,len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        ith_tweet = [username,description,location, following, followers, totaltweets, retweetcount, text, hashtext]

        db.loc[len(db)] = ith_tweet
        #printTweet(i, ith_tweet)
        i = i+1

    return db

# Autenticacion para el uso de la API de Twitter
auth = OAuthHandler(os.environ["apiKey"], os.environ["apiKeySecret"])
auth.set_access_token(os.environ["accessToken"], os.environ["accessTokenSecret"])

api = tweepy.API(auth)

