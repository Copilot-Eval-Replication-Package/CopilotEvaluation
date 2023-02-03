

def dfs_cycle(self, s):
        self.visited[s] = True
        for i in self.graph[s]:
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return True
            elif self.visited[i] == True:
                return True
        return False

    # create a function that checks if two vetrices are reachable from each other. if they are the  function returns true otherwise false.
def is_reachable(self, s, d):
    self.visited = [False] * self.V
    if self.dfs_cycle(s):
        return False
    else:
        return True if self.dfs_cycle(d) else False

   