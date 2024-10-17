from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import MainUserProgram, UserProgram
from .forms import UserSessionsForm, MainUserProgramForm


@login_required
def index(request):
    """
    view to show template
    """
    queryset = MainUserProgram.objects.all()
    mainsessions_form = MainUserProgramForm(request.POST or None)
    content = queryset
    maker_user = MainUserProgram.user
    title = "My Sessions"

    if request.method == "POST":
        if mainsessions_form.is_valid():
            user_session = mainsessions_form.save(commit=False)
            user_session.user = request.user
            user_session.post = content
            user_session.save()
            messages.success(request, "Session Was Successfully Made !")
            mainsessions_form = MainUserProgramForm()

    viewbag = {"contents": content,
               "title": title,
               "maker_user": maker_user,
               'mainsessions_form': mainsessions_form}

    return render(request, "userprograms/index.html", viewbag)

@login_required
def mysessions(request, id):
    """
    View to show template
    """
    session = get_object_or_404(MainUserProgram, id=id)
    mysessions = UserProgram.objects.filter(session_id=id)
    usersessions_form = UserSessionsForm(request.POST or None)
    title = session.session_name

    if request.method == "POST":
        if usersessions_form.is_valid():
            user_program = usersessions_form.save(commit=False)
            user_program.user = request.user
            user_program.session = session
            user_program.save()
            messages.success(request, "Exercise Was Successfully Made !")
            usersessions_form = UserSessionsForm()

    content = {'main_program': session,
               "usersessions_form": usersessions_form,
               "title": title,
               "mysessions": mysessions, }

    return render(request, "userprograms/user-sessions.html", content)

@login_required
def updateView(request, id):
    queryset = get_object_or_404(UserProgram, id=id)
    form = UserSessionsForm(instance=queryset)
    if request.method == 'POST':
        form = UserSessionsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Exercise Was Updated Successfully !")
            return redirect('userprograms')
        else:
            form = UserSessionsForm(instance=queryset)
            messages.error(request, "Exercise Was Not Updated !")
    template_name = 'userprograms/user-sessions-update.html'
    return render(request, template_name, {'form': form})

@login_required
def deleteView(request, id, session_id):
    queryset = MainUserProgram.objects.all()
    main_program = get_object_or_404(queryset, id=id)
    exercise = get_object_or_404(UserProgram, pk=session_id)
    if request.method == 'POST':
        exercise.delete()
        messages.success(request, "Exercise Was Deleted Successfully !")
        return HttpResponseRedirect(reverse('mysessions', args=[id]))
    else:
        messages.error(request, "Exercise couldn't be deleted!")

    return render(request, "userprograms/delete-failed.html")

@login_required
def mainDeleteView(request, id):
    queryset = get_object_or_404(MainUserProgram, id=id)
    if request.method == 'GET':
        queryset.delete()
        messages.success(request, "Exercise was deleted!")
        return redirect('userprograms')
    else:
        messages.error(request, "Exercise couldn't be deleted!")

    return render(request, "userprograms/delete-failed.html")
