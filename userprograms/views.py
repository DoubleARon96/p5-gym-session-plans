from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import MainUserProgram, UserPrograme
from .forms import UserSessionsForm

def index(request):
    """
    view to show template
    """
    queryset = MainUserProgram.objects.all()
    content = queryset
    title = "My Sessions"
    viewbag = {"contents": content,
               "title" : title}
        
    return render (request, "userprograms/index.html",viewbag)



def mysessions(request, id):
    """
    View to show template
    """
    session = get_object_or_404(MainUserProgram, id = id)
    mysessions = UserPrograme.objects.all()
    usersessions_form = UserSessionsForm(request.POST or None)  
    title = session.session_name
    
    if request.method == "POST":
        if usersessions_form.is_valid():
            user_program = usersessions_form.save(commit=False)  
            user_program.user = request.user  
            user_program.post = session
            user_program.save()
            usersessions_form = UserSessionsForm()
            

    return render(request, "userprograms/user-sessions.html", {
        'main_program': session,
        'usersessions_form': usersessions_form,
        "title" : title,
        "mysessions" :mysessions
    })


def updateView(request, id):
    queryset =  get_object_or_404 (MainUserProgram, id=id)
    form = UserSessionsForm(instance=queryset)
    if request.method == 'POST':
        form = UserSessionsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('userprograms')
        else:
            form = UserSessionsForm(instance = queryset)
    template_name = 'userprograms/user-sessions-upadate.html'
    return render(request, template_name,{'form':form})


def deleteView(request, id):
    queryset = get_object_or_404(MainUserProgram, id=id)
    form = UserSessionsForm(instance=queryset)
    
    if request.method == 'POST':
        form = UserSessionsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.delete()
            messages.success(request, 'Exercise deleted!')
        else:
            messages.error(request, "Exercise couldn't be deleted!")

    # Redirect back to the same page with the correct ID
    return HttpResponseRedirect(reverse('mysessions', id=id))
