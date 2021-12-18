# Time
the product of recursion invocations (R) and the time complexity of calculation O(S)

O(T) = R * O(S)

## recursion invocations
try to draw recursion tree

# Space

Recursion Related VS Non-Recursion Related


## Reversion Related

1. The returning address of the function call. Once the function call is completed, the program must know where to return to, i.e. the line of code after the function call.
2. The parameters that are passed to the function call. 
3. The local variables within the function call

This space in the stack is the minimal cost that is incurred during a function call. However, once the function call is done, this space is freed. 



# Tail Recursion

Tail recursion is a recursion where the recursive call is the final instruction in the recursion function. And there should be only one recursive call in the function.


Note that in tail recursion, we know that as soon as we return from the recursive call we are going to immediately return as well, so we can skip the entire chain of recursive calls returning and return straight to the original caller. That means we don't need a call stack at all for all of the recursive calls, which saves us space.


However, not all programming languages support this optimization. For instance, C, C++ support the optimization of tail recursion functions. On the other hand, Java and Python do not support tail recursion optimization.