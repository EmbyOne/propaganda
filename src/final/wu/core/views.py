from django.shortcuts import render, redirect
from django.http import request, HttpResponse, Http404, FileResponse
from core.forms import messageForm
import tweepy
from django.conf import settings

# basic filter, change later TODO
profanity = 'shit' # this is bad bad first and we must filter it out !!!!!!!!

# Twitter client setup, keys taken from environemnt variables
client = tweepy.Client(
    consumer_key=settings.CONSUMER_KEY, consumer_secret=settings.CONSUMER_SECRET,
    access_token=settings.ACCESS_TOKEN, access_token_secret=settings.ACCESS_TOKEN_SECRET
)


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = messageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            result = form.instance

            # Error handling stuff for the future
            error = None
            if profanity in result.message:
                error = 'no profanity pls we are pg'
            if 123 == 121:
                error = 'what the fuck happened here'
            if error:
                return render(request, 'main.html', {'form': form, 'result': result, 'error': error})


            # do the twitter shit
            # uuga buuga
            response = client.create_tweet(text=result.message)

            # The url for the tweet
            url = f"https://twitter.com/user/status/{response.data['id']}"
            
            return render(request, 'main.html', {'form': form, 'url': url})

    # if GET (or any other method) is used, return the base site
    else:
        form = messageForm()

    return render(request, 'main.html', {'form': form})


    