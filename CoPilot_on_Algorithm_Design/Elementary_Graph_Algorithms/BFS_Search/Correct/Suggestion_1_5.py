


    # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
def bfs(self, s):
    # create an empty queue.
    queue = []
        # create a visited list.
    visited = [False] * self.V
        # mark the source vertex as visited.
    visited[s] = True
        # enqueue the source vertex.
    queue.append(s)
        # while the queue is not empty.
    while queue:
        # dequeue a vertex.
        s = queue.pop(0)
            # print the vertex.
        print(s, end=" ")
            # get the adjacent vertexes.
        for i in self.graph[s]:
            # if the adjacent vertex is not visited.
            if visited[i] == False:
                # mark it as visited.
                visited[i] = True
                    # enqueue the adjacent vertex.
                queue.append(i)

