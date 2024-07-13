from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import MainUserProgram, UserPrograme
from .forms import UserSessionsForm, MainUserProgramForm

def index(request):
    """
    view to show template
    """
    queryset = MainUserProgram.objects.all()
    mainsessions_form = MainUserProgramForm(request.POST or None)  
    content = queryset
    title = "My Sessions"

    if request.method == "POST":
        if mainsessions_form.is_valid():
            user_session = mainsessions_form.save(commit=False)  
            user_session.user = request.user  
            user_session.post = content
            user_session.save()
            mainsessions_form = MainUserProgramForm()

    viewbag = {"contents": content,
               "title" : title,
               'mainsessions_form':mainsessions_form}
        
    return render (request, "userprograms/index.html",viewbag)



def mysessions(request, id):
    """
    View to show template
    """
    session = get_object_or_404(MainUserProgram, id = id)
    mysessions = UserPrograme.objects.filter(session = id)
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
    queryset =  get_object_or_404 (UserPrograme, id=id)
    form = UserSessionsForm(instance=queryset)
    if request.method == 'POST':
        form = UserSessionsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('userprograms')
        else:
            form = UserSessionsForm(instance=queryset)
    template_name = 'userprograms/user-sessions-update.html'
    return render(request, template_name, {'form':form})



#def deleteView(request, exercise_id, mainuserprogram_id):
#    main_program = get_object_or_404(MainUserProgram, id=mainuserprogram_id)
#    exercise = get_object_or_404(UserPrograme, id=exercise_id)
#    if request.method == 'POST':
#        exercise_id.delete()
#        messages.success(request, 'Exercise deleted!')
#    else:
#        messages.error(request, "Exercise couldn't be deleted!")
    
#    return HttpResponseRedirect(reverse('mysessions', args=[mainuserprogram_id]))

def deleteView(request, id):
    queryset =  get_object_or_404 (UserPrograme, id=id)
    if request.method == 'GET':
        queryset.delete()
        return redirect('userprograms')
    else:
         messages.error(request, "Exercise couldn't be deleted!")
    
    return render (request, "userprograms/delete-failed.html")

def mainDeleteView(request, id):
    queryset =  get_object_or_404 (MainUserProgram, id=id)
    if request.method == 'GET':
        queryset.delete()
        return redirect('userprograms')
    else:
         messages.error(request, "Exercise couldn't be deleted!")
    
    return render (request, "userprograms/delete-failed.html")
