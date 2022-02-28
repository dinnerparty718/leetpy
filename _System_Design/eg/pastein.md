High Availability

5:1 ratio between the read and write



DB
    Paste (only store the content key that point to file storage)
    User

standalone Key Generation Service (KGS) 


Datastore layer
    metadata mysql or mongoDB or Cassandra
    storage



How to Clean up

1. Whenever a user tries to access an expired link, we can delete the link and return an error to the user.
2. seperated clean up process. when traffic is low
3. We can have a default expiration time for each link (e.g., two years).
4. After removing an expired link, we can put the key back in the key-DB to be reused.
