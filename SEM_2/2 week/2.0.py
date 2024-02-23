import numpy as np
class SumTree:
    def __init__(self, data: list):
        ln = len(data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = data
        else:
            self.data = data
            lb = int(lb) + 1
            for i in range(ln, 2 ** lb):
                self.data.append(0)

        self.tree = [0 for i in range(len(self.data) - 1)] + self.data
        self.calc_tree()

    def calc_tree(self) -> None:
        for i in range(len(self.tree) + 1, 2, -2):
            s1 = self.tree[i - 2]
            s2 = self.tree[i - 3]
            sm = s1 + s2
            self.tree[(i - 4) // 2] = sm
    def update(self, pos, num):
        upd = self.tree[len(self.tree)//2:len(self.tree)]
        upd.insert(pos, num)
        ln = len(upd)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = upd
        else:
            self.data = upd
            lb = int(lb) + 1
            for i in range(ln, 2 ** lb):
                self.data.append(0)

        self.tree = [0 for i in range(len(self.data) - 1)] + self.data
        self.calc_tree()
def Sum(tree, l: int, r: int):
    def tree_sum(l: int, r: int, tl=0, tr=len(tree.data) - 1):  # len(tree.data)-1
        sum = 0
        tm = (tl + tr + 1) // 2

        # если встретили лист
        if tr == tl:
            return tree.data[tm]

        # если отрезок на который смотрим полностью внутри запрашиваемого
        if l <= tl and r >= tr:
            index1 = (len(tree.data) - 1) + tr  # 14
            index2 = (len(tree.data) - 1) + tl + 1  # 8
            while index1 != index2:
                if index1 > 6:
                    index1 = max((index1 - 2) // 2, 0)
                    index2 = max((index2 - 2) // 2, 0)
                else:
                    index1 = max((index1 - 1) // 2, 0)
                    index2 = max((index2 - 1) // 2, 0)
            if tl + 1 == tr:
                return tree.tree[(index1 - 2) // 2]
            else:
                return tree.tree[index1]

        # если надо, спускаемся по дереву дальше
        go_left = l < tm
        go_right = r >= tm
        if go_left:
            sum += tree_sum(l, r, tl=tl, tr=tm - 1)
        if go_right:
            sum += tree_sum(l, r, tl=tm, tr=tr)

        return sum
    return tree_sum(l, r)
# [1,2,3,4,5,6,7,]
# 0 1 2 3 4 5 6

tree = SumTree([1,2,3,4,5,6,7,8])
print(tree.tree)
print(Sum(tree,0,5))
tree.update(6, 99)
print(tree.tree)