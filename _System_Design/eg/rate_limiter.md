Highly available

A rate limiter caps how many requests a sender can issue in a specific time window. It then blocks requests once the cap is reached.



against abusive behaviors targeting the application layer like
- Denial-of-service (DOS) attacks
- brute-force password attempts
- brute-force credit card transactions,



benefits
- Misbehaving clients/scripts
- Security
- To prevent abusive behavior and bad design practices
- To keep costs and resource usage under control
- Revenue
- To eliminate spikiness in traffic


Funtional
1. 15 per second
2. total count across a combination of server

Non-Function
1. Highly
2. should not introduce latencies


How
Rate Limiting
Throttling - HTTP status “429 - Too many requests".
    Hard Throttling
    Soft Throttling
    Elastic or Dynamic Throttling

Fixed Window Algorithm
Rolling Window Algorithm
Sliding Window with Counters (best)

    use redis hash
    Write-back cache



# https://www.youtube.com/watch?v=CRGPbCbRTHA
rate limit using redis