'''
twitter bot to check for new tweets from Adam Dunn 
and retweet the newest one that we have not yet tweeted
'''

# THIS DOESN'T WORK YET

import time
import twitter
import pandas as pd 
import numpy as np

# my private app credentials in a file called credentials.py
from credentials import *

adamdunn = 'adamdunn_44'

api = twitter.Api(consumer_key,consumer_secret,access_token_key,access_token_secret)

while True:
    try:
        api.PostRetweet(api.GetUserTimeline(screen_name=adamdunn)[0])
        time.sleep(86400)
    except:
        pass
