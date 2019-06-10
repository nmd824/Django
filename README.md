# Permissions Blog Site

This is a very simple Django web application. As this is my first time writing an application in Django and Python (I've only ever written short Python scripts to automate things on my Mac), I'm sure it's not very good in generally and can be improved a great deal as I learn more.

## Required packages

Please see requirements.txt

## Database

This web application uses PostgreSQL with a database called myDB with an user named "myprojectuser" and password is "password".

## Running the server

Start the virtual environment and use the following command to start the server: python manage.py runserver

## Create a Mobile App

Go to http://127.0.0.1:8000/create_app_form/ and fill up the form.

The data will be stored in the database and can be seen from http://127.0.0.1:8000/admin/PermissionsBlogSite/mobileapp/

Icon will be uploaded to the media folder.

## Create an App Permission

Go to http://127.0.0.1:8000/create_permission_form/ and fill up the form.

The data will be stored in the database and can be seen from http://127.0.0.1:8000/admin/PermissionsBlogSite/apppermissions/

## Edit an App Permission

Go to View All App Permissions and click on the "Edit" link.

Alternatively, go to http://127.0.0.1:8000/edit/<pk> where <pk> is the primary key of the App Permission that you want to change.

E.g. If the App Permission to be changed has a primary key of 1 in the database, the link to edit it would be http://127.0.0.1:8000/edit/1

### Shortcomings

This is a terribly written page in my opinion. It's unintuive and not user friendly at all (it assumes the user knows the primary key).

One problem with this page is that I could not figure out why my instance is not being loaded into the page so that the user can see what needs to be edited.

## View All Mobile Apps

Go to http://127.0.0.1:8000/view_all_apps/. All the Mobile Apps that were stored will be displayed with the information in the models.py.

## View All App Permission

Go to http://127.0.0.1:8000/view_all_permissions/. All the App Permissions that were stored will be displayed with the information in the models.py.