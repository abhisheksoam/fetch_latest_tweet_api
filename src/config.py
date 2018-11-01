__author__ = 'abhishek'

# Twitter credential

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

consumer_key = '8U7d6zD7kq4Gnk8k6PFSW8quh'
consumer_secret = 'JeuTPEZPMw0Qpzrczr7VlXKrkMPGwvuVgPXI30i4LiF4Mp4zK3'
access_token = '2460953959-S5HiLFWbLMM5GJrmEEWR2FvF79Mxz2H1RqKwYBF'
access_token_secret = 'OfKnswsWi6qW8poipQMdaqFTdpTod6QmQReQCHpGQCa16'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)



# get_all_tweets('narendramodi')

# get_user_tweets('abhisheksoamraj')
