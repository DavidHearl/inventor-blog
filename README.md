# Inventor Blog - [Live Website](https://inventor-blog.herokuapp.com)

CAD Tips is a fully responsive blog where users can come to learn how to use Autodesk Inventor.
The user will find helpful posts and examples which they can complete to increase their skill!

## User Experience

### Epics into User Stories

## Design

### Color Scheme

### Font

## Concepts - Wire Frames

## Agile Development

## Data Model

### Database Management System

### User Models

### Post Model

### Comment Model

### Database

## Technologies Used

### Languages

#### HTML, CSS, JavaScript, Python

### Version Control

#### Git, GitHub

### Responsive Design

[Techsini.com](https://techsini.com/multi-mockup/)

### Site Packages

#### Font Awesome

#### Google Fonts

#### Bootstrap




----------------------------

## Deployment

### Terminal Commands
- Install Django and gunicorn : pip3 install Django==3.2 gunicorn
- Install supporting libraries : pip3 install dj_database_url psycopg2
- Install Cloudinary Libraries : pip3 install dj3-cloudinary-storage
- Create requirements file : pip3 freeze --local > requirements.txt
- Create Project : django-admin startproject <ins>project-name</ins> . (Don't forget the dot)
- Create App (blog) : python3 manage.py startapp <ins>app-name</ins>
- pip3 install django-allauth
- pip3 install django-crispy-forms

## Installation & Command Line

- python3 manage.py migrate
- pip3 freeze --local > requirements.txt
- pip3 install django-summernote


## Creating a super user

- python3 manage.py createsuperuser

## Testing

For testing purposes two users have been created.

admin and user, both share the same password.

python3 manage.py test blog.tests

## To Do List - Will be removed before final deployment

*** Everything in Order ***

- fix python tests, then run pep8 on test files
- delete comments for users
- style website
- type up userstories in github
- write readme
