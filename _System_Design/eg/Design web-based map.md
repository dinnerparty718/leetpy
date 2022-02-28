# Read-heavy application
    writes are minmal compared to read
    data can be cached


# Data Type: Spatial
    some db out-of-box support

# Database


The coordinates of the places are persisted in the database
We can expect a surge in traffic on the service during peak office hours, festivals or any significant events in the city

need to scale up and down on the fly

A NoSQL graph database would fit best as a database for this application. horizontal scale in nature
Real-time features


# Architecture
    client server


# Backend technology
    We can pick Java, Scala, Python, and Go in the server-side language


# Monolith vs microservice
    core feature?
        - map search
        - plan our routes

# APIs
    Direction API, Distance Matrix, Geocoding, Places, Roads, Elevation, Time zone, and Custom search API.
    so monolith out of the picture

We need microservices to implement so many different functionalities. Let’s write a separate service for every feature. This is a cleaner approach and it will help the service scale and stay highly available. 


# Server-side rendering of map tiles
    we can cache the rendered image for future requests. The image is static content and will be the same for all the users.
    Smaller tiles help with the zoom in and out operations. 

    We can create the map in advance by rendering it on the server and caching the tiles. Also, we would need a dedicated map server to render the tiles on the backend.


# User Interface


So, here is the flow: the user runs a search for a particular location. The request is routed to the tile cache on the backend, which contains all the pre-generated tiles. It sits between the UI and the map server. If the requested tile is present in the cache, it is sent to the UI. If not, the map server hits the database, fetches the coordinates and related data, generates the tile and returns it to the user.


# Real-time features (resource-intensive)
    we have to establish a persistent connection with the server.
    implementing real-time features only when they are really required.