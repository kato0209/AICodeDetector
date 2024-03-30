<?php
/**
 * 幅優先探索 Breadth First Search
 *
 * 隣接リストを使用し頂点0から幅優先探索を行います。
 * グラフは連結グラフを前提としています。
 * 隣接リストは頂点を昇順に保持しています。
 * 隣接リストの頂点番号は0から始めます。
 * 0からたどり着けない頂点の距離は-1を設定します。
 */
Class BFS
{
    /** @var integer $n 頂点数 */
    public $n;
    /** @var integer[] $adjList 隣接リスト */
    public $adjList;
    /** @var integer[] 管理用キュー */
    public $queue = [];
    /** @var integer[] $detectedTime 頂点までの距離 */
    public $distances;
    /** @var boolean[] 訪問済フラグ(探索完了済みではない) */
    public $visited = [];
    /** @var integer[] 親頂点 */
    private $parents = [];

    /**
     * BFS constructor.
     *
     * @param integer $n       頂点数
     * @param array   $adjList 隣接リスト
     */
    public function __construct($n, array $adjList)
    {
        $this->n       = $n;
        $this->adjList = $adjList;
        $this->visited = array_fill(0, $n, false);
        $this->start();
    }

    /**
     * 探索開始
     */
    private function start()
    {
        $this->queue        = [];
        $this->distances[0] = 0;
        $this->visited[0]   = true;
        $this->parents[0]   = -1;
        array_push($this->queue, 0);
        $this->search();
    }

    /**
     * 探索
     */
    private function search()
    {
        while (!empty($this->queue)) {
            $u    = array_shift($this->queue);
            $next = $this->next($u);
            foreach ($next as $v) {
                array_push($this->queue, $v);
                $this->visited[$v] = true;
                $this->parents[$v] = $u;
                if (isset($this->distances[$u])) {
                    $this->distances[$v] = $this->distances[$u] + 1;
                }
            }
        }

        return;
    }

    /**
     * @param integer $u 頂点
     * @return bool|mixed
     */
    private function next($u)
    {
        $next = [];
        foreach ($this->adjList[$u] as $v) {
            if ($this->visited[$v] === false) {
                array_push($next, $v);
            }
        }

        return $next;
    }

    /**
     * 頂点の距離取得
     */
    public function getDistances()
    {
        return $this->distances;
    }

    /**
     * 経路取得
     *
     * @return array
     */
    public function getPath()
    {
        return $this->parents;
    }
}
