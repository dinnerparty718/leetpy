# Booking Engine

book my show/fandango

High available
Scalable
fault tolerant


how to know available

1. connect to db
2. use theatre api


10 mins for reserve


# search Elasticsearch

# cache 
    static info
    redis - distributed and persistent
    
# DB
    need acid property
    country - city -> theater,hall -> show
    RDBMS mysql or prosgres / sharded by geo
        master read replica

    trailers, movie info -> NonSQL distributed. cassadra. replication factor

# async worker
    kafka 
    PDFS, BNG send email. SNS

# hadoop for data analytics
    HIVE
    ML (recommendation)

# Spark or storm for trends
    fault detection

# Payment
    third paty
    paypal
    stripe

workflow

    nearby theatre
    movie
    open a show
    available seats
    make API call to theatre DB, to block the seat 10 mins
    theatre give back unque ID
    show QR code


# logstash


# tables

theater
screen -> tiers -> seats


Nosql
    comments
    ratings
    movie info
    trailer
    artist
    cast
    reviews
    analytic data


[link] https://www.youtube.com/watch?v=Kt8a_4Ahds8

Booking engine layers
1. intergration with suppliers
2. Search rules
3. pricing changes
4. booking and ticketing flows



OTA online travel agency
    via API
    - send reqeust for inventory
    - check inventory availablity
    - get price
    - book travel products
    - receive ordered tickets