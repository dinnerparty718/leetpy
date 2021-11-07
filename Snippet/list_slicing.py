# input '0000'
# output making one move. each position 2 value 2 * 4 = 8 combinations

def neighbors(node: str) -> str:
    for i in range(4):
        x = int(node[i])
        for d in (-1, 1):
            y = (x + d) % 10
            yield node[:i] + str(y) + node[i+1:]


for i in neighbors('0000'):
    print(i)
