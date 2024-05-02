package main

import (
    "errors"
    "fmt"
)

// ノード
type Node struct {
    name  string  // ノード名
    edges []*Edge // 次に移動できるエッジ
    done  bool    // 処理済みかを表すフラグ
    cost int     // このノードにたどり着くのに必要だったコスト
    prev  *Node   // このノードにたどりつくのに使われたノード
}

func NewNode(name string) *Node {
    node := &Node{name, []*Edge{}, false, -1, nil}
    return node
}

// ノードに次の接続先を示したエッジを追加する
func (self *Node) AddEdge(edge *Edge) {
    self.edges = append(self.edges, edge)
}

// エッジ
type Edge struct {
    next *Node // 次に移動できるノード
    cost int  // 移動にかかるコスト
}

func NewEdge(next *Node, cost int) *Edge {
    edge := &Edge{next, cost}
    return edge
}

// 有向グラフ
type DirectedGraph struct {
    nodes map[string]*Node
}

func NewDirectedGraph() *DirectedGraph {
    return &DirectedGraph{
        map[string]*Node{}}
}

// グラフの要素を追加する (接続元ノード名、接続先ノード名、移動にかかるコスト)
func (self *DirectedGraph) Add(src, dst string, cost int) {
    // ノードが既にある場合は追加しない
    srcNode, ok := self.nodes[src]
    if !ok {
      srcNode = NewNode(src)
        self.nodes[src] = srcNode
    }
    
    dstNode, ok := self.nodes[dst]
    if !ok {
        dstNode = NewNode(dst)
        self.nodes[dst] = dstNode
    }

    // ノードをエッジでつなぐ
    edge := NewEdge(dstNode, cost)
    srcNode.AddEdge(edge)
}

// スタートとゴールを指定して最短経路を求める
func (self *DirectedGraph) ShortestPath(start string, goal string) (ret []*Node, err error) {
    // 名前からスタート地点のノードを取得する
    startNode := self.nodes[start]

    // スタートのコストを 0 に設定することで処理対象にする
    startNode.cost = 0

    for {
        // 次の処理対象のノードを取得する
        node, err := self.nextNode()

        // 次に処理するノードが見つからなければ終了
        if err != nil {
            return nil, errors.New("Goal not found")
        }

        // ゴールまで到達した
        if node.name == goal {
            break
        }
        
        // 取得したノードを処理する
        self.calc(node)
    }
    
    // ゴールから逆順にスタートまでノードをたどっていく
    n := self.nodes[goal]
    for {
        ret = append(ret, n)
        if n.name == start {
            break
        }
        n = n.prev
    }
    
    return ret, nil
}

// つながっているノードのコストを計算する
func (self *DirectedGraph) calc(node *Node) {
    // ノードにつながっているエッジを取得する
    for _, edge := range node.edges {
        nextNode := edge.next

        // 既に処理済みのノードならスキップする
        if nextNode.done {
            continue
        }

        // このノードに到達するのに必要なコストを計算する
        cost := node.cost + edge.cost
        if nextNode.cost == -1 || cost < nextNode.cost {
            // 既に見つかっている経路よりもコストが小さければ処理中のノードを遷移元として記録する
            nextNode.cost = cost
            nextNode.prev = node
        }
    }
    
    // つながっているノードのコスト計算がおわったらこのノードは処理済みをマークする
    node.done = true
}

func (self *DirectedGraph) nextNode() (next *Node, err error) {
    // グラフに含まれるノードを線形探索する
    for _, node := range self.nodes {
        
        // 処理済みのノードは対象外
        if node.done {
            continue
        }
        
        // コストが初期値 (-1) になっているノードはまだそのノードまでの最短経路が判明していないので処理できない
        if node.cost == -1 {
            continue
        }
        
        // 最初に見つかったものは問答無用で次の処理対象の候補になる
        if next == nil {
            next = node
        }
        
        // 既に見つかったノードよりもコストの小さいものがあればそちらを先に処理しなければいけない
        if next.cost > node.cost {
            next = node
        }
    }
    
    // 次の処理対象となるノードが見つからなかったときはエラー
    if next == nil {
        return nil, errors.New("Untreated node not found")
    }
    
    return
}

func main() {
    // 有向グラフを作る
    g := NewDirectedGraph()
 
    // グラフを定義していく
    g.Add("s", "a", 2)
    g.Add("s", "b", 5)
    g.Add("a", "b", 2)
    g.Add("a", "c", 5)
    g.Add("b", "c", 4)
    g.Add("b", "d", 2)
    g.Add("c", "z", 7)
    g.Add("d", "c", 5)
    g.Add("d", "z", 2)
 
    // "s" ノードから "z" ノードへの最短経路を得る
    path, err := g.ShortestPath("s", "z")
 
    // 経路が見つからなければ終了
    if err != nil {
        fmt.Println("Goal not found")
        return
    }
 
    // 見つかった経路からノードとコストを表示する
    for _, node := range path {
        fmt.Printf("ノード: %v, コスト: %v\n", node.name, node.cost)
    }
}
