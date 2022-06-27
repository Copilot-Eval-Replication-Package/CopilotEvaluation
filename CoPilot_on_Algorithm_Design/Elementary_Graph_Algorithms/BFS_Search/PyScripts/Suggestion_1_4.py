

def print_graph(self):
        for i in range(self.V):
            print(i, ""-->"", self.graph[i])
            
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
    def bfs(self, s):
        # create a queue and enqueue the source vertex.
        queue = []
        queue.append(s)
        # mark the source vertex as visited.
        visited = [False] * self.V
        visited[s] = True
        # loop until the queue is empty.
        while queue:
            # dequeue a vertex from the queue.
            s = queue.pop(0)
            # print the vertex.
            print(s, end = "" "")
            # loop through the adjacency list of the dequeued vertex.
            for i in self.graph[s]:
                # if the adjacent vertex is not visited, enqueue it and mark it as visited.
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

