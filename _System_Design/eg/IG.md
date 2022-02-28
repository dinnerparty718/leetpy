High Availability

FR
1. Users should be able to upload/download/view photos.
2. Users can perform searches based on photo/video titles.
3. Users can follow other users.
4. The system should generate and display a user’s News Feed consisting of top photos from all the people the user follows


NFR
1. Our service needs to be highly available.
2. The acceptable latency of the system is 200ms for News Feed generation.
3. Consistency can take a hit (in the interest of availability) if a user doesn’t see a photo for a while; it should be fine.
4. The system should be highly reliable; any uploaded photo or video should never be lost.



Not in scope: Adding tags to photos, searching photos on tags, commenting on photos, tagging users to photos, who to follow, etc


never use userID for sharding
non-uniform distribution of storage

Sharding
1. by user id
   1. never use userID for sharding non-uniform distribution of storage
   2. what if one shard can't handle the size of user photos
   3. store all in on shard. if shard goes down
2. by PhotoID (need to generate ID before hand, so hash['id'] % numOfShard )
   1. DB  64 bit ID field.
   2. two mysql

KeyGeneratingServer1:
auto-increment-increment = 2
auto-increment-offset = 1

KeyGeneratingServer2:
auto-increment-increment = 2
auto-increment-offset = 2