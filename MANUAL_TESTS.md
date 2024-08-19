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
![making session form](docs/test-images/making-session-form.png)
![new session made ](docs/test-images/session-made.png)
![delete session test](docs/test-images/test-delete.png)
![delete session test alert](docs/test-images/delete-session-alert.png)

### Making Exercise , Delete & Update
#### Making A New Exercise
![exercise view](docs/test-images/exercise-page-view.png)
![making new exercise](docs/test-images/making-new-exercise.png)
![exercise added](docs/test-images/new-exercise-added.png)
#### Updating
![updating session test](docs/test-images/testing-update-exercise.png)
![update successful](docs/test-images/update-exercise-alert.png)
#### Deleting 
![testing Delete](docs/test-images/testing-exercise-delete.png)
![delete success](docs/test-images/delete-test-success.png)

## PT Sessions
## Reviews