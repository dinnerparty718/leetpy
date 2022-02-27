
https://microservices.io/patterns/data/saga.html

# Segregated Access of Global Atomicity

### ACID across service

Solution

Implement each business transaction that spans multiple services is a saga. A saga is a sequence of local transactions. Each local transaction updates the database and publishes a message or event to trigger the next local transaction in the saga. If a local transaction fails because it violates a business rule then the saga executes a series of compensating transactions that undo the changes that were made by the preceding local transactions.


# Pros

It enables an application to maintain data consistency across multiple services without using distributed transactions

# Cons

a developer must design compensating transactions that explicitly undo changes made earlier in a saga.


A client that initiates the saga, which an asynchronous flow, using a synchronous request (e.g. HTTP POST /orders) needs to be able to determine its outcome. There are several options, each with different trade-offs:

The service sends back a response once the saga completes, e.g. once it receives an OrderApproved or OrderRejected event.
The service sends back a response (e.g. containing the orderID) after initiating the saga and the client periodically polls (e.g. GET /orders/{orderID}) to determine the outcome
The service sends back a response (e.g. containing the orderID) after initiating the saga, and then sends an event (e.g. websocket, web hook, etc) to the client once the saga completes.

