from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*(len(self.graph))
        # print(visited)
        # print (self.graph)
        queue = []
        queue.append(s)
        visited[s]=True
        while queue:
            # print(queue)
            # print(visited)
            s=queue.pop(0)
            print (s,)

            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print('Following is the Breadth First Traversal(starting from vertex 2)')
g.BFS(2)
