from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
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
            return redirect('mysessions')
        else:
            form = UserSessionsForm(instance=queryset)
    template_name = 'userprograms/user-sessions.html'
    return render(request, template_name, {'form':form})