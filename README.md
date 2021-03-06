# **Memopolis**

A fullstack django project, with the aim to create, browse, comment, update and delete memes.

The project is hosted under https://www.memopolis.pl/. (Currently unhosted)

## Upvote System

This site features a system which allows to vote and unvote for a specific meme. Additionally, each user may see their own page that shows their five memes with the largest number of upvotes. This data is shown using chart.js.

![alt text](https://i.imgur.com/SAlWxOi.png "User upvotes")

# API documentation:

## Django REST framework
Memopolis offers an API, which is built on Django REST framework.

## Resources:
### Meme objects:
#### GET https://www.memopolis.pl/api/memopolis/meme
#### Description:
 Memes are displayed on the main page for example.
#### Properties:
        {
           "id": integer,
           "author": string,
           "title": string,
           "num_vote_up": integer,
           "tags": list of integers,
           "image": string,
           "date_posted": string,
           "accepted": boolean
        }
---
### Comment objects:
#### GET https://www.memopolis.pl/api/memopolis/comment
#### Description:
 Comments are displayed on individual meme pages (detail views).
#### Properties:
        {
           "id": integer,
           "author": integer,
           "content": string,
           "num_vote_up": integer,
           "date_posted": string,
           "belongs_to": integer
        }
---
### Tag objects:
#### GET https://www.memopolis.pl/api/memopolis/tag
#### Description:
 Tags are bound to memes and describe them.
#### Properties:
        {
           "id": integer,
           "name": string
        }
---
### User objects:
#### GET https://www.memopolis.pl/api/users/user
#### Description:
 Users are accounts created by website visitors. There is a difference between user objects and profile objects.
#### Properties:
        {
           "id": integer,
           "username": string,
           "last_login": string,
           "date_joined": string,
           "is_superuser": boolean
        }
---
### Profile objects:
#### GET https://www.memopolis.pl/api/users/profile
#### Description:
 A profile is a combination of a user and an image, which is used as an avatar.
#### Properties:
        {
           "id": integer,
           "user": integer,
           "image": string 
        }
