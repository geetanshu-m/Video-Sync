# Video Sync
## Track youtube for a specific search

API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

### Tech Stack

- Django / Django Rest Framework
- Clery + Celery Beat
- Redis

### Things achived in the project

- Included Async worker which runs tasks periodically.
- Exposed GET API to get the results present in the DB.
- Over this get API with search query param, service can search on the tile and description
- Project Dockerized

### How to run this application

**Make sure that docker and docker-compose is already present in your system, otherwise this will not run**

- Add .env file which whould contain the following things in the root folder
```
QUERY=YOUR_QUERY
YOUTUBE_API_KEY=API_KEY
```
- run ```docker-compose build```
- run ```docker-comopose up```
- the server is now running on localhost:8080

### API's that are exposed

**Get all the Videos**
```
Request
{
    url:"/"
}
Response
[
    Array of Objs
]
```
**Search among the existing records**
```
Request
{
    url:"/?search=abc"
}
Response
[
    Array of objs
]
```
