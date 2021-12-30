
# Time O(α(N)) -> O(1)
#! ultimate implementation
class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:

            # add y to x
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                # add x to y
                self.root[rootX] = rootY
            else:
                # equal height
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


# quck union
class UnionFind_Quick_Union:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]

    # quick union
    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX

            # return the root node

    def find(self, x: int):
        # return the grand grand parent
        while x != self.root[x]:
            x = self.root[x]

        return x

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class UnionFind_Quick_Find:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]

    # quick find
    def find(self, x: int):
        return self.root[x]

    # go through entire array and update root

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)

# optimiztion of quick union. record the height of the tree


class UnionFind_Rank:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class UnionFind_Compact:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]

    # quick union
    # O(log(n)) based on find
    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX

    # O(log(n))

    def find(self, x: int):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # O(log(n)) depends on find
    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


uf = UnionFind(10)


# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true

print(uf.root)
