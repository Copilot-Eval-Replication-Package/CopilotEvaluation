vertices=[1,2,3,4]
graph = [[0 for column in range(len(vertices))]
                      for row in range(len(vertices))]

print(graph)

graph2 = [None] * len(vertices)
for i in range(len(vertices)):
    graph2[i] = []


print(graph2)
