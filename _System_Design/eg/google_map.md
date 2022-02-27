https://www.youtube.com/watch?v=jk3yvVfNvds

function
- identify roads, routes
- distance & ETA bw 2 points
- plugable
  - plugin traffic
  - weather
  - accident
  - road block

Non Functional

- High Availablity
- Good Accuracy
- Not too slow
- scale
  - 1B MAU
  - 5M companies using API



HARD problem

massive dataset

A ----- B
directed graph with multiple graph

shortest path
    djiastra
    bellmen ford
pre-calculation


across segments / mega segment
    just get 20 segments running shortest path
    exit point
    dynamic programming


how to calucate weight
    - distance
    - ETA
    - Avg speed -> traffice / weather / other attr use statistics

ETA - use historical
    day of week
    hour of day
    if ETA > 30%
        recalculate

caculate avg speed and ETA

+-20%

Traffic weather
low       good
med       bad
ight


websocket
websocket manager -> redis
location service -> cassandra persistence
    -> kafka -> spark -> streaming -> hadoop


spark streaming (real-time processing for trends)
    - roads job
    - avg speed job last 15 mins -> update ETA, bubble up
    - hotspot
    - identifer


spark streaming for kafka

Kafka -> Map udpate servie -> Graph processing service -> cassandra

Hadoop
    Spark ML/Jobs
    - road classifier
    - vehicle classifier
      - bus? bus stopping not traffic 
      - ride is bumpy - two wheel vs four wheel

user device navigation workflow
    lb -> area search service -> Elastic Search
        > Navigation tracking service
            reroute
            deviating the route
            send to kafka
        > Map service
            -> graph processing service -> segment service -> cassandra (roads/live traffic)
            -> historical data service
                cassandra
                at day of week some hour the average traffic (google maps route planning)

            Third party data manager push data to graph processing service
            we can also verify the third party accuracy

dispute areas? India/China/Pakistan
    depend on where you're from
    LOL

