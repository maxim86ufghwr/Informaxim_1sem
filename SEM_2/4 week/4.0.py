def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return  graph
def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {} #dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
        else:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict

def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)


    res_matrix = [[0 for i in range(V_num)]for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] -1
        index_2 = edge[1]-1
        res_matrix[index_1][index_2] = 1

    return res_matrix
def print_matrix(matrix):
    for line in matrix:
        print(*line)
def DFS(graph, v, visited=[]):
    print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh, visited)

def has_cycle_util(node, vis=set(), is_cyc=set()): #извините но без перебора он выдаёт неверное значение если у одной вешины два предка и одного из предков предок другой предок
    if node in is_cyc:
        return True
    elif node in vis:
        return False
    vis.add(node)
    is_cyc.add(node)

    for neigh in graph[node]:
        if has_cycle_util(neigh, vis, is_cyc):
            return True
    is_cyc.remove(node)
    return False
def has_cycle(graph):
    for node in graph:
        if has_cycle_util(node):
            return True
    return False
def DFS_stack(gra, v, visited = []):
    print(v)
    stack = []
    visited.append(v)
    stack.append(v)
    while stack:
        v = stack.pop()
        for neigh in gra[v]:
            if neigh not in visited:
                visited.append(neigh)
                stack.append(neigh)
                print(neigh)
                break
def topologikal(gr, v, pr = ''):
    visited = []
    stack = []
    while len(stack) < len(gr.keys()):
        visited.append(v)
        while visited:
            c = 0
            for neigh in gr[v]:
                if neigh not in stack:
                    c = 1
                    break
            if c == 0:
                stack.append(v)
                visited.remove(v)
                if len(visited) != 0:
                    v = visited[len(visited)-1]
                else:
                    for el in gr.keys():
                        if el not in stack:
                            v = el
                            visited.append(v)
            else:
                for neigh in gr[v]:
                    if neigh not in stack:
                        v = neigh
                        visited.append(v)
                        break
    if pr == 'print':
        print(stack[::-1])
    return stack[::-1]
def is_v_vertice_of_u(gr, how_requests):
    stack = topologikal(gr, 1)
    for i in range(how_requests):
        v, u = map(int, input().split())
        if stack.index(v) < stack.index(u):
            print(f'{u} is NOT contain vertice of {v}')
        else:
            if how_ways(gr, u, v)>0:
                print(f'{u} is contain vertice of {v}')
            else:
                print(f'{u} is NOT contain vertice of {v}')
def how_ways(gr, start, fin):
    stack = topologikal(gr, 1)
    neigh = [i for i in gr[start]]
    in_f = stack.index(fin)
    vis = []
    count = 0
    while neigh:
        t = neigh[len(neigh)-1]
        if t == fin:
            count += 1
        elif stack.index(t) < in_f:
            vis.append(t)
            for el in gr[t]:
                if el not in vis and stack.index(el) <= in_f:
                    neigh.append(el)
        neigh.remove(t)
    return count

graph = read_graph_as_neigh_list()
DFS(graph, 1)
print(graph)
print(has_cycle(graph))
DFS_stack(graph, 1)
topologikal(graph, 1, 'print')
is_v_vertice_of_u(graph, 2)
start, fin = map(int, input('начало и конец: ').split())
print(how_ways(graph, start, fin))
