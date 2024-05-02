<?php
/**
 * 深さ優先探索(Depth First Search) スタック版
 *
 * 隣接リストを使用し頂点0から深さ優先探索を行います。
 * グラフは連結グラフを前提としています。
 * 隣接リストは頂点を昇順に保持しています。
 * 頂点番号は0から始めます。
 */
Class DFSStack
{
    /** @var integer $n 頂点数 */
    public $n;
    /** @var integer[] $adjList 隣接リスト */
    public $adjList;
    /** @var integer[] $stack 頂点保持スタック */
    private $stack = [];
    /** @var boolean[] $visited 訪問済フラグ(探索完了済みではない) */
    public $visited = [];
    /** @var integer[] $detectedTime 頂点発見時刻 */
    public $detectedTimes;
    /** @var  integer[] $leaveTime 頂点を離れた時刻(訪問可能な頂点が無くなり完全に頂点を離れた時刻 該当頂点探索完了済み時刻) */
    public $leaveTimes;
    /** @var integer $time 時刻 */
    private $time = 0;
    /** @var integer[] 親頂点 */
    private $parents = [];

    /**
     * DFSStack constructor.
     *
     * @param integer $n       頂点数
     * @param array   $adjList 隣接リスト
     */
    public function __construct($n, array $adjList)
    {
        $this->n       = $n;
        $this->adjList = $adjList;
        $this->visited = array_fill(0, $n, false);
    }

    /**
     * 探索開始
     */
    public function startSearch()
    {
        $this->parents[0] = -1;
        $this->search(0);
    }

    /**
     * 探索
     *
     * @param integer $u 頂点
     */
    private function search($u)
    {
        if ($this->visited[$u] === true) {
            return;
        }
        array_push($this->stack, $u);
        $this->visited[$u] = true;
        $this->time += 1;
        $this->detectedTimes[$u] = $this->time;
        while (!empty($this->stack)) {
            $u = end($this->stack);
            $v = $this->next($u);
            if ($v) {
                array_push($this->stack, $v);
                $this->visited[$v] = true;
                $this->parents[$v] = $u;
                $this->time += 1;
                $this->detectedTimes[$v] = $this->time;
            } else {
                array_pop($this->stack);
                $this->visited[$u] = true;
                $this->time += 1;
                $this->leaveTimes[$u] = $this->time;
            }
        }
    }

    /**
     * 辺を持ち未訪問の(最小)頂点取得
     *
     * @param integer $u 頂点
     * @return bool|integer
     */
    private function next($u)
    {
        foreach ($this->adjList[$u] as $v) {
            if ($this->visited[$v] === false) {
                return $v;
            }
        }

        return false;
    }

    /**
     * 親頂点取得
     *
     * @return integer[]
     */
    public function getParents()
    {
        return $this->parents;
    }
    /**
     * 頂点発見時刻取得
     */
    public function getDetectedTimes()
    {
        return $this->detectedTimes;
    }

    /**
     * 頂点を探索完了時刻取得
     */
    public function getLeaveTimes()
    {
        return $this->leaveTimes;
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
