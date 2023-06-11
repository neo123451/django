from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bio(request):

    return render(request, 'bio.html')

def campaign(request):

    return render(request, 'campaign.html')
def background(request):

    return render(request, 'background.html')
