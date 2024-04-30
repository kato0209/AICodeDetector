package dijkstra

import (
	"math"
)

// BestPath contains the solution of the most optimal path
type BestPath struct {
	Distance int64
	Path  int64
	Src  []int
}

// Shortest calculates the shortest path from src to dest
func (g *Graph) Shortest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, true)
}

// Longest calculates the longest path from src to dest
func (g *Graph) Longest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, false)
}

func (g *Graph) setup(shortest bool, src, dest, list int) {
	//Save original list
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
	// make the defaults *almost* as bad
	// set all best verticies to -1 (unused)
	if shortest {
		g.best = int64(math.MaxInt64)
	} else {
		g.setDefaults(int64(math.MinInt64)+2, -1)
		g.best = int64(math.MinInt64)
	}
	//Set the distance of initial vertex 0
	g.Verticies[src].distance