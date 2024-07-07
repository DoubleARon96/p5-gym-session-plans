from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import MainUserProgram, UserPrograme

def index(request):
    """
    view to show template
    """
    queryset = MainUserProgram.objects.all()
    content = queryset
    viewbag = {"contents": content}
        
    return render (request, "userprograms/index.html",viewbag)



def mysessions(request, id):
    """
    View to show template
    """
    session = get_object_or_404(MainUserProgram, id=id)  # i need to get the id to work
    usersessions_form = UserSessionsForm(request.POST or None)  

    if request.method == "POST":
        if usersessions_form.is_valid():
            user_program = usersessions_form.save(commit=False)  
            user_program.user = request.user  
            user_program.post = session
            user_program.save()
            messages.success(request, 'Comment Is Just Going To Be Checked')

    return render(request, "userprograms/index.html", {
        'main_program': session,
        'usersessions_form': usersessions_form,
    })
