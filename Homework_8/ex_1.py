"""
Created on Wed Dec 26 13:41:50 2022

@author: Ксения
"""


s = int(input("Введите количество друзей: "))

graph = []
for i in range(s):
    row = [1] * s
    row[i] = 0
    graph.append(row)

print(graph)

handshakes = 0
for row in graph:
    for i in row:
        handshakes += i

print(f"Всего рукопожатий {handshakes}")
