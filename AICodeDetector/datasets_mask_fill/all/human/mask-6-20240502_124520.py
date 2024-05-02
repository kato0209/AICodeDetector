# Using a Python dictionary to act as an adjacency list
graph = {
 <extra_id_0> : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' <extra_id_1>  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def <extra_id_2> node):  #function for dfs 
    if node not in visited:
        print <extra_id_3>   <extra_id_4>   visited.add(node)
   <extra_id_5>    for neighbour in graph[node]:
            dfs(visited, <extra_id_6> Driver Code
print("Following <extra_id_7> Depth-First Search")
dfs(visited, graph, '5')