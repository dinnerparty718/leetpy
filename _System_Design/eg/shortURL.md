

# URL

your URL should never be longer than 2,048 characters.

first page of google 40 - 100


Why do we need URL shortening


functional
- Url -> shorter unique 
- type short url, service redirect to content original url
- optionally, pick their own url
- expiration ?

non-functional
- HA, if service down, can't redirect
- url redirect should happen in real time, low latency
- short url should not be guessable

extended requirement




read-write ratio 100/1
# how many new short URL generated


# a = 500_000_000/  ( 30* 24 * 3600 )



[link] https://jerrynsh.com/i-built-my-own-tiny-url/


[bytecounter] https://mothereff.in/byte-counter



80-20 rule, meaning 20% of URLs generate 80% of traffic, we would like to cache these 20% hot URLs.


Assuming 500 million new URLs per month and 100:1 read:write ratio, 

[link] https://www.educative.io/module/lesson/grokking-system-design-interview/xVZVrgDXYLP#1.-Why-do-we-need-URL-shortening?



createURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_date=None)


# api_dev_key use to throttle 

The API developer key of a registered account. throttle users based on their allocated quota


Using base64 encoding, a 6 letters long key would result in 64^6 = ~68.7 billion possible strings. -> sufficient
Using base64 encoding, an 8 letters long key would result in 64^8 = ~281 trillion possible strings.

make sure unique
Key Generation Service (KGS) that generates random six-letter strings beforehand and stores them in a database (let’s call it key-DB). 

How to handle concurrency

What would be the key-DB size? With base64 encoding, we can generate 68.7B unique six letters keys. If we need one byte to store one alpha-numeric character, we can store all these keys in:

6 (characters per key) * 68.7B (unique keys) = 412 GB.



# todo

to generate key ahead of time
or dynamically assign values

Using Redis as an LRU cache. automatically evicted
