# Using a Python dictionary to act as an adjacency list
graph = {
 '1' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : [],  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print ('Node not visited yet.')
        if node in graph:   ()   visited.add(node)
       for neighbour in graph[node]:
            dfs(visited, graph, neighbour) # Driver Code
print("Following is Depth-First Search")
dfs(visited, graph, '5')