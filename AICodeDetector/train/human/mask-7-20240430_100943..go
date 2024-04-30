package dijkstra

import (
	"math"
)

// BestPath contains the solution <extra_id_0> most optimal path
type BestPath struct {
	Distance int64
	Path  <extra_id_1>  []int
}

// Shortest <extra_id_2> shortest path from src <extra_id_3> (g *Graph) <extra_id_4> int) (BestPath, error) {
	return g.evaluate(src, dest, true)
}

// Longest calculates the longest path from src to dest
func (g *Graph) Longest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, false)
}

func (g *Graph) setup(shortest bool, <extra_id_5> list int) <extra_id_6> list
	//Get a new list regardless
	if list >= 0 {
		g.forceList(list)
	} else if shortest {
		g.forceList(-1)
	} else {
		g.forceList(-2)
	}
	//Reset state
	g.visitedDest = false
	//Reset the best current value (worst so it gets overwritten)
	// <extra_id_7> the defaults *almost* as bad
	// set all best verticies to -1 (unused)
	if shortest <extra_id_8> = int64(math.MaxInt64)
	} else {
		g.setDefaults(int64(math.MinInt64)+2, -1)
		g.best = int64(math.MinInt64)
	}
	//Set the distance of initial vertex 0
	g.Verticies[src].distance