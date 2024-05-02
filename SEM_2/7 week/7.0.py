from heapq import *
def read_graph_as_edges_w():
    n = int(input('!!!Внимрние заполнять в порядке:: ВЕС -- НАЧАЛО -- КОНЕЦ'))
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph

'''def has_cycle_deep(node, vis=set(), is_cyc=set()): #извините но без перебора он выдаёт неверное значение если у одной вешины два предка и одного из предков предок другой предок
    if node in is_cyc:
        return True
    elif node in vis:
        return False
    vis.add(node)
    is_cyc.add(node)

    for neigh in graph[node]:
        if has_cycle_deep(neigh, vis, is_cyc):
            return True
    is_cyc.remove(node)
    return False
def has_cycle(graph):
    for node in graph:
        if has_cycle_deep(node):
            return True
    return False'''

def read_graph_as_neigh_list_w(gr):
    edge_list = gr
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict


def read_graph_as_neigh_matrix_w():
    edge_list = read_graph_as_edges_w()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix


def print_matrix_w(matrix):
    for line in matrix:
        print(*line)


def DFS_w(graph, v, visited=[]):
    # print(v)
    visited.append(v)
    for neigh in graph[v][0]:
        if neigh not in visited:
            DFS_w(graph, neigh, visited)

def bfs_w(graph, v):
    visited = []
    queue = []
    d = {}
    for keys in graph.keys():
        d[keys] = 100000
    visited.append(v)
    queue.append(v)
    d[v] = 0

    while queue:
        u = queue.pop(0)
        print(u, end=" ")

        for neighdour in graph[u]:
            if neighdour not in visited:
                visited.append(neighdour)
                queue.append(neighdour)
                d[neighdour] = d[u] + 1
    return d


def dijkstra(graph, v):
    visited = []
    d = {}
    end = []
    for keys in graph.keys():
        d[keys] = 100000
    visited.append([0, v])
    d[v] = 0
    visited.sort()
    c = visited.pop(0)
    for neigh in graph[c[1]]:
        if neigh[0] not in end:
            if d[c[1]] + neigh[1] < d[neigh]:
                d[neigh[0]] = (d[c[1]] + neigh[1])
            visited.append(neigh[::-1])
    return d

def FW(graph):
    V = len(graph)
    d = [[1000000 for i in range(V)] for j in range(V)]
    nxt = [[-1 for i in range(V)] for j in range(V)]

    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                d[i][j] = graph[i][j]
                nxt[i][j] = j
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]
    return d, nxt
def pth(i,j, nxt):
    p = [i]
    while nxt[i-1][j-1] + 1 != j:
        i = nxt[i-1][j-1] + 1
        p.append(i)
    p.append(j)
    return p
def kruskal(graph): # read_graph_as_edges
    g = graph
    g.sort()
    tree_v = set()
    tree_e = []
    for e in g:
        if e[1] not in tree_v or e[2] not in tree_v:
            tree_v.add(e[1])
            tree_v.add(e[2])
            tree_e.append(e)
        else:
            continue
    return tree_e

def prim(graph):

    v = 1
    tmp = list(graph[v])
    h = []

    for e in tmp:
        h.append([e[2], e[1], v])
    heapify(h)
    tree_v = set([v])
    tree_e = []

    while h:
        e_min = heappop(h)
        if e_min[2] not in tree_v:
            tree_v.add(e_min[2])
            for e in graph[e_min[2]]:
                t = [e[2], e[1]]
                heappush(h, (list(t) + [e_min[1]]))
            v = e_min[2]
            tree_e.append(e_min)
        else:
            continue
    return tree_e


def find_MST(graph_list):
    gr = graph_list
    ans = {tuple(i): 'Always' for i in gr}
    weight = set(i[0] for i in gr)
    div_l = {i: [] for i in weight}
    gr.sort()
    j = 0
    for i in weight:
        f = []
        while j < len(gr) and i == gr[j][0]:
            f.append(gr[j])
            j += 1
        div_l[i] = tuple(f)

    inter = []
    for lis in div_l.values():
        inte = []
        for ver in lis:
            mst = kruskal(inter + [ver])
            if ver not in mst:
                ans[tuple(ver)] = 'Never'
            else:
                inte.append(ver)
        inter = inter + inte
    ve = set()
    for i in ans.keys():
        if ans[i] == 'Always':
            ve.add(i)
    mst = kruskal(graph_list)
    for i in ans.keys():
        if list(i) not in mst and ans[i] != 'Never':
            ans[i] = 'at least one'
    print(ans)




graph_list = read_graph_as_edges_w()
graph = read_graph_as_neigh_list_w(graph_list)
'''
5
1 2 2
1 3 4
2 3 10
3 4 60
1 4 3
3
100 1 2
1 2 3
1 3 1
'''
'''G = read_graph_as_neigh_matrix_w()
D, P = FW(G)
P = pth(1, 3, P)
for line in D:
    print(line)
print(P)'''
print(kruskal(graph_list))
find_MST(graph_list)
