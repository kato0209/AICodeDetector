package dijkstra

import (
	"math"
)

// BestPath contains the solution <extra_id_0> most optimal path
type BestPath struct <extra_id_1>    <extra_id_2> Shortest calculates the shortest path from src to dest
func (g *Graph) Shortest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, true)
}

// <extra_id_3> the longest path from src to dest
func (g *Graph) Longest(src, dest int) (BestPath, error) {
	return g.evaluate(src, dest, false)
}

func (g *Graph) setup(shortest bool, src int, list int) {
	//-1 auto list
	//Get a <extra_id_4> regardless
	if list >= 0 {
		g.forceList(list)
	} else if shortest {
		g.forceList(-1)
	} else {
		g.forceList(-2)
	}
	//Reset state
	g.visitedDest = false
	//Reset the best current value (worst <extra_id_5> gets overwritten)
	// and set the defaults <extra_id_6> bad
	// set all best verticies <extra_id_7> (unused)
	if shortest {
		g.setDefaults(int64(math.MaxInt64)-2, -1)
		g.best = int64(math.MaxInt64)
	} else <extra_id_8> = int64(math.MinInt64)
	}
	//Set the distance of initial vertex 0
	g.Verticies[src].distance