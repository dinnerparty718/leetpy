strong consistency


[link] https://www.educative.io/module/lesson/grokking-system-design-interview/qZ1v5v5n42p#1.-What-is-Facebook-Messenger?


Functional Requirements:

1. Messenger should support one-on-one conversations between users.
2. Messenger should keep track of the online/offline statuses of its users.
3. Messenger should support the persistent storage of chat history.


Non-functional Requirements:

1. Users should have a real-time chatting experience with minimum latency.
2. Our system should be highly consistent; users should see the same chat history on all their devices.
3. Messenger’s high availability is desirable; we can tolerate lower availability in the interest of consistency.

Extended Requirements:

1. Group Chats: Messenger should support multiple people talking to each other in a group.
2. Push notifications: Messenger should be able to notify users of new messages when they are offline.



High Level
- high levle graph
- detailed workflow 
  

Detail Component

1. Receive incoming messages and deliver outgoing messages.
2. Store and retrieve messages from the database.
3. Keep a record of which user is online or has gone offline, and notify all the relevant users about these status changes.



Server 50K concurrent connections at any time

as of 2012
WhatsApp handles 3 MILLION TCP Connections Per Server


keep user and server connection using webSocket
    where to find mapping table


maintain the sequencing of the messages
    use sequence number when client send out message


storage system:
    handle frequent write
    wide-column database solution like HBase (Cassandra)
         HBase is a column-oriented key-value NoSQL database that can store multiple values against one key into multiple column


Managing user’s status
    optimization of other users status count

Data partitioning
    should be on userID. Fetch them together
    how many shards/ partition
hash(UserID) % 1000


It’s extremely hard to failover TCP connections to other servers;
an easier approach can be to have clients automatically reconnect if the connection is lost.