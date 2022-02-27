Unique Id Generator


use cases: 
    url shortener
    debug?


1. Google spanner, auto increment primary key
2. LB -> server, UUID 8 - 4 - 4 - 4 -12 
3. LB -> server
   1. 128 bits
   2. Timesteamp 64 bits,  utc millisecondes
   3. 32 bits. server id (16 bit data center id, 16 server id)
   4. 8 bits. process id
   5. 24bit deduping 



https://www.youtube.com/watch?v=sf-p7B7ZWQA

requirement
any random unique id of some fixed size
unique id's in sequential order
unique id's in fix(64 bits) and be sortable


1. using UUID universal unique id same as GUID UUID 8 - 4 - 4 - 4 -12 = 36 char
   1. not sortable
   2. 128 bit too long
2. using database uniqueid
   1. too long 
3. ticket server
4. snowflakes from twitter (best)
    - timestamp , worker number, sequence number
    - time 41 bit


# unique ID generator
https://www.youtube.com/watch?v=Oh9-zd0If9U

1. multi-master replication
   1. increment count by k where k is number of server
      - mysql 1,3,5    -> web servers
      - mysql 2,4,6    -> web servers
    - need to think about add / delete server
2. UUID 128 bit. low probabilty collision
   1. need to figure if it fit 64 bit. 
   2. too long for the requirement
3. ticket server
   1. central server ticket server -> simple
   2. single point of failure
   3. replication
4. twitter snowflake (best)


64-bit ID

1 + 41 + 5 + 5 + 12

- sign bit ,1 bit. always 0. reserve for futre use
- 41 bits minisecond twitter snowflake default epoch
- datacenter id 5 bits 2^5 data centers
- machine id
- squence number 12 bits 
  - process/machine id
  - reset to 0 every lillisecond
  - max 4096 new id per millisecond

   

