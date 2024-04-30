package brevity

import "fmt"

// Graph structure and NewGraph functions are mostly identical for brevity; see the previous snippet.

// FindShortestPath finds and prints the shortest path between each of the start and
// end vertices.
func (g *Graph) FindShortestPath(start, end int) {
	visited := make(map[int]bool)
	predecessor := make(map[int]int)
	queue := []int{start}
	found := false

	for len(queue) > 0 && !found {
		vertex := queue[0]
		queue = queue[1:]
		for _, adjacent := range g.adjList[vertex] {
			if !visited[adjacent] {
				predecessor[adjacent] = vertex
				visited[adjacent] = true
				queue = append(queue, adjacent)
				if adjacent == end {
					found = true
					break
				}
			}
		}
	}

	if !found {
		fmt.Println("No path found")
		return
	}

	// Reconstruct the path from end to start
	path := []int{end}
	for at := end; at != start; at = predecessor[at] {
		path = append([]int{predecessor[at]}, path...)
	}

	fmt.Printf("Shortest path: %v\n", path)
}

func main() {
	// Graph initialization omitted for bRevity: the graph is initialized and edges are added as in the snippet.

	start := 0
	end := 4
	fmt.Printf("Finding the shortest path