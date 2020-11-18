#  Mini Blog

 - Python 3.8
 - MySQL 5.7
 - Vue.js

## Run
Clone the repo
```sh
git clone https://github.com/parnus01/mini-blog.git
cd mini-blog
```

Start everything with docker-compose

Install [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

** 
For the first compose it will take some time to install the image and install the required packages
```sh
docker-compose up -d
```

## Quickstart
After start all container 

**First initial will take time for install node_modules**
- landing to  http://localhost:8080/
- login with default username / password
- CRUD Blog

Test Users
- john / john123!
- emmy / emmy123!
- robert / robert123!

## Container

- `backend` - For RestAPI develop with Flask
- `frontend` - For SPA develop with Vue .
- `db` - RDBMS.
