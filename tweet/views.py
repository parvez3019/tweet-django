from .forms import StatusForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
import tweepy
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()




# def twitterAuthenticate(request):
# 	consumer_key = 'u2q9wRYm39FNfO5pRAW5TRC5I'
# 	consumer_secret = '3laxjeOWk95UjI3bkjR6PIWLJZI6J1KyetIV2z0BvUDJ8xfqq3'
# 	access_token = ''
# 	access_token_secret= ''
# 	session = {}
# 	callback_url = '/'
#     auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret', 'callback_url')

#     try:
#         redirect_url = auth.get_authorization_url()
#     except tweepy.TweepError:
#         return HttpResponse('error', status=500)

#     request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)

#     return HttpResponseRedirect(redirect_url)

# def twitterAuthorizeCallback(request):
#     verifier = request.GET.get('oauth_verifier')

#     auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret')

#     token = request.session.get('request_token')
#     request.session.delete('request_token')
#     auth.set_request_token(token[0], token[1])

#     try:
#         token = auth.get_access_token(verifier)
#     except tweepy.TweepError:
#         return HttpResponse('error', status=500)

#     response_data = {}
#     response_data['key'] = auth.access_token.key
#     response_data['secret'] = auth.access_token.secret

#     response = 'you are now authenticated'

#     return HttpResponse(response)





def home(request):
	form=StatusForm(request.POST or None)
	if request.method=="POST":
				
		print "scirpt"

		consumer_key = 'u2q9wRYm39FNfO5pRAW5TRC5I'
		consumer_secret = '3laxjeOWk95UjI3bkjR6PIWLJZI6J1KyetIV2z0BvUDJ8xfqq3'
		access_token = ''
		access_token_secret= ''
		session = {}
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		try:
			redirect_url = auth.get_authorization_url()
		except tweepy.TweepError:
		    return HttpResponse('error', status=500)

		request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)


		# request_token = session['request_token']
		# del session['request_token']

		# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		# auth.request_token = request_token
		# verifier = request.GET.get('oauth_verifier')
		# auth.get_access_token(verifier)
		# session['token'] = (auth.access_token, auth.access_token_secret)



		# # auth.set_access_token(access_token, access_token_secret)
		# token, token_secret = session['token']
		# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		# auth.set_access_token(token, token_secret)
		# # api = tweepy.API(auth)



		verifier = request.GET.get('oauth_verifier')
		auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret')
		token = request.session.get('request_token')
		request.session.delete('request_token')
		auth.set_request_token(token[0], token[1])

		try:
		    token = auth.get_access_token(verifier)
		except tweepy.TweepError:
			return HttpResponse('error', status=500)

		response_data = {}
		response_data['key'] = auth.access_token.key
		response_data['secret'] = auth.access_token.secret  
        response = 'you are now authenticated'
        api = tweepy.API(auth)
        api.update_status('tweepy + oauth!')
        print 'done'
        return render(request,"home.html")
    
    