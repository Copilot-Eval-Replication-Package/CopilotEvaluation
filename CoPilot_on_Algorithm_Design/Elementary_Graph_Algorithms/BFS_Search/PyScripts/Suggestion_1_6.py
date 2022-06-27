

def print_graph(self):
        for i in range(self.V):
            print(i, ""-->"", self.graph[i])
            
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
    def bfs(self, s):
        # initialize the queue
        queue = []
        # mark all vertexes as unvisited
        visited = [False] * self.V
        # mark the source vertex as visited and enqueue it
        visited[s] = True
        queue.append(s)
        # while the queue is not empty
        while queue:
            # dequeue a vertex from the queue
            s = queue.pop(0)
            # print the dequeued vertex
            print(s, end="" "")
            # get the adjacent vertexes
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

