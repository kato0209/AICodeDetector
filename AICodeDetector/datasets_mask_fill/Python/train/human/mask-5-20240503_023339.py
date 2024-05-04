# Using a Python dictionary to act as <extra_id_0> list
graph = <extra_id_1> '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function <extra_id_2> 
 <extra_id_3>  if node not <extra_id_4>        print (node)
   <extra_id_5>    visited.add(node)
        for neighbour in graph[node]:
     <extra_id_6>      dfs(visited, graph, neighbour)

# <extra_id_7> is the Depth-First Search")
dfs(visited, graph, '5')