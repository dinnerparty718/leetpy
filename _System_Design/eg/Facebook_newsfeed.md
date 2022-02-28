### fb newsfeed or timeline


interanlly fb use mysql to represent the whole graph

mysql  (with shard)
    1. with sharding : comments of the post co-location. coming from one shard
    2. write new engine (MyRocks DB) to replace InnoDB. using Log Structure Merge (LSM) tree

Tao service (decide where new key belong)
Cache  write-through cache.


Feed generation:

1. retrie ids of all users/entity that Jane follows
2. Retrieve latest, most popular and relevant posts for those IDs. These are the potential posts that we can show in Jane’s newsfeed.
3. Rank these posts based on the relevance to Jane. This represents Jane’s current feed.
4. Store this feed in the cache and return top posts (say 20) to be rendered on Jane’s feed.
5. On the front-end, when Jane reaches the end of her current feed, she can fetch the next 20 posts from the server and so on.

Feed are genereating one time
for additional feeds
    if Jane online
         every 5 perform the above steps to rank and add the newer posts to her feed. Jane can then be notified that there are newer items in her feed that she can fetch.

components
1. Web servers: To maintain a connection with the user. This connection will be used to transfer data between the user and the server. WebSocket
2. Application Server. post stuff
3. Metadata database and cache: To store the metadata about Users, Pages, and Groups.
4. Posts database and cache: To store metadata about posts and their contents
5. Video and photo storage, and cache: Blob storage, to store all the media included in the posts
6. Newsfeed generation service: To gather and rank all the relevant posts for a user to generate newsfeed and store in the cache. This service will also receive live updates and will add these newer feed items to any user’s timeline.
7. feed notification server



Detail

offline generation newsfeed
how to store feeds in cache
    hash['userid'] : { linkhashmap (mantain insertion order, equivilant OrderedDic ), lastGenerated }
   

    linkhashmap: jump to any feed item and easy for iterate throught it
Should we generate newsfeed for all?
    LRU
    user pattern


Feed publishing

The process of pushing a post to all the followers is called fanout.



1. "pull" model or fanout-on-load
New data might not be shown to the users until they issue a pull request, user request update. response would be empty if there is no update
2. "Push" model or Fan-out-on-write
    long polling