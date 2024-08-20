# Tests

## Manuel Testing

## HTML Validation

### Home Page
![home page view](docs/validation-images/home-page.png)
![home page validation](docs/validation-images/home-page-validation.png)
The only issue I had was the welcome message on the home page it was putting an extra P element 

### Basket Page
![basket page](docs/validation-images/basket-page.png)
![basket validation](docs/validation-images/basket-validation.png)
No issues where found only a couple of warnings

## Sign Up Page
![sign up page](docs/validation-images/sign-out-page.png)
![no errors but dose not work page](docs/validation-images/passes-validation-dose-not-work.png)
![error but working page](docs/validation-images/errors-for-signup-valdidation.png)

the issues with page come from generated code from alluth/Django. 
1. unordered list in a span element is not allowed but generates as one 
2. A P element is not connecting to the other 

## PT Sessions
![Main PT sessions](docs/validation-images/pt-session-page.png)
![Main PT Validation](docs/validation-images/pt-session-validation.png)
I had no issues with this only a couple of warnings.
![Single PT session](docs/validation-images/pt-session-page-view.png)
![Single PT session](docs/validation-images/pt-session-page-view.png)
I had no issues with this only a couple of warnings.

## User Sessions
![user sessions  main view](docs/validation-images/user-programs-main-page.png)
![user validation](docs/validation-images/user-main-validation.png)
I had no issues with this only a couple of warnings.
![exercises page](docs/validation-images/user-exercise-page.png)
![exercise page Validation](docs/validation-images/user-exercise-validation.png)

## Profile Page
![profile page](docs/validation-images/profile-page.png)
![profile page Validation](docs/validation-images/profile-page-validation.png)

## Payment Page
![payment page](docs/validation-images/payment-page.png)
![payment validation](docs/validation-images/payment-validation.png)
## CSS Validation

### styles .css
![styles css](docs/validation-images/styles-css.png)
only had two errors at first one was object-fit:fit instead of contain.
the other one was I put sold instead of solid on a border.

### Custom Admin
![admin css](docs/validation-images/admin-css.png)
Only found one issue and that was I tried to set a colour as none. so i deleted it 

## Java Script Validation

### Delete Exercise JS
![delete exercise](docs/validation-images/delete-exercise-validation.png)
### Delete Item JS
![delete item](docs/validation-images/delete-item-validation.png)
### Delete Main Exercise JS
![delete main exercise](docs/validation-images/delete-main-exercise-validation.png)
### Stripe Element JS
![stripe element](docs/validation-images/stripe-elements-validation.png)

## Python Validation
When doing the validations I made sure to take screen shots of a few for examples.
with all files except django generated ones, I also made sure they all conform to to Pep8 rules.
![home page view first test](docs/validation-images/python-validation/home-page-first-test.png)
this is an example of what issues you will come across when doing Python validation with pep8 rules.
![home page view passed](docs/validation-images/python-validation/home-validaion-pass.png)
Here is the an example of a corrected version of the page.
![basket context validation](docs/validation-images/python-validation/basket-context-file-validation.png)
Basket context file
![home page form validation](docs/validation-images/python-validation/home-form-validation.png)
Home page form file
![payment form validation](docs/validation-images/python-validation/payment-form-validation.png)
Payment form file 
![user program validation](docs/validation-images/python-validation/user-program-validation.png)
user program file
![basket validation](docs/validation-images/python-validation/views-file-basket-validation.png)
Basket view  file

# Light Room
I ran a light room test because its a good way to test the website in multiply ways in one test.

* Performance – Based on how fast the website loads and contributes to the overall UX.
* Accessibility – Based on how easy it is to use the website regardless if people might use a screen reader, etc.
* Best Practices – Based on the best practices used in industry.
* SEO Performance – Based on how useful the meta tags and labels are throughout the website.
![Light Room Test](docs/test-images/light-room.png)

# Manuel Testing
The testing methods I did were pretending to be a customer and using the app as a staff member to.
this involves going through all the links and pages making programs and deleting them also making orders and making sure they are accessible by the client when brought.

I also sent a live version to a few friends to test it out and give reviews on it.

