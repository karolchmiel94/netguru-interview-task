<!--
repo name: netguru-interview-task
description: Simple e-commerce website with blog
github name:  karolchmiel94
link: https://github.com/karolchmiel94/netguru-interview-task
logo path:
screenshot:
email: karolch94@gmail.com
-->

<!-- PROJECT LOGO -->
<br/>
<p align="center">
    <h3 align="center"><a href="https://github.com/karolchmiel94/netguru-interview-task">netguru-interview-task</a></h3>
    <p align="center">
        Best RESTful API to save, browse, and rate cars!
        <br />
        <br />
    </p>
    <h3 align="center"><a href="http://guarded-ocean-69420.herokuapp.com/">Link to project on Heroku</a></h3>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [Requirements](#requiremens)
- [Setup](#setup)
- [Functionalities description](#functionalities-description)

<!-- Requirements -->
## Requirements

- Docker
- memcached

Project uses memcached locally. To be able to use this cache system, you have to have it's dependencies installed.

Mac OS:
> brew install memcached

Linux:
> sudo apt-get install memcached


<!-- Setup -->
## Setup

- Run cache system

For cache system to work locally, it has to be run as daemon with

> brew services start memcached

or

> sudo service memcached start

command or by running

> memcached

in a dedicated terminal window.

- Clone project

> git clone https://github.com/karolchmiel94/netguru-interview-task.git

> cd netguru-interview-task

- Build and run image

> docker-compose up --build -d

Application is up and running at localhost:8000/

<!-- Functionalities description -->
## Functionalities description

Local database uses sqlite3 so it require no setup. Application hosted on Heroku uses Postgres.

Car models, fetched by theirs maker, are saved in cache using memcached to improve response times.

List of cars, with theirs average ratings, is available under:
GET /cars/

Adding a car can be done via:
POST /cars/
{

  "make" : "Volkswagen",
  "model" : "Golf",

}

Cars can be deleted by providing their id under:
DELETE /cars/{ id }

List of cars ordered by the number of rates is available under:
GET /popular/