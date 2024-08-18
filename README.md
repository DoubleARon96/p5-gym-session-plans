
Welcome Aaron storey,
# Home Page

### Brief description
the home page is aimed to welcome new people to the app/site so they understand what we as the developers can provide the user.

### Plans
![home page plan ](docs/readme-images/home-page-plan.jpg)
![image of data plan ](docs/readme-images/home-data-plan.png)

### Thoughts 
this is a basic model i set up thinking that it would be nice to be able to edit for super users but i thought if i keep it to only one and make it so only devs and the client can change.

i also made it so its crud function is only to be updated so its easy to track and make sure not to much writing is on the home.

# issues
1. the first issue i has was getting the static files to work on the deployed version. 
is would have the bootstrap styles but no css, js or media I had made. 
* Solution
I forgot to download and set up whitenoise to the middle ware   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
#   'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

2. update / edit the new story
*  I had an issue with getting the news story to upadate so i had to do some research and the problem was i had the urls set up wrong so it was using the wrong views function

>Urls.py
path('sv/', views.showView, name='show_url'),

>views.py

def updateView(request, ids):
    queryset =  get_object_or_404 (HomeNews, id=ids)
    form = NewsForm(instance=queryset)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
#            return redirect('home')
        else:
            form = NewsForm(instance=queryset)
    template_name = 'home/crud.html'
    return render(request, template_name, {'form':form})

instead of having the redirect to home it was using the show View one and this confused me going through and wondering why the form didn't appear

# User Sessions
### js issues
this issues has been the hardest one so far the image below shows the debugging i was using the console logs where my best friend.
![js-issue](docs/readme-images/js-issue-on-html.png)
I realised the for loop wasn't correct on the html.
![wrong-loop](docs/readme-images/right-loop.png)
this is the change i had to do to make sure it worked 
![correct-loop](docs/readme-images/right-loop.png)
this shows that it wasn't collecting the delete number to add to the url.
![url-issue](docs/readme-images/url-issue.png)

### Brief description
the aim for this page was so that customers can make up there own sessions and record what they have done.

### Plans
![usersession page plan ]()
![image of data plan ](docs/readme-images/session-data-plan.png)

### Thoughts 
when making this i spent a long time trying to get the crud function to work on the exercise part because the urls and the java script just weren't working together well but its a great learning curve and will increase my skills by a lot.
### Test
The Tests i did manually : 
1. add new program
![Adding New Program](docs/readme-images/adding-session.png)
Session Added
![program added](docs/readme-images/session-added.png)
2. View Full Session
this view shows that the link on the session open up to the exercise page
![exercise View](docs/readme-images/view-in-session.png)
3. add Exercises 
This image shows the form to add a program to the exercise page 
![Adding Session](docs/readme-images/adding-session.png)
4. Edit Session
this shows the editing form for the exercise and auto fills with the old information.
![edit form](docs/readme-images/editing-exercise.png)
this shows that after editing it dose update the exercise.
![edited exercise](docs/readme-images/exercise-edited.png)
5. Delete Exercise
![]()


# Pt sessions
### Brief description
This app is for the Pts/admins so they can sell their training sessions and maintain the updates for the clients so they will always have new sessions and learn new ways to try all the time.
### issues
![wrong syntax](docs/readme-images/add-to-basket-wrong.png)
when trying to debug i couldn't understand why it wasn't adding anything but!!!
![correct syntax](docs/readme-images/adding-to-basket-correct.png)
then i was reviewing the walkthrough i saw they have the "+= 1" and thought, that makes sense how can you add nothing to nothing and then boom it worked.
### Testing
The Tests i did where 
1. Add Item To Basket
2. Test Link to the full Session Page

# Basket
### Brief description
this app is designed to be for all clients looking to by any sessions the PT/Admins make. it also only keeps the clients items when they keep the page open.
### issues
### Testing

# Payments
### Brief description
this app is to help integrate stripe and make it easier for the users to know exactly what items they are buying 
### issues
### Testing

### Key Words

## main subjects

* Gym Sessions
![gym-session-search](docs/readme-images/key-word-search-gym-sessions.png)

* Programs 
![programs search](docs/readme-images/key-word-search-programs.png)

* Training
![rival app](docs/readme-images/key-word-search-rival-app.png)

## Short Tail Key Words:
~ Fitness ~
Training 
~ Muscles ~
Exercises
Personal Training
~ Chest ~
~ Back ~
~ Legs ~
~ Biceps ~
~ Triceps ~
~ Full Body ~
Hit Training
Health
Goals
Sessions
weight loss
cutting weight
~ lose weight ~
~gym~ 

Long tail Key Words:

~Personal Training Sessions~
Custom-made sessions and free recording of sessions
many Different styles of training e.g Hit, Full Body and Steady State
Sessions for any needs or goals 
~buy personal training sessions~
record my gym program



## All Key Words That Will Be On The Site:

Custom-made sessions and free recording of sessions
many Different styles of training e.g Hit, Full Body and Steady State
Sessions for any needs or goals 
Record My Gym Program
Hit Training
Health
Goals
Sessions
weight loss
cutting weight
Exercises
Personal Training

# Facebook Page

![facebook-header](docs/readme-images/facebook-header.png)
![facebook-main](docs/readme-images/facebook-page.png)

### Why Use Facebook

Facebook is an amazing site to get free and paid avertisement. Facebook also has great instagram integration so you can boost on face book as well as instagram,whats app and share links on other social media site.

# Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku tool belt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

## Testing And Validation 
[Link To Testing](MANUAL_TESTS.md)