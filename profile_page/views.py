from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ptsessions.models import PtSessions

# Create your views here.


@login_required
def index(request):
    try:
        profile = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        profile = None

    context = {'profile': profile}
    return render(request, "profile_page/index.html", context)
