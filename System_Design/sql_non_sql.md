## when to pick noSQL


# handling a large number of read-write operations
    - parallel
    - add nodes on the fly
    - handle concurrent traffic
    - scale fast

# flexibility with data modeling
    - good for inital phrase of development
  
# eventual consistency over strong consistency
    - strong consistency -> performance tradeoff
    - eg. twitter influrencer tweet and reteets. the count of the retweet is not important.
    - geographically distributed nodes take some tiem to reach global consensus
    - inconsistency does not mean data loss.
    - youtube video, 10 views and 15 likes :)

# running data analytics
    - time-series
    - wide-column
    - document oriented
    - fb 2 petabyte of data per day in multiple clusters at different data centres.
  
SQL

[link] https://www.scaleyourapp.com/what-database-does-facebook-use-a-1000-feet-deep-dive/

facebook 
    - mysql for social graph (changed DB engine and make some tweeks)
    - InnoDB to MyRocks to reduce storage
    - 3.5 times smaller than the InnoDB instance uncompressed and 2 times smaller than InnoDB instance compressed.
    - Cassandra - for user inbox search
    - Apache Hive for data warehousing, query and analytics fb ads
    - Presto DB
Quora - mysql (partitioning the data at the application level)



## polyglot

[link] https://www.educative.io/module/lesson/web-application-architecture-101/N02NV6VLE5p#Graph-database

fb
    rdbms for user freinds likes or graph db like neo4j
k-v store
    user session
wide column db
    for analytics
    cassandra or HBase

ACID transaction - payment system

Graph database
    recommendation system

document-oriented datastore like Elasticsearch



# Eventual Consistency

optimistic replication

tweet like counts across the continent
Eventual consistency fits best for use cases where the data accuracy doesn’t matter much
the system keeping the count of concurrent users watching a live video stream,
dealing with massive amounts of analytics data, a slight data inaccuracy in real-time won’t matter much.

# Strong Consistency
bank stock market


# document-oriented data store
    semi-structured 
    flexible schema
    don't know how to 

    Typical use cases of document-oriented databases include:

use cases
    - Real-time feeds
    - Live sports apps
    - Writing product catalogues
    - Inventory management
    - Storing user comments
    - Web-based multiplayer games

Real-life implementations#
Here are some of the good real-life implementations of the tech:

SEGA uses Mongo-DB to improve the experience for millions of mobile gamers.

Coinbase scaled from 15k requests per min to 1.2 million requests per minute with MongoDB
[link] https://blog.coinbase.com/scaling-connections-with-ruby-and-mongodb-99204dbf8857

Blue-green deployment


# graph database

    fits best for modelling real-world use cases where entities have complex relationships.


    By design, graph databases can quickly query customers’ past purchases, as well as instantly capture any new interests shown in the customer’s current online visit — essential for making real-time recommendations.


# Key-Value Database
    O(1) Redis or Memcached
    Due to the minimum latency they ensure, that is constant O(1) time, the primary use case for these databases is caching application data.

Typical use cases of a key-value database are:

- Caching
- Persisting user state
- Persisting user sessions
- Managing real-time data
- Implementing queues
- Creating leaderboards in online games and web apps
- Implementing a pub-sub system


# Time Series Database

Influx DB, Timescale DB, Prometheus
Amazon Timestream

use casse:
    iOT
    self-driving car
    trading platform

writing an autonomous trading platform that deals with changing stock prices in real-time, etc.

Time-series data is generally ingested from IoT devices, self-driving vehicles, industry sensors, social networks, stock market financial data, etc.

Studying data streaming-in from applications helps us track the behavior of the system as a whole. It allows us to study user patterns, anomalies, and how things change over time.

Time-series data is primarily used for running analytics and deducing conclusions. It helps the stakeholders make future business decisions by looking at the analytics results. Running analytics enables us to evolve our product continually.

Regular databases are not built to handle time-series data. With the advent of IoT, these databases are getting pretty popular and adopted by the big guns in the industry.



# Wide-Column Database

Cassandra, HBase, Google BigTable, ScyllaDB
