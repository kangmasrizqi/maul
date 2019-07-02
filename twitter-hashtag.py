import tweepy
import csv
consumer_key = 'gg9H0EzMsJBlVt722STHwGxu7'
consumer_secret = 'N9cZsJBPThgIg66TD1SCGDFWqTValYkyMP9NffLOhKIGmZ2Ikf'
access_token = '979692300136677376-9nc3lgCJzZ1RnqjiF9ObeQRCDAfCma8'
access_token_secret = 's1tn2kJ7NxMM78Hs6LbOTwWPgPZo9H0gepAPKEQxvarwT'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('#AkutuOrangnya.csv', 'a')
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,q="#AkutuOrangnya",count=50,
                           lang="id",
                           since="2019-07-02").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
