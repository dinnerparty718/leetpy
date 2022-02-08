'''
Nodes in a Subtree
You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
Signature
int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
Input
A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
Constraints
N and Q are the integers between 1 and 1,000,000
u is a unique integer between 1 and N
s is of the length of N, containing only lowercase letters
c is a lowercase letter contained in string s
Node 1 is the root of the tree
Output
An integer array containing the response to each query
Example
        1(a)
        /   \
      2(b)  3(a)
s = "aba"
RootNode = 1
query = [[1, 'a']]
Note: Node 1 corresponds to first letter 'a', Node 2 corresponds to second letter of the string 'b', Node 3 corresponds to third letter of the string 'a'.
output = [2]
Both Node 1 and Node 3 contain 'a', so the number of nodes within the subtree of Node 1 containing 'a' is 2.


'''


import math
# Add any extra import statements you may need here


class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

# Add any helper functions you may need here

# 1 iter queries and put node in the hash
# 2 for each node. do recrusive count


def count_of_nodes(root, queries, s):

    if not root or not queries or not s:
        return []

    nodes = {}
    s_0 = ' ' + s

    for node_val, char in queries:
        nodes[node_val] = None

    def dfs(node: Node):
        if not node:
            return

        if node.val in nodes:
            nodes[node.val] = node

        for n in node.children:
            dfs(n)

    dfs(root)

    res = []

    def count(node: Node, s: str) -> int:
        if not node:
            return 0

        cnt = 0

        if s_0[node.val] == s:
            cnt += 1

        for n in node.children:
            cnt += count(n, s)

        return cnt

    for node_val, char in queries:
        res.append(count(nodes[node_val], char))

    return res

    # Write your code here

    # These are the tests we use to determine if the solution is correct.
    # You can add your own at the bottom.


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":

    # Testcase 1
    n_1, q_1 = 3, 1
    s_1 = "aba"
    root_1 = Node(1)
    root_1.children.append(Node(2))
    root_1.children.append(Node(3))
    queries_1 = [(1, 'a')]

    output_1 = count_of_nodes(root_1, queries_1, s_1)
    expected_1 = [2]
    check(expected_1, output_1)

    # Testcase 2
    n_2, q_2 = 7, 3
    s_2 = "abaacab"
    root_2 = Node(1)
    root_2.children.append(Node(2))
    root_2.children.append(Node(3))
    root_2.children.append(Node(7))
    root_2.children[0].children.append(Node(4))
    root_2.children[0].children.append(Node(5))
    root_2.children[1].children.append(Node(6))
    queries_2 = [(1, 'a'), (2, 'b'), (3, 'a')]
    output_2 = count_of_nodes(root_2, queries_2, s_2)
    expected_2 = [4, 1, 2]
    check(expected_2, output_2)

    # Add your own test cases here
