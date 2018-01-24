#!/usr/bin/python
from secrets import *
import random
import tweepy
                
# twitter setup
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)
#tweet='I made it.'
#api.update_status(tweet)

filename = open ('/users/douglassmith/desktop/stephenbot/depressed.txt', 'r')
tweettext = filename.readlines()
randomChoice = random.randrange(len(tweettext))
print (tweettext[randomChoice])
api.update_status(status=tweettext[randomChoice])
#0	*/5 *	*	*	. /etc/profile: python /Users/douglassmith/desktop/stephenbot/bot.py
