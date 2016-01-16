from django.shortcuts import render
from django.http import HttpResponse

christina = {'name':'Christina',
                       'description':'sexy funny kitty wrangler',
                       'images':['img/profiles-samples/christina.jpg',
                                 'img/profiles-samples/gilmores.jpg',
                                 'img/profiles-samples/kitties.jpg']}

jason = {'name':'Jason','description':'robust healthy male'}
ian = {'name':'Ian','description':'wickedly smart beneficent mastermind'}
amy = {'name':'Amy','description':'amazon warrior princess'}

# Create your views here.
def home(request):
    return render(request, "match/search.html")

def profiles(request):
    return render(request, "match/profiles.html", {'profile':christina})

def profile(request):
    return render(request, "match/profile.html", {'profile':christina})

def results(request):
    return render(request, "match/results.html", {'profiles':[christina, ian, jason, amy]});

