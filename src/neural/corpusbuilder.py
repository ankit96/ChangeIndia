'''
1)builds a txt file of words from specific topic using tweepy

'''
__author__ = 'ankit'
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import cPickle
from nltk.tag import pos_tag


#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


api = tweepy.API(auth)

#print ethical('Justin Bieber top discussions in India.')
bribe = open("sports.txt", "w")

for tweet in tweepy.Cursor(api.search,
                           q="sports",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
                           	
    	try:
    		#print tweet.text
    		#if "park" in tweet.text.lower():
    			#print str(tweet.text)
    		
		bribe.write(str(tweet.text.lower()))
		bribe.write("\n")
    		"""	
		for a in tweet.text.lower().split():
			if '@' not in a and 'http' not in a:  
				bribe.write(str(a))
				bribe.write("\n")
		"""	
    	except UnicodeEncodeError:
		print ""   
		
bribe.close()

    	
