from .forms import StatusForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
import tweepy
import requests.packages.urllib3
from django.http import HttpResponse
requests.packages.urllib3.disable_warnings()


def twitterAuthenticate(request):
    consumer_key = 'u2q9wRYm39FNfO5pRAW5TRC5I'
    consumer_secret = '3laxjeOWk95UjI3bkjR6PIWLJZI6J1KyetIV2z0BvUDJ8xfqq3'
    access_token = ''
    access_token_secret= ''
    session = {}
    callback_url = 'www.twitter.com'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret,'callback_url')
    try:
        redirect_url = auth.get_authorization_url()
        session['request_token'] = auth.request_token
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'
    # request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)
    verifier = request.GET.get('oauth_verifier')

    
    auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret,''callback_url')

    token = request.session.get('request_token')
    request.session.delete('request_token')
    # auth.set_request_token(token[0], token[1])
    auth.request_token = session.get('request_token')

    # try:
    #     token = auth.get_access_token(verifier)
    # except tweepy.TweepError:
    #     return HttpResponse('error', status=500)
    verifier = request.GET.get('oauth_verifier')
    auth.get_access_token(verifier)

    response_data = {}
    response_data['key'] = auth.access_token.key
    response_data['secret'] = auth.access_token.secret

    response = 'you are now authenticated'
    api = tweepy.API(auth)
    api.update_status('tweepy + oauth!')
    return HttpResponse(response)


def twitterAuthorizeCallback(request):
    verifier = request.GET.get('oauth_verifier')

    auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret')

    token = request.session.get('request_token')
    request.session.delete('request_token')
    auth.set_request_token(token[0], token[1])

    try:
        token = auth.get_access_token(verifier)
    except tweepy.TweepError:
        return HttpResponse('error', status=500)

    # response_data = {}
    # response_data['key'] = auth.access_token.key
    # response_data['secret'] = auth.access_token.secret
    session ={}
    session['token'] = (auth.access_token, auth.access_token_secret)
    # auth.set_access_token(access_token, access_token_secret)
    token, token_secret = session['token']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(token, token_secret)

    response = 'you are now authenticated'
    api = tweepy.API(auth)
    api.update_status('tweepy + oauth!')
    return HttpResponse(response)



