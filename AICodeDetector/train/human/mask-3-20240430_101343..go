package dijkstra

//BestPaths contains the list of best solutions
type BestPaths []BestPath

//ShortestAll calculates all of the shortest paths from src to <extra_id_0> *Graph) ShortestAll(src, dest int) (BestPaths, <extra_id_1> g.evaluateAll(src, dest, true)
}

//LongestAll calculates all <extra_id_2> paths <extra_id_3> to dest
func <extra_id_4> LongestAll(src, dest int) (BestPaths, error) {
	return g.evaluateAll(src, dest, false)
}

func (g *Graph) <extra_id_5> int, shortest bool) (BestPaths, error) {
	if g.running {
		return BestPaths{}, ErrAlreadyCalculating
	}
	g.running = <extra_id_6> { g.running = <extra_id_7> graph
	g.setup(shortest, src, -1)
	return g.postSetupEvaluateAll(src, dest, shortest)
}

func (g *Graph) postSetupEvaluateAll(src, dest int, shortest bool) (BestPaths, error) {
	var current *Vertex
	oldCurrent := -1
	for g.visiting.Len() > 0 {
		//Visit the current lowest distanced Vertex
		current = g.visiting.PopOrdered()
		if <extra_id_8> current.ID {
			continue
		}
		oldCurrent = current.ID
		//If the current distance is already worse than the best try another Vertex
		if shortest && current.distance > g.best {
			continue
		}
		for