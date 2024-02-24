class FenTree:
    def __init__(self, data: list):
        ln = len(data)
        self.data = data
        self.b = []
        self.bins = []
        for i in range(ln):
            self.b.append(sum(self.data[i & (i+1):i+1]))
            self.bins.append(i & (i+1))
            print(i & (i+1), i)
    def update(self, pos, num) -> None:
        old = self.data[pos]
        difference = num - old
        self.data[pos] += difference
        while pos <= len(self.data):
            self.b[pos] += difference
            pos = pos | pos+1
def Su(tree, n) -> float:
    if tree.bins[n] != 0:
        return tree.b[n] + Su(tree, tree.bins[n]-1)
    else:
        return tree.b[n]

def Sum(tree, l: int, r: int):
    return Su(tree, r) - Su(tree, l-1)

tree = FenTree([1,2,3,4,5,6,7,8])
print(tree.data, tree.b)
print(Sum(tree, 1, 5))
tree.update(5, 99)
print(tree.data, tree.b)
print(Sum(tree, 1, 5))