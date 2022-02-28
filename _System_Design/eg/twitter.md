# FR
- post new tweets (280 characters)
- follow other users
- mark tweet fav
- create / display user's time line consist of all users that following
- twee can contain photos and videos
  - t.co/

# NFR
- be highly available
- < 200 ms latency
- consistency can take a hit (for availablity)
  

# Extended


- search for tweets
- replaying to a tweets
- trends
- tagging other users
- tweet notification
- who to follow, suggestions
- moments



# Storage

1B user
200M DAU
100M tweets/day
avg 200 followers

100M * (280 bytes + 30bytes) = 30G/day

30*365 11TB per year
55 TB for 5 years

bandwidth

10b tweet views
10b * 280 bytes / 3600 * 24 = 32mb/s



# System API
(Post) tweet (api_key, tweet_id, tweet_data)

(GET) tweet(api_key, tweet_id)


# https://www.youtube.com/watch?v=LghAWi4H974


LB -> server cluster


# Database Schema

user(user_id, email, last Login)
tweet (id,user_id, lat, lo, createDate, numTimeFav)
userFollow(user1, user2) user1 following user 2
Faverates(tweet_id,userId)




# Data Sharding

Options
1. shard on userID (hotspot)
   A-M
   N-Z
2. shard on tweetID
   hashID % numOfDB    server1, server2

3. shard on creatTime



how to store tweets for fast read/read

generate tweet ID base on timestamp + sequence_number

If we make our TweetID 64bits (8 bytes) long
we can easily store tweets for the next 100 years and also store them for mili-seconds granularity.

## Cache

hash table  to case lastest 
  tweets  double linkedlist  head - new tweet - old tweet-tail (similary to LRU list)

LRU



## manhanttan project (eventually consistency)

hash funciton for partition key
which key range store in which parition -> keeps in zookeeper

leaderless replication + last write wins (inspired by dynamo) timestamp

write consistency waite for required number of response -> quorum within a region

twitter is quarum write

Read Repair
anti-entropy Repair -> merkle tree

SSTable -> borrowed from big table


B-Tree(inno DB, read-heavy)
RocksDB(all workload, both read heavy write heavy)


eventually consistency to strong consistency

