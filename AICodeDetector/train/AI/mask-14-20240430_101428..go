package <extra_id_0> Graph structure and NewGraph <extra_id_1> for brevity; see the previous snippet.

// FindShortestPath finds and prints the shortest path between <extra_id_2> end vertices.
func (g *Graph) FindShortestPath(start, end int) <extra_id_3> make(map[int]bool)
	predecessor := make(map[int]int)
	queue := []int{start}
	found := false

	for <extra_id_4> 0 && !found {
		vertex := queue[0]
		queue = queue[1:]
		for _, adjacent := range g.adjList[vertex] {
			if !visited[adjacent] {
				predecessor[adjacent] <extra_id_5> = true
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
	// Graph initialization omitted for <extra_id_6> graph is initialized and edges are added as in <extra_id_7> snippet.

	start := 0
	end := 4
	fmt.Printf("Finding <extra_id_8> path