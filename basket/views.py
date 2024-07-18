from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from ptsessions.models import PtSessions
#from .models import 
#from .forms import 

# Create your views here.
def Basket (request):
    
    #items = request.session.get('basket',{})
    template = 'basket/index.html'
    #content = { }
    return render(request, template)