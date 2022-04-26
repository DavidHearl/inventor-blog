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




## To Do List - Will be removed before final deployment

- Add google adsense to the website

- Delete comments for user

