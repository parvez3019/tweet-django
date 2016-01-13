import tweepy

#Authentication and token 

print "scirpt"

consumer_key = 'u2q9wRYm39FNfO5pRAW5TRC5I'
consumer_secret = '3laxjeOWk95UjI3bkjR6PIWLJZI6J1KyetIV2z0BvUDJ8xfqq3'
access_token = ''
access_token_secret= ''
session = {}

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
except tweepy.TweepError:
    print 'Error! Failed to get request token.'


request_token = session['request_token']
del session['request_token']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.request_token = request_token
verifier = request.GET.get('oauth_verifier')
auth.get_access_token(verifier)
session['token'] = (auth.access_token, auth.access_token_secret)



# auth.set_access_token(access_token, access_token_secret)
token, token_secret = session['token']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
# api = tweepy.API(auth)




#Post Tweet 

api = tweepy.API(auth)

api.update_status('tweepy + oauth!')