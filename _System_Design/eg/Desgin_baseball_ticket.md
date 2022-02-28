A Baseball Game Ticket Booking Web Portal

# Database
    payment system need ACID trasactions
    MySQL

# Handling concurrency
    is there a peak time
    usage pattern
    There will be a surge of fans on the portal to buy tickets for the baseball game as soon as they are made available.

    Also, the number of requests will naturally be a lot more than the number of tickets available. At a point, there will be n requests to buy one ticket. We need to make sure the system handles this concurrent scenario well. How will you implement this scenario? Think about it.



# Message queue or Database locks and Caching

    FIFO

    Generally, on e-commerce sites or travel booking websites, the number of tickets/products shown on the website is not accurate, and they are inconsistent cached values. When a user moves on to buy a particular ticket/product and checks out the cart, the system polls the database for the accurate count and locks the resource for the transaction.


# Backend tech
    we can pick from Java, Scala, Python, Go
    Notification
    RabbitMQ or Kafka


# User interface
    need to be responsive
    responsive framework like Bootstrap JS.