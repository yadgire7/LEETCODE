'''
This file includes python implementation of graphs.
1. Creation of a graph
2. Traversal Techniques
3. Applications(algorithms)
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # function to insert an edge in the graph(undirected)
    # Note that if you are considering a directed graph, then the edge goes from u to v
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def getVertices(self):
        u_nodes = list(self.graph.keys())
        v_nodes = sum(list(self.graph.values()), [])
        return set(u_nodes + v_nodes)
    
    def getLength(self):
        vertices = self.getVertices()
        return len(vertices)
    
    '''
    BFS: Breadth First Search
    This algorithm searches for all the nodes at a given level and then moves to the level below 
    '''
    def BFS(self, start):
        # start: starting node to perform BFS
        visited = set()
        # create a queue to keep track of the to be traversed
        queue = []
        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node)
            for child in self.graph[node]:
                if child not in visited:
                    # print(child)
                    queue.append(child)
                    visited.add(child)
        
    

if __name__ == '__main__':
    g = Graph()
    g.addEdge('A', 'B')

    g.addEdge('A', 'E')
    g.addEdge('B', 'D')
    g.addEdge('B', 'C')

    vertices = g.getVertices()
    print(f"Vertices: {vertices}")
    g.BFS('B')
