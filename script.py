from twitter import *

import urllib.request
import random

# read the credentials
credentials = {}
for line in open('.credentials'):
    if len(line.strip()) > 0:
        k,v = line.split("=")
        credentials[k] = v.strip()

oauth = credentials['OAUTH_CREDENTIALS']
secret = credentials['OAUTH_SECRET']
app_key = credentials['APP_KEY']
app_secret = credentials['APP_SECRET']
reply_to_id = credentials['REPLY_TWEET_ID']
reply_to_account = credentials['REPLY_TO_ACCOUNT']

tw = Twitter(auth=OAuth(oauth, secret, app_key, app_secret))

list_of_messages = []
for line in urllib.request.urlopen("https://pastebin.com/raw/mL1dXzuy"):
    list_of_messages.append(line.decode('utf-8').strip())

tweet = list_of_messages[random.randint(0, len(list_of_messages))].strip()
status = "@%s %s" % (reply_to_account, tweet)

# Somehow if this fail, just send an email or ping me so I can update the .credentials file
tw.statuses.update(status=status, in_reply_to_status_id=reply_to_id)

