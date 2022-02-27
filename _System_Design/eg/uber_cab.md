https://www.youtube.com/watch?v=Tp8kpMe-ZKw



- see cabs
- ETA & approx Price
- Book a cab
- Location Tracking


- Global
- low latency
- high availabl
- hight consitency
- scale
  - 100M MAU
  - 14M rides per day




how to find the nearby driver

map cab to segment
    get continues ping from cab. assgin segment
    calculated from runtime
    
Maps:
    divide city in 
    lat/long belong to segmnet
    calculation ETA
    get route
    segment decrease. 

## user app
    user service  redis, userDB mySQL
ws  cab request service
    request cab finder

## dirve app
    driver sercie redis, userDB mySQL
    
    Web socket connection
    
    location Service



Drivers are connected websocket handler
    have connection ready
    service also want to talk to driver


    webSocket manager -> store in redis -> also persistent
        keep track which websocket handler connnect to each driver

        two way mapping
            driver -> handler
            handler -> driver

    handler send location to 
        Location Service 
            -> cassadra, scale up
            live location
            route , for billing service

            Redis (what drivers in S1)
                S1: d1,d2,d3

        Location Service -> Map Service




## Trip serivce

# live and archiver
    live trip store in mysql (transactional property)
    archived trips stores in casaandra for read


## Trip Archiver
    runs cron job every 12 hours


Go through the flow


## driver priority engine
    give a list of driver
    return potential


## Payment Service
    listen for kafka, insert to mysql

    kafka -> sparking streaming cluster
    spark ML/job

    - user profileing
    - driver profiling
    - premium vs regular


    Driver Priority Engine

    Fraud Engine






REAL uber


https://www.youtube.com/watch?v=AzptiVdUJXgs


1. Car current location index
2. Fast queries by location
3. by car properties
   1. current capacity (uber pool)
   2. Driver stip status
4. High volume of reads and writes
5. Do NOT need long-term duratle storage


in-memoery seraching index

Driver app -> update    Geobase    <- quries    rider app


Geobase Worker
    D0,D1,D2,D3
    update(driver1, location, onTrip, capacity, probA, probB)


    query(key-, center(), radius, filters:{})


Ringpop (open source) hash ring
    gossip essage
    a ring

options

city sharding
    San Francisco
    New York


Geosharding
    map -> small segment polygon


    San Fransisco UberX
    San Fransico UberPool

worker will handle prodcut by key


shart dimention
hotspot
    dimension
    varies with time

    partition by socondary key



Auto Repartition

Geobase  <- controller reassigment


Location Store quirement
1. high-volume of writes
2. durable storage
3. timeseirs read, where was a driver between Tstart Tend?
4. map-matched Data what was the path on a map

persistent in cassandra
    ringpop 
    need partition
        partition key driverUUID, time BUcket

    write?
    DC1 DC2
    write replication

    read?  add redis for recent trip


# todo

https://www.youtube.com/watch?v=ChtumoDfZXI

Map-Matched
why we need it?
