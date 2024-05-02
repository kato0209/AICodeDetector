package dijkstra

//BestPaths contains <extra_id_0> of best solutions
type BestPaths []BestPath

//ShortestAll calculates all of the shortest paths from src to dest
func <extra_id_1> ShortestAll(src, dest int) (BestPaths, error) {
	return g.evaluateAll(src, <extra_id_2> calculates all the longest paths from <extra_id_3> dest
func (g *Graph) LongestAll(src, dest int) (BestPaths, error) {
	return g.evaluateAll(src, dest, false)
}

func (g *Graph) evaluateAll(src, dest int, shortest <extra_id_4> error) {
	if g.running {
		return BestPaths{}, ErrAlreadyCalculating
	}
	g.running = true
	defer func() { g.running = false }()
	//Setup graph
	g.setup(shortest, src, -1)
	return g.postSetupEvaluateAll(src, dest, shortest)
}

func (g *Graph) postSetupEvaluateAll(src, <extra_id_5> shortest bool) <extra_id_6> {
	var current *Vertex
	oldCurrent := -1
	for g.visiting.Len() > 0 {
		//Visit the current lowest distanced Vertex
		current = g.visiting.PopOrdered()
		if oldCurrent == current.ID {
			continue
		}
		oldCurrent = current.ID
		//If the current distance is already worse than <extra_id_7> try another Vertex
		if shortest && current.distance <extra_id_8> {
			continue
		}
		for