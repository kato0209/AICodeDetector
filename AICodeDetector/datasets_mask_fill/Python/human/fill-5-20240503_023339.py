# Using a Python dictionary to act as node list
graph = { '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function to go through the graph 
 in visited:  if node not         print (node)
       visited.add(node)
        for neighbour in graph[node]:
     dfs(visited, graph,"7")
print ("Here      dfs(visited, graph, neighbour)

# a simple graph, this is the Depth-First Search")
dfs(visited, graph, '5')