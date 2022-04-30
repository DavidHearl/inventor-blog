# Inventor Blog - [Live Website](https://inventor-blog.herokuapp.com)

Multi Device Layout will go here
https://techsini.com/multi-mockup/index.php

## About
---

CAD Tips is a fully responsive blog where users can come to learn how to use Autodesk Inventor.
The user will find helpful posts and examples which they can complete to increase their skill!

## Table of Contents
---
1. [User Stories](#UserStories)
2. [Features](#Features)
3. [Databases](#Databases)
4. [Technologies Used](#TechnologiesUsed)
5. [Testing](#Testing)
6. [Validator Testing](#ValidatorTesting)
7. [Bugs Found](#BugsFound)
8. [Deployment](#Deployment)
9. [Acknowledgement](#Acknowledgement)

## User Stories
---

### Admin

- As an admin I want to approve posts before they are published so I can keep the infomation on the site relevant.
- As an Admin I want to create, read, update and delete posts so that I can manage my blog content
- As an Admin I want to create draft posts so that I can take more time to create content.
- As an Admin I want to apporve or reject comments so that I can filter out irrelevant comments.

### User

- As a Site User I want to see the number of likes on each post so that I can see which artile is the most popular
- As a site user I want to view comments on the article so I can read the conversation and get more knowledge
- As a Site User I want to register an account so that I can comment and like
- As a Site User I want to leave a comment on a post so that I can be involved in a conversation
- As a Site User I want to leave a like or unlike a post so that I can interact with the content.

### Visitor

- As a visitior I want to see a list of posts so that I can select the post I would like to read.
- As a visitor I want to click on a post so that I can read the full content as see all the information

## Features
---


### Color Scheme
---


## Databases
---

### Structure

## Technologies Used
---

### Languages

- HTML
- CSS
- Python
- JavaScript

## Testing
---


| Number | Marking Criteria | Met |
|:-:|:----------|:---:|
|1.1|Design a Front-End for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions.||
|1.2|Implement custom HTML and CSS code to create a responsive Full-Stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions||
|1.3|Build a database-backed MVC web application that allows users to store and manipulate data records about a particular domain.||
|1.4|Design a database structure relevant for your domain, consisting of a minimum of one custom model.||
|1.5|Use an Agile tool to manage the planning and implementation of all significant functionality||
|1.6|Document and implement all User Stories and map them to the project within an Agile tool||
|1.7|Write Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code.||
|1.8|Include sufficient custom Python logic to demonstrate your proficiency in the language||
|1.9|Include functions with compound statements such as if conditions and/or loops in your Python code||
|1.10|Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions).||
|1.11|Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility.||
|1.12|Document and implement all User Stories within the Agile tool and map them to the project goals||
|1.13|Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc.,created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation||
|2.1|Develop the model into a usable database where data is stored in a consistent and well-organised manner.||
|2.2|Create functionality for users to create, locate, display, edit and delete records||
|2.3|All changes to the data should be notified to relevant user||
|2.4|Implement at least one form, with validation, that allows users to create and edit models in the backend||
|3.1|Apply role-based login and registration functionality||
|3.2|The current login state is reflected to the user||
|3.3|Users should not be permitted to access restricted content or functionality prior to role-based login.||
|4.1|Design and implement manual and/or automated Python test procedures to assess functionality, usability, responsiveness and data management within the entire web application||
|4.2|Design and implement manual and/or automated JavaScript test procedures to assess functionality,usability, responsiveness and data management within the entire web application||
|4.3|Document all implemented testing in the README.||
|5.1|Use Git & GitHub for version control of a Full-Stack web application up to deployment, using commit messages to document the development process.||
|5.2|Commit final code that is free of any passwords or security-sensitive information to the repository and the hosting platform||
|6.1|Deploy a final version of the Full-Stack application code to a cloud-based hosting platform and test to ensure it matches the development version||
|6.2|Ensure that the final deployed code is free of commented out code and has no broken internal links||
|6.3|Document the deployment process in a README file in English||
|6.4|Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off||
|7.1|Design a custom data model that fits the purpose of the project||


## Validator Testing
---

- The HTML templates were checked using the 
- The CSS stylesheet was validated using the
- The JavaScript file was run through
- The Python Files were run through

## Bugs Found
---

## Deployment
---

1. Login to Heroku and Create a New App
2. Create a name for your app, It must be unique name (not just unique for your heroku projects)
3. Click "Create App" then select a region, either Europe or United States
4. Next, navigate to the 'Resources' tab. Move down to the add-ons section then in the box and search for 'Heroku Postgres', add the Heroku Postgres database to the project.
5. Next, navigate to the 'Settings' tab at the top of the page.
6. Scroll down to Config Vars (also known as Environment Variables, hence env.py) then click 'Reveal Config Vars'. 
7. Create 4 config vars ['CLOUDINARY_URL', 'DATABASE_URL', 'SECRET_KEY', 'DISABLE_COLLECTSTATIC']
8. The values of the first 3 variables then have to be mirrored in the env.py file (Make sure the env.py referenced in the .gitignore file)
9. In the settings.py file we need to import os, import dj_database_url and then create an if statement to import the env.py file. 
10. In the setttings.py file you also need to replace the insecure secret key with the one you made up
11. Scroll down and comment out the current database and past this code in DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
12. Update the 'INSTALLED_APPS' list with 'cloudinary' and 'cloudinary_storage'
13. In the settings.py file add:

- STATIC_URL = '/static/'
- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
- MEDIA_URL = '/media/'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

14. You need to set the BASE_DIR to 'BASE_DIR = Path(__file__).resolve().parent.parent'
15. Then add 'TEMPLATE_DIR' tot he Templates block
16. now to deploy to heroku you need to install the heroku cli, so paste this command into the terminal: 'npm install -g heroku'
17. Once the CLI has been installed you can login with 'heroku loging -i'
18. Then type 'heroku git:clone -a 'app_name'
19. Add and Commit as you normally would. Then to push to heroku use: 'git push heroku main' or to push to git hub 'git push origin main'

## Acknowledgments
---
