"""
Created on Wed Dec 26 13:41:50 2022

@author: Ксения
"""

from collections import deque


def generate_graph(num):
    new_graph = {}

    for i in range(num):
        new_graph[i] = tuple(j for j in range(num) if j != i)

    return new_graph


def walk_graph(graph, start, finish):
    length = len(graph)
    parent = [None] * length
    is_visited = [False] * length

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()

        if current == finish:
            break

        for vertex in graph[current]:
            if not is_visited[vertex]:
                is_visited[vertex] = True
                parent[vertex] = current
                deq.appendleft(vertex)
    else:
        return f"Из вершины {start} невозможно попасть в вершину {finish}"

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return list(way)


amount = int(input("Количество вершин в графе: "))
vertex_start = int(input("Введите вершину начала: "))
vertex_end = int(input("Введите вершину конца: "))

gen = generate_graph(amount)

print(walk_graph(gen, vertex_start, vertex_end))
