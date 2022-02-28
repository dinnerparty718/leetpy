Availability

Size

500M
100M daily active users (DAU)





Extended Requirement
Snapshot?

Design Consideration
- Expect huge read and write volumes.
- We can reduce the amount of data exchange by transferring updated chunks only.
- By removing duplicate chunks, we can save storage space and bandwidth usage.
- For small changes, clients can intelligently upload the diffs instead of the whole chunk.

4 MB chunks SHA-256 hash


How should clients handle slow servers? Clients should exponentially back-off if the server is busy/not-responding. Meaning, if a server is too slow to respond, clients should delay their retries, and this delay should increase exponentially.

sync mobile on demand

Rich client

synchroization service


Metadata Partitioning
1. Vertical Partitioning (subject base)
   1.  Joining two tables in two separate databases 
2. Range Based
   1. unbalanced servers
   2. path starts with letter 'A','ZZ'
3. Hash
   1. FileID
   2. Consistent Hashing