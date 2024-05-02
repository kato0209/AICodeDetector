package dijkstra

//BestPaths contains a collection of best solutions
type BestPaths []BestPath

//ShortestAll calculates all of the shortest paths from src to dest
func (g *Graph) ShortestAll(src, dest int) (BestPaths, error) {
	return g.evaluateAll(src, dest, true)
}

//LongestAll calculates all the longest paths from src to dest
func (g *Graph) LongestAll(src, dest int) (BestPaths, error) {
	return g.evaluateAll(src, dest, false)
}

func (g *Graph) evaluateAll(src, dest int, shortest bool) (BestPaths, error) {
	if g.running {
		return BestPaths{}, ErrAlreadyCalculating
	}
	g.running = true
	defer func() { g.running = false }()
	//Setup graph
	g.setup(shortest, src, -1)
	return g.postSetupEvaluateAll(src, dest, shortest)
}

func (g *Graph) postSetupEvaluateAll(src, dest int, shortest bool) (BestPaths, error) {
	var current *Vertex
	oldCurrent := -1
	for g.visiting.Len() > 0 {
		//Visit the current lowest distanced Vertex
		current = g.visiting.PopOrdered()
		if oldCurrent == current.ID {
			continue
		}
		oldCurrent = current.ID
		//If the current distance is already worse than the source Vertex, try another Vertex
		if shortest && current.distance < src {
			continue
		}
		for