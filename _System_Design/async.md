Tomcat server
    200 thread

210 , extra 10 clients need to wait



JS does not have multi-thread
JS is single-threaded


Node will not wait
    single thread but non-blocking


    non-blocking i/o
    nodesJS has workers
    
    behind the scene libuv uses system kerel has multiple thread


node for I/O intensive work
    NOT for CPU intensive work


## Event Loop

[link] https://www.youtube.com/watch?v=8zKuNo4ay8E

# Call Stack  , event loop and callback queue, micro stask queue (higer priority) 

call stack inside JS Engine (JS Engine inside browser)

event loop constantly check call stack, wait for it's empty
    if not empty, push it to the call stack

micro task queue
    what goes into 
        1. promises go to Micro Task queue ->  fetch cb 
        2. mutation observer
    can add more items to itself, cause "Startvation"
   

d
c
a() -> line by line
GEC(Global Exection Context, line by line)


a = () =>{
 console.log('a')
}

a()

console.log('end')


# console
a
end

pop a
pop GEC


Broswer 
    JS Engine
    has local storage
    Timer
    https://
    page
    bluetooth
    location

web APIs -> super power 
# window global object in the brower
    don't need window.console.log() if it's in the global scope
    
# process global object in NodeJS

setTimeout() -> not part of javascript
DOM APIs document.*
fetch()
localStorage
console console.log is not javascript LOL
location



