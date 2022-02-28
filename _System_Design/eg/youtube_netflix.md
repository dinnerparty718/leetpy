High Availablity

1.5B total user
700M daily acitve user

upload/view
read:write ratio to be 200:1


Bandwidth
    5GB/sec
    Assuming an upload:view ratio of 1:200, we would need 1TB/s outgoing bandwidth.


thumbnail

Video Uploads: Since videos could be huge, if while uploading, the connection drops, we should support resuming from the same point.



Metadata Sharding
    userID
    videoID better


Video Deduplication
    algo:  Block Matching, Phase Correlation

dynamic HTTP redirections
Content Delivery Network (CDN)