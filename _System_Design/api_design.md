https://www.youtube.com/watch?v=6RvlKYgRFYQ

### 1. API Paradigms

### REST VS RPC VS GRAPHQL

## REST representational state transfer REST


resources
    use nouns

    CRUD - CreatReadUdateDelete

    POST PUT PATCH GET DELETE
    return JSON

    https://foobar.com/api/v1/uesrs
        get entire collections
    https://foobar.com/api/v1/uesrs/user_1
        get single entify

    represent relationship
    https://foobar.com/api/v1/uesrs/user_1/orders
    https://foobar.com/api/v1/uesrs/user_1/orders/order_1

    non-crud operations?
    archive ?

    PATCH /users/user_1
    body :{ "archived": true }

    Deactivate -> user subresource level, can use verb

    PUT /users/user_1/deactive

    Search? use query parameters
    PUT /search/code?name=bob

# Pros
    - Standard method names/arguments and status coes
    - Utilizae HTTP features
    - Easy to maintain
 # Cons
    - Big payloads -> can solved by GraphQL
    - Multiple HTTP roundtrips
      - resource and subrerouces. two seperate calls

Rules of thumbs:
    - Best for APIs that expose CRUD like operations

## Remote Procedure Call


## RPC 

about Actions (e.g slack)
    - GET
    - POST

# Pros
    - Easy to understand
    - Lightweight payload
    - High Performance
# Cons
    - Discovery is difficult (not standardize)
    - Limit standardization
    - lead to function explosion

Rules of thumbs:
    - Best for APIs that expose actions


## GraphQL APIs

developed by facebook, adopted by github yeal
https://api/github.com/graphql
    POST GET

query:

{

    User {
        name
        username
    }
}

# Pros
    - Saves multiple round trips
    - Avoids versioning
      - add new field without breaking
      - can deprecate fiels
      - smaller payload size
# Cons
    - Added complexity
    - Optimizing performance is difficult
      - use cases
    - Too complicated for a simple API

Rules of thumbs:
    - Best when you need query flexibility


### 2 Event-Driven API

e.g
Request: Get Status
Reponse: Status - Processing
Keep sending Request until data is complete
long polling -- not efficient

Event-Driven API solve this problem


## different styles
    - WebHooks
    - WebSockets
    - HTTP Streaming

# WebHooks
    register with interested events and callback URL
    - in English: this is the event I am intested in, this is where you should send the information
    - API provider send Event Update POST
    - similar to mailing systems
      - don't have to poll 

Pitfalls
    - Failures: Ensure delivery through retries (API provider need to retry)
    - Firewalls: Apps running behind firewalls can send, but receiving can be trickey
    - Noice: each webhook represnet a single event. Many events in a short time can be noisy

# WebSockets

client -> handshake(http)                   server
        <- upgrade to WebSocket
        <-> Bidirectional communication

use case: chat, games

Pros
    - Bidirectinal low latency communication (single TCP connection)
    - Reduced overhead of http requests

Cons
    - Clients are responsible for driving connection lifespan
    - Scalability challenges - server


# HTTP Streaming (long lived connection)

client -> request server
    <- New Events indefinite
    <- New Events indefinite

    two ways
        1. chunked, no browser client
        2. Server-Sent-Event, for browser  -> twitter
Pros:
    - can stream over simple http
    - Native browser support
Cons:
    - bidirecitonal communication is challenging
    - buffering


### API Security
[link] https://www.youtube.com/watch?v=x6jUDfpESmA

## Authentication and Authorization

Authentication: verify who you are
Authorization: verify what you're allowed to do, resources you're allowed to access


# Basic Authentication -> lagacy
    user/password Base64 encoded with SSL
    sent for each reqeust, higher changes for being hacked

    twitter moved on to Oauth

# Oauth 2007 standard
    Allows user to grant access
    1. No password sharing
    2. revoke access from application individulally
    3. granular access to resources

    Oauth:  flow   Authorizaiton Server resource Server
   
        Redirect URL
        Callback URL
        response type - code
        Scopes - write
    
    return authorization code & refresh token to exchange for get access token (for security)
    
    back channel will also attach a "secret"

    

    openID Connect
        simple identify layer
    
        Redirect URL
        Callback URL
        response type - code
        Scopes - openid
    
    return id token


    Scopes
        used to limit an application's acces to user data
        need to be specified scope 'read-tweet'
        
        read
        write
        read/write

        Twitter

        Timeline Followers Messages Tweets

        app

    Refresh Tockens
        allows access tokens to be renewed
        used to request new token when old one expires
        client id and secret


## react node and oauth2 
[link] https://www.youtube.com/watch?v=dyZmsz6usWk


### Web API Pagination
## Offset-based vs Cursor-based


# Offset-based
    Client provides
    - Limit - maxinum number of items in a batch AKA page
    - offset - The starting position in the list of items

    https://www.awesome-store.com/products?limit=50&offset=100

    setect *
    from products
    order by id desc
    limit 50 offset 100

Pros
    - simple implementiation for client and server
    - possible to jump to arbitrary pages
Cons
    - unreliable results
    - Inefficient for large or distributed datasets

# Cursor-based
Client requests with a limit
    https://www.awesome-store.com/products?limit=50
Server responds with results and a next-cursor
    next-cursor=12345678
client includes this cursor in subsequent requests
    https://www.awesome-store.com/products?limit=50&nextCursor=12345678

Pros
    improve performance - index on cursor
    consistent results
cons
    clients need to traverse through each page one by one
    records need to added sequentially to the DB
    client need to manage the next cursor



### Web API Rage Limiting

1. Prevent single point of failure (DoS attack)
2. Prevent misuse



1. avoid global rate limites
2. measure clients based on use case

Users -> per-user basis
application -> per-application basis
Unauthenticated -> IP address

3. design for occasional traffice bursts
4. Allow exceptions for high profile clients
   
API Performance
    Redis or Memcached
Rate Limiting algorithems
    - token bucket
    - fixed window counter
    - sliding window counter