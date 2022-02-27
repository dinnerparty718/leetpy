### Redis Cluster -> High Availability


HASH_SLOT = CRC16(key) mod 16384
Consistent Hashing vs Hash Slot

Master Replica




### Redis Sentinal (acheive High availablity)

Using Redis as an LRU cache

Eviction policies

It is also worth noting that setting an expire to a key costs memory, so using a policy like allkeys-lru is more memory efficient since there is no need to set an expire for the key to be evicted under memory pressure.

