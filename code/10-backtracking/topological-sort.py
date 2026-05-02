"""
Given a directed acyclic graph (DAG), perform a topological sort on the graph.
"""
from collections import deque


def topological_sort1(adj_list, n):
    indegress = [0] * n
    for node in range(n):
        for neighbour in adj_list[node]:    
            indegress[neighbour] += 1
    
    queue = deque()
    order = []
    for degree in indegress:
        if degree == 0:
            queue.append(degree)
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in adj_list[node]:
            indegress[neighbour] -= 1
            if indegress[neighbour] == 0:
                queue.append(neighbour)
    return order

def topological_sort(adj_list, n):
    indegree = [0] * n
    for u in adj_list:
        for v in adj_list[u]:
            indegree[v] += 1
    # enqueue nodes with indegree 0
    queue = deque([u for u in range(n) if indegree[u] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        
        for v in adj_list.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == n else []


if __name__ == "__main__":
    edges = {
        0: [1], 
        1: [2, 3], 
        2: [], 
        3: [2, 4], 
        4: []
    }
    n = 5 
    print(topological_sort(edges, n))
    