import re
import tweepy
from textblob import TextBlob

consumer_key = "xveoNdJRrtopuc7SdgElUQI65"
consumer_secret = "qosFFtFiySQ0XOJ6zQFTyVkoJg2debzxgSxfzYZfoP0LVD0PWB"
access_token = "849232974310658048-4APVhRe5ZJGfjitbXU0qHYsdE1eeQHT"
access_token_secrt = "yuzEOyOTi6vKWkI79HDXzg1puL9mqQKXXLREtgD6crPw7"

def twitter_authentication():

	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secrt)
	api = tweepy.API(auth)

	public_tweets = api.search('messi10stats')
	count = 0;
	for tweet in  public_tweets:
		print(clean_tweet(tweet.text))
		analysis = TextBlob(clean_tweet(tweet.text))
		print(analysis.sentiment)
		print("---------------------------------------")

def clean_tweet(tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

twitter_authentication()