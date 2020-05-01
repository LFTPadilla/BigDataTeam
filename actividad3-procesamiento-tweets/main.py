import tweepy
import keys
from tweetutilities import print_tweets
import wordcloud
import matplotlib.pyplot as plt


def autenticarse():
    # Se crea y se configura OAuthHandler para autenticarse en Twitter
    auth = tweepy.OAuthHandler(keys.consumer_key,
                               keys.consumer_secret)
    
    auth.set_access_token(keys.access_token,
                          keys.access_token_secret)
    
    # Se configura el API
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
                 
    return api