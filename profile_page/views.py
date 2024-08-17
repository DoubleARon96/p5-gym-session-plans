from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from ptsessions.models import PtSessions
from userprograms.models import MainUserProgram

# Create your views here.


@login_required
def index(request):
    title = "Profile Page"
    try:
        profile = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        profile = None

    
    sessions = PtSessions.objects.filter(client=request.user)
    user_sessions = MainUserProgram.objects.filter(user=request.user)
    sessions_count = user_sessions.count

    if not sessions.exists():
        messages.warning(request, 'You have no Sessions')

    context = {
        'profile': profile,
        'sessions': sessions,
        'user_sessions': user_sessions,
        'title': title,
        'client_sessions': request.user.username,
        'sessions_count' : sessions_count
    }
    return render(request, "profile_page/index.html", context)