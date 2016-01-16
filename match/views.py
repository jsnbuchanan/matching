import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

christina = {'name':'Christina',
                       'description':'sexy funny kitty wrangler',
                       'images':['img/profiles-samples/christina.jpg',
                                 'img/profiles-samples/gilmores.jpg',
                                 'img/profiles-samples/kitties.jpg']}

jason = {'name':'Jason','description':'robust healthy male',
         # 'images':['img/profiles-samples/jason-potion.jpg',
         #           'img/profiles-samples/jason-warlord.jpg',
         #           'img/profiles-samples/jason-butt.jpg']
         }

ian = {'name':'Ian','description':'wickedly smart beneficent mastermind',
       'images':['img/profiles-samples/ian-fire.jpg',
                 'img/profiles-samples/ian-frog.jpg',
                 'img/profiles-samples/ian-color.jpg',
                 'img/profiles-samples/ian-suckers.jpg']
      }
amy = {'name':'Amy','description':'amazon warrior princess',
       'images':['img/profiles-samples/amy-kiss.jpg',
                 'img/profiles-samples/amy-wifi.jpg',
                 'img/profiles-samples/amy-savanah.jpg']
      }

# Create your views here.


def home(request):
    return render(request, "match/search.html")


def profiles(request):
    return render(request, "match/profiles.html", {'profile':christina})


def profile(request):
    return render(request, "match/profile.html", {'profile':christina})


def results(request):
    match_profiles = {'profiles':[christina, ian, jason, amy]}

    for profile in match_profiles['profiles']:

        if 'images' not in profile.keys():

            profile['images'] = ['/static/img/profile.jpg']

            # the following is an example of logging
            logger.debug('The %s profile was assigned a generic thumbnail' % (profile['name']))

    return render(request, "match/results.html", match_profiles)

