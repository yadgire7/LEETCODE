# create an adjecency matrix, 2 sets viz: visited, unvisited, and a distance graph
import math

adj = [[0,5,3,6,0,0],
       [5,0,8,0,0,0],
       [3,8,0,0,0,11],
       [6,0,0,0,9,0],
       [0,0,0,9,0,12],
       [0,0,11,0,12,0]]

visited = set()

unvisited = set(range(6))
print(unvisited)

start = 0
distance = {}
for v in unvisited:
    if v== start:
        distance[v] = 0
    else:
        distance[v] = math.inf

visiting = unvisited.pop(start)
for 

