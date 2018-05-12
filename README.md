# Instaclone
## A clone of the website for the popular photo app Instagram built using Django 1.11.


## By **[Samirah Maison](https://github.com/sami-mai)**

## Description
[This](https://mai-instaclone.herokuapp.com/) A clone of the website for the popular photo app [Instagram](https://www.instagram.com/) built using Django 1.11.

A user with an account can:
* post images with captions
* view list of other users
* follow other users and see their posts on their timeline
* like a post
* comment on a post
* download an image

## User Stories
As a user I would like:
* to sign in to use the application
* to upload photos
* to see my profile with my posts
* to follow others and see their picture on my timeline
* to like a picture and leave a comment on it
* download a picture and save it to my machine


## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd instaclone`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE gram
```
9. Change the database information in `instaProject/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instaclone',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
```
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application


## Known Bugs

No known bugs


## Technologies Used
- Python3.6
- Django
- Bootstrap
- Postgres Database
- CSS
- HTML
- Heroku

### License
This project is licensed under the MIT License - see the LICENSE.md file for details
MIT (c) 2018 **[Samirah Maison](https://github.com/sami-mai)**

## Acknowledgements
* Moringa School
