# BACKEND CODE CHALLENGE

## Instructions to run 
Easy way: visit this [link](http://santoscoy.pythonanywhere.com) and login with:
+ username: admin
+ password: admin

Now go to the ***Instructions to fill the information of admin user***.

If you want to run locally, download this repo, unzip and open the terminal on the unzipped directory. 
Then run the follow commands:

1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver`

Then go to [127.0.0.1:8000](http://127.0.0.1:8000)

## Instructions to login as admin

If you decided to visit the production [link](http://santoscoy.pythonanywhere.com), you can pass this step and go to the 
***Instructions to add staff user*** section, otherwise open a new terminal go to repo directory and run the follow command:
+ `python manage.py createsuperuser`

It then will ask you to enter a username, email address and password. When finish go back to [127.0.0.1:8000](http://127.0.0.1:8000) 
and login with the username and password you have been register.
## Instructions to fill the information of admin user

Now you should be on the home page, go to the User link at left as the follow image

![User_link](https://user-images.githubusercontent.com/92071602/164566577-5af8d3ac-3c96-445d-b2fa-2b6d64b9bb93.jpeg)

and click on the *admin* link. Then you will be redirect to a form like the follow image:

![user_form](https://user-images.githubusercontent.com/92071602/164569818-b987b09b-c36a-4b0c-b8f6-f12292cffa4a.jpeg)

fill the fields and click on the save button at the bottom.

## Instructions to add staff user 

To add staff user 
then click the *ADD USER* button at right upper corner, this:
![ADD_USER_button](https://user-images.githubusercontent.com/92071602/164567136-387a00ab-de69-4d31-95cf-328d617b779f.jpeg)
Now you have been redirect to a form that will ask you to enter the username, password and confirm password. Fill the fields and click on the save button
then you will be redirect to a form like the one we saw before on the ***Instructions to fill the information of admin user*** fill it and check the box 
*Staff status*.

![staff_status](https://user-images.githubusercontent.com/92071602/164568446-594074b3-1e83-4d6c-b31a-5bce90275c42.jpeg)

Then scroll to the *User permission* section and select the follow permissions:
+ auth | user | Can view user
+ code_challenge_app | email | Can add email
+ code_challenge_app | email | Can view email
+ code_challenge_app | email_template | Can view email_template

as the follow image:

![WhatsApp Image 2022-04-21 at 6 52 49 PM](https://user-images.githubusercontent.com/92071602/164569300-82f60a9d-144d-4bbe-9ae4-3e6fc249be87.jpeg)

Then click on the button save at the bottom.


## Instructions to add template email

Go to the homepage and click on the *Email template* link, then click the *ADD EMAIL_TEMPLATE* button, then you will be redirect to a form like this: 

![WhatsApp Image 2022-04-21 at 7 17 11 PM](https://user-images.githubusercontent.com/92071602/164570951-36f1ad2c-9bb4-4779-8771-07d9870d0987.jpeg)

Here you  can fiel the fields as you want, but i recomend use the follow content:

+ tittle: Python course
+ subject: {0}, welcome to the new Python Course!
+ content: This email is intended for {0},
We are pleased to let you know that you have been selected to participate in our
new Python Course. Please send us your information and documents to
complete the registration process to continue with the course. In addition, we
have attached the course syllabus to this email.
You have seven days from now ({1}) to complete the registration.
Greetings from Python School!

+ NOTE: {} is used to pass variables to a formated string, in the subject field  the 
variable {0} is the name of the user to whom the email will be addressed, and in
the content field, the variable {0} is the name of the user starting with the 
last name and separated by a comma, and the variable {1} is the date and time
the email was created. They will be reflected only when a new email is created,
later.

When finish fill the fields, click on the save button at the bottom.


## Instructions to add email

Now we are ready to create an email, click on the email link at left and click on the 
*ADD EMAIL* button. you will be redirect to a form like the follow image:

![WhatsApp Image 2022-04-21 at 7 37 24 PM](https://user-images.githubusercontent.com/92071602/164573438-c2e7febd-8164-4975-96df-8a72323b4afc.jpeg)

To fill the filds you have to click on the magnifying glass icon, and select a template and a user.
Select that one you want and click on the save button. 

You will be redirect to a email objects page and should seems like this:

![WhatsApp Image 2022-04-21 at 7 44 42 PM](https://user-images.githubusercontent.com/92071602/164575196-f4c00c32-b011-4c36-a525-aeaa5b0c2530.jpeg)

you can click on the *Python Course* link and the fields that where empty are now rendered as the template that have been selected before, also 
can click on the *VIEW ON SITE* button to show how is rendered in a html template.

NOTE: The admin site have some configured features, like look in email templates by template name, or
look in emails by related template, related user or the email address of the creator of the email, also
if the data base have a lot of emails can filter by related template, related user ,etc.





