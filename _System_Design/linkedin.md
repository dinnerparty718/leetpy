## scaling


[link] https://engineering.linkedin.com/architecture/brief-history-scaling-linkedin


# offline workflow
    precomute data insights like 
        people you may know
        similar profiles
        notable alumni
        profiel browse maps

Profile Page
University Page


## how does linkedin know if user is online

# https://www.scaleyourapp.com/linkedin-real-time-architecture-how-does-linkedin-identify-its-users-online/



Apache Globin: The Stateful Logical Pipeline
Data Ingestion

# todo

[link] https://www.youtube.com/watch?v=BQ7aONetKl4

Stats

300B Kafka Events daily
200TB Data Ingested Daily
250PB Data on HDFS

- Connector Diversity

in parallep
Source -> Work Unit -> tasks ETL -> Data publish

WorkUnit
    A logical unit of work.  
    - Kafka Topic
    - HDFS Folder
    - Hive Dataset

