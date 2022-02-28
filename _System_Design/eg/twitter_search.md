## Twitter Search

https://www.youtube.com/watch?v=NSmFpZk4H2I


Fanout service -> Ingester(LB micro service, high available) -> search index  (inverted index) -> blender 

    tokenize/term -> remove stop words
    inverted index
        word: [ tweet_id, tweet_id2 ]

    shard
        1. shard by word ( what if word become hot)
           1. add replica or cache
        2. shard by tweetID ?? hit all partition
        3. word and tweetID
     1. 

seattle is becoming hug and clour companies (filter out is and of, becoming)
stemming -> find root word
    companies -> company


https://www.youtube.com/watch?v=hFtj3SHC-SQ

Linkedin Chinese Version

# todo
Service discovery


apple
store
    apple intersection store

partition by?
    1. Term A-G machine1 ...
    2. by docID
    3. consisten Hashing -> bloom filter. false positive


by DocID
    all servers has index of all terms (apple)
    search for all servers
    n1 [1011,2333]
    n2 [5633,45444]

    combine n1 and n2



Steps
1. dispather generate epxpression tree (A & B) | C
why expreesion tree
    intermediate result helps reduce the data transfer (A & B) first then union C
2. apple & store first, hold on to C cupertino
   1. dispatcher send apple/store to controllers. consistent hashing
   2. resquest id , term
   3. how to reduce traffice for aggregator


# bandwidth

    10 times intersection

    res = {
        term: 'apple'
        min:1
        max: 3001
        count: 2100
    }

    res = {
        term: store
        min:101
        max:2001
        count: 1101
    }



## google


https://www.youtube.com/watch?v=CeGtqouT8eA


Term freq Occurence
quick 1   [ 1,[2] ] doc1 and position2

order matters

position in increment order
    doc1 [2,3,4]
    doc2 [1,2,3]


for prefix dog*

term can be sorted, perform binary search

*az* 