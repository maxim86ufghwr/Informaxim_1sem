def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph

def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_w()
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
'''def DFS_w(graph, v, visited=[]):
    # print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS_w(graph, neigh, visited)'''
def has_cycle_w(graph, v, visited=[]):
    result = False
    visited.append(v)
    for neigh in graph[v]:

        if neigh in visited:
            result = True
            return result

        if result == False:
            result = has_cycle_w(graph, neigh, visited)

    return result
def topologicalSortUtil_w(v, visited, stack=[], i=1):
    visited[v] = True
    for v in graph:
        if visited[i] == False:
            topologicalSortUtil_w(i, visited, stack)
            stack.append(v)
        i += 1


def topologicalSort_w(graph):
    if has_cycle_w(graph, v=1) == False:
        visited = [False] * (len(graph) + 1)
        stack = []
        for i in range(len(graph)):
            if visited[i] == False:
                topologicalSortUtil_w(i, visited, stack)
        return stack
    else:
        t = 'Невозможно выполнить из-за присутсвия цикла в данном графе...'
        return t


def road_in_v_from_u_w(graph, v, u):
    Topolog_list = topologicalSort_w(graph)
    if type(Topolog_list) == str:
        return Topolog_list
    else:
        First_index = Topolog_list.index(v)
        Second_index = Topolog_list.index(u)
        answer = 0
        visited = [v]
        if First_index < Second_index:
            return answer
        else:
            for i in graph:
                if i in visited:
                    answer += 1
                else:
                    pass
                visited.append(i)
            return answer

def father_n_w(graph, v, u):
    result = road_in_v_from_u_w(graph, v, u)
    if result > 0:
        return True
    else:
        return False

def bfs_w(graph, v):
    visited = []
    queue = []
    d = {}
    for keys in graph.keys():
        d[keys] = float('infinity')
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
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 10000000000000000000

    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])
    return d

def dijkstra_max(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 100000000000000
    d[v] = 10000000000
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if max(d[c[1]], neigh[1]) < d[neigh[0]]:
                    if d[c[1]] < 10000000000:
                        d[neigh[0]] = max(d[c[1]], neigh[1])
                    else:
                        d[neigh[0]] = neigh[1]
                visited.append(neigh[::-1])
    d[v] = 0
    return d
def dijkstra_multi(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 100000000000000
    d[v] = 1
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] * neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] * neigh[1])
                visited.append(neigh[::-1])
    d[v] = 0
    return d
def dijkstra_conk(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 100000000000000
    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if int(str(d[c[1]]) + str(neigh[1])) < d[neigh[0]]:
                    d[neigh[0]] = int(str(d[c[1]]) + str(neigh[1]))
                visited.append(neigh[::-1])
    return d
def dijkstra_min(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 0
    d[v] = 100000000000000000
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if min(d[c[1]], neigh[1]) > d[neigh[0]]:
                    if d[c[1]] > 0:
                        d[neigh[0]] = min(d[c[1]], neigh[1])
                    else:
                        d[neigh[0]] = neigh[1]
                visited.append(neigh[::-1])
    d[v] = 0
    return d

graph = read_graph_as_neigh_list_w()
#DFS_w(graph, 1)
# print(has_cycle(graph, 1))
# print(topologicalSort(graph))
#print(graph)
#print_matrix_w(read_graph_as_neigh_matrix_w())
# print(road_in_v_from_u(graph, 7, 6))
# print(father_n(graph, 6 , 7))
#d = bfs_w(graph, 1)
#print(d)
'''
8
1 4 6
1 2 1
3 2 2
2 5 3
2 6 1
5 3 1
6 2 2
6 4 1
5
1 2 1
2 4 1
4 3 1
2 3 4
1 3 6
'''
print(dijkstra(graph, 1))
print('Максимум', dijkstra_max(graph, 1))
print('Умножение', dijkstra_multi(graph, 1))
print('конкатенация', dijkstra_conk(graph, 1))
print('Минимум', dijkstra_min(graph, 1))
'''G_exp = read_graph_as_neigh_matrix_w()
D = FW(G_exp)
print(D)'''