https://www.youtube.com/watch?v=jFOR1LBEUgM

save typing

Functional
- give 2 suggestions to the user as they type

Out-of-scope
    region based
    filteration on word suggested

Non Functional
- fast response time (<200ms)
- scalability
- availablity



Trie to the rescue
insert search O(L) L length of word
sapce O(L*N) N number of words

aim for speed

optimized. store top 2 rank word at the node itself

LB

Type Ahead Service -> get prefix -> to to redis
    Y: Yell, Youtue
    YO: Youth, Youtube
    YOU:
    YOUTH

distributed Cache

Database (trie - DB)
    nonSQL unstructured
    clusters with cluster manager zookeep (manage the config file)
    N1 N2 N3 N4 N5 (trie on at least 3 nodes)
    if cache miss:
        request goes to zoo keeper
            A-B -> N1 N2 N3
            Y-Z N1, N3, N5
            Z-ZZ -> N5,N5
            put in the cache


    different partition strategy
        1. base on first letter A,B. hotspot
        2. based on maxicum capacity of ther server as long as they can fit
           1. A - AABC
           2. AABD - BXA

        3. Hash. the term -> multiple tries and need aggregation. need to involve all servers

How to build the trie?

Word Collecter Service (single design for twitter trend)
    -> HDFS (last 15 mins)
    -> Spark Streaming Service (1 hour)
        1. spark mr job, count frequency and rank (most recent has higher weight)
        2. created trie -> update trie DB

        -> distributed queue -> update cache



Typeahead Client side optimziation
    think Angular, observable