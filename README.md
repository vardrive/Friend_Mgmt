# DRF Friend Management

## Overview 

This application enables you to to create and manage friendships and follows between users.

It features a custom User model to define email as username.

## Requirements

- Python - 2.7.6
- Django - 1.11.4
- Django REST Framework - 3.6.4
- django-friendship
- django-MySQL-python

## Usage

URLs
```
http://localhost/users/  			# List of users
http://localhost/friends/'email address'/ 	# List of friends of user
http://localhost/followers/'email address'/ 	# List of followers of user
```


