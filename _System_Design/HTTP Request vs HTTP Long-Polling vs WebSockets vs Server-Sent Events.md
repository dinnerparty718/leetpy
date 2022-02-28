# HTTP Request
    client send data to server
    handshake
    open connection
    connection close

    fecthing profile info

# HTTP Long-Polling
    client make a request to server
    client waits for server to response
    connection open for a long time
    connection get closed
    timeout for the request, make a new response

# Http Polling (not recommendation)
    client make a request to server
    regular intervel 1s 2s
    empty response
    unnessarry network calls
    drain batter of mobile device

# WebSockets
    persistent connection between client-server
    bi-direction communication
    HTTP TCP/IP

    handshake with server'
    connection established
    reduce overhead of handshaking. (on time )

# Server-Sent Events
    only server can send to client
    eg. stock price. live feed. shwoing client progress