### A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.


## to implement startswith() which hashmap/hashset can't do


# Time O(N)
# Space O(M*N*K)  k = 26



find max xor, exclusive or


## Algorithm

To summarise, now one could

- Insert a number into Bitwise Trie.
- Find maximum XOR of a given number with all numbers that have been inserted so far.

That's all one needs to solve the initial problem:

- Convert all numbers to the binary form.
- Add the numbers into Trie one by one and compute the maximum XOR of a number to add with all previously inserted. Update maximum XOR at each step.
- Return max_xor.




## example


1. Autocomplete
2. spell checker (add and serach word, wordDictionary)
3. Accelerate DFS. terminate early ?
4. Store other Data type
   1. max XOR 1,0
   2. IP routing longest prefix matching




## tricks


use dict directly

use node['#'] to store additional info eg. word itself, for word index