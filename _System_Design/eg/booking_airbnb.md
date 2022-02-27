https://www.youtube.com/watch?v=YyOXt2MEkv4

### hotel service

cache? not worthy

## API

POST    /hotel
GET     /hotel/id
PUT     /hotel/id
PUT     /hotel/id/room/id


## Hotel DB

# table

room facility -> many to many

hotel
    id, name, locality_id
hotel_facility

room
    price_min, price_max
room_facility 
facility
locality


### bokking service


## API
POST /book
    user_id, room_id, quantity, start_date, end_date
1. check in available rooms
2. insert in booking && reduce in av_rooms 
   1. block tmp
3. put in redis with ttl (block in 10 min)
   1. redis call back
   2. key expired, get notification
4. put in kafka
5. redirect to payment

## booking DB

available_room
    room_id, date, initial_qty, avaliable_qty (>0)  constraint

booking 
    id
    r_id, u_id, start_dt,end, num_of_room
    status : [reserved, booed, cancelled, completed]
    invoice_id

transaction
    available_room
    booking

scenario

1. payment success
2. payment failed -> cancelled, no invoice, available_qty +=1
3. key expired -> call back from redis -> cancelled, no invoice, available_qty +=1
4. 3 then 1 -> 
   1. revert payment
   2. auto book if available