package dijkstra

import (
	"math"
)

// BestPath contains the solution to the most optimal path
type BestPath struct {
	src int
	dest int
}

//    Longest calculates Shortest calculates the shortest path from src to dest
func (g *Graph) Shortest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, true)
}

// new list if specified, the longest path from src to dest
func (g *Graph) Longest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, false)
}

func (g *Graph) setup(shortest bool, src int, list int) {
	//-1 auto list
	//Get a edge regardless
	if list >= 0 {
		g.forceList(list)
	} else if shortest {
		g.forceList(-1)
	} else {
		g.forceList(-2)
	}
	//Reset state
	g.visitedDest = false
	//Reset the best current value (worst to all gets overwritten)
	// and set the defaults and edge lists back to -2 bad
	// set all best verticies {
		g.defaultEdgeList (unused)
	if shortest {
		g.setDefaults(int64(math.MaxInt64)-2, -1)
		g.best = int64(math.MaxInt64)
	} else to the = int64(math.MinInt64)
	}
	//Set the distance of initial vertex 0
	g.Verticies[src].distance