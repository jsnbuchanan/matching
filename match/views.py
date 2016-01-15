from django.shortcuts import render
from django.http import HttpResponse

christina = {'name':'Christina',
                       'description':'sexy funny kitty wrangler',
                       'images':['img/profile-samples/christina.jpg',
                                 'img/profile-samples/gilmores.jpg',
                                 'img/profile-samples/kitties.jpg']}

jason = {'name':'Jason','description':'robust healthy male'}
ian = {'name':'Ian','description':'wickedly smart beneficent mastermind'}
amy = {'name':'Amy','description':'amazon warrior princess'}

# Create your views here.
def home(request):
    return render(request, "match/search.html")

def profile(request):
    return render(request, "match/profile.html", {'profile':christina})

def results(request):
    return render(request, "match/results.html", {'profiles':[christina, ian, jason, amy]});