## Home
There is only two features to test on this page 
1. super users are the only ones that can see the update button
2. the update button takes you to a page that lets you update
### Update Button Test
![super user home page](docs/test-images/super-user-home.png)
Non super user view
![non super user view](docs/test-images/non-super-user-view.png)
### Updating The Message
![super user home page](docs/test-images/super-user-home.png)
The button is visible in super user mode.
![title test update](docs/test-images/updating-title.png)
Link on the button dose take you to the update page and allows you to added and take away text.
![updated version](docs/test-images/updating-title.png)
Pressed the update button takes you back to home page and has updated text.
## Payments Tests
Payment test involves making sure all the buttons and links go to the right page, all forms are fill able and will let the user continue on to the payment and then check that the payment goes through the stripe payment system correctly.
1. ![fill out form](docs/readme-images/payment-view.png)
when doing this I tested to see if they are all required.
if the email can be skipped by not adding the @ and it stops you.
![email check](docs/test-images/email-test.png)
2. ![Enter Card Details](docs/test-images/entering-card-number.png)
this checks if the card is valid and has a build in save function.
if you don't put in the right number it will say and give a red warning.
3. ![Submit the payment](docs/test-images/submit.png)
this redirects you to a success page or if it fails it will have a warning pop up on the screen.
4. ![Check stripe](docs/readme-images/succesful-payment-intent.png)
this is were i checked if the webhooks were working and if the card is failing.
5. ![final stage](docs/test-images/order-number-succes-page.png)
if everything goes well you will reach this page.

## User Sessions
The user Sessions Tests I will Be doing
1. Making sure the link to the page works
2. make sure page displays 
3. make sure the user can make a session 
4. if you can make a session the next will be can you use the link to get to the adding exercise page 
5. when on the adding exercise page i will test if you can add new exercises , update them and delete them.
### Making Session & Deleting Test
the testing of the sessions was easy because it was only create and delete so only two buttons
* testing the create scroll down and fill in the form and then press the add new button and an alert will show saying it was created and it will show on the page.

* testing the delete click the delete button and then you will get a warning saying are you sure and when you click the delete, it deleted the session and an alert will show.
![making session form](docs/test-images/making-session-form.png)
![new session made ](docs/test-images/session-made.png)
![delete session test](docs/test-images/test-delete.png)
![delete session test alert](docs/test-images/delete-session-alert.png)

### Making Exercise , Delete & Update
#### Making A New Exercise
The Tests I did to make sure that Crud functionality is working in this part I also tested to make sure
the alerts were working with every test
![exercise view](docs/test-images/exercise-page-view.png)
The link to the page works and the page displays fully
![making new exercise](docs/test-images/making-new-exercise.png)
next step was to check if i could add a new exercise so i scrolled down to the form.
![exercise added](docs/test-images/new-exercise-added.png)
the last step was click the button make and then you will get an alert and then the new exercise was made.
#### Updating
when testing the update function I looked out for alerts and if it was successful 
![updating session test](docs/test-images/testing-update-exercise.png)
first I clicked the update button and then it took me to the update page and changed a few things to 
check if the texts can be changed
![update successful](docs/test-images/update-exercise-alert.png)
the final step is click the update button and then it shows an alert. the new exercise appeared as a table on the grid.
#### Deleting
testing the delete button was the easiest because all i had to do is click and see what happens.
![testing Delete](docs/test-images/testing-exercise-delete.png)
first step click on the delete button.
![delete success](docs/test-images/delete-test-success.png)
no warning shows but an alert shows up and the exercise is deleted.

## PT Sessions
Testing the Pt session includes
1. making sure the admin button appears only for super users
2. items can be brought by users logged in
3. when on the super user page they only have access to the pt sessions
4. final but big test is to check that i can create a pt session and it appear on the pt session page.
### Staff/Personal Trainers options
![staff view](docs/readme-images/staff-view.png)
the Staff/Personal Trainers will all have access to a restricted version of the admin page.
![client view](docs/readme-images/client-view.png)
this shows that the admin button is not showing means that it has passed this test.
### Staff/Personal Trainer Page
the styles on this page is very basic because the customers wont be able to view it so all it needs to be is functional and thats what this image blow shows:
![staff page for pt's](docs/readme-images/admin-pt-page.png)
this gives staff the option to make programs up and if they know html they can us that to make a more
advanced looking program.
### Making A PT Session
1. First check the link works.
2. no other pt sessions are appearing from other pt's
![filter working and link works](docs/readme-images/adim-view-with-filter.png)
this shows that the admin has given the right access.
Making a new session in the menu the link works and the view is limited to only session made by the current user logged in
![making a new session](docs/test-images/making-a-session.png)
next i filled out the form and check all the required and tested what clients can add the session to.
![filling out form](docs/test-images/filling-out-form.png)
now to check if the session will be added after I confirm the form.
![form added](docs/test-images/new-session-added.png)
The next check is to make sure its on the market place and adding to basket works too.
![added to market place](docs/test-images/new-session-on-market.png)
the last check is to see if you can view the session from you profile where it is stored
![final view](docs/test-images/final-view.png)
##### issues
while testing this the only issue i can think of is that you can add anyone as the user but this will be counted because all members of staff will be trained to use this and if they select the wrong person we have a admin team to fix the issue.
## Reviews