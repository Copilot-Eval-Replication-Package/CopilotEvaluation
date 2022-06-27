

    def dfs(self, s):
            visited = [False] * self.V
            self.dfs_util(s, visited)
    
    def dfs_util(self, s, visited):
            visited[s] = True
            print(s, end="" "")
            for i in self.graph[s]:
                if visited[i] == False:
                    self.dfs_util(i, visited)
    
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
    def dfs_path(self, s, d):
            visited = [False] * self.V
            stack = []
            stack.append(s)
            visited[s] = True
            while stack:
                s = stack.pop()
                print(s, end="" "")
                if s == d:
                    return True
                for i in self.graph[s]:
                    if visited[i] == False:
                        stack.append(i)
                        visited[i] = True
            return False
    
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
    def dfs_path_util(self, s, d, visited, path):
            visited[s] = True
            path.append(s)
            if s == d:
                return True
            for i in self.graph[s]:
                if visited[i] == False:
                    if self.dfs_path_util(i, d, visited, path):
                        return True
            path.pop()
            return False
    
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
    def dfs_path_util_print(self, s, d, visited, path):
            visited[s] = True
            path.append(s)
            print(s, end="" "")
            if s == d:
                return True
            for i in self.graph[s]:
                if visited[i] == False

