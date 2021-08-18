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
    <!-- <a href="https://github.com/karolchmiel94/netguru-interview-task">
        <img src="" alt="Logo" width="80" height="80">
    </a> -->
    <h3 align="center"><a href="https://github.com/karolchmiel94/netguru-interview-task">netguru-interview-task</a></h3>
    <p align="center">
        Best RESTful API to save, browse, and rate cars!
        <br />
        <br />
    </p>
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

<!-- Setup -->
## Setup


> git clone https://github.com/karolchmiel94/netguru-interview-task.git
> cd netguru-interview-task
> docker-compose up

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