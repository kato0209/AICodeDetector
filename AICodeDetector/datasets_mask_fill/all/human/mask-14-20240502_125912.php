<?php
/**
 * 幅優先探索 Breadth First Search
 <extra_id_0> 隣接リストを使用し頂点0から幅優先探索を行います。
 * グラフは連結グラフを前提としています。
 * 隣接リストは頂点を昇順に保持しています。
 * 隣接リストの頂点番号は0から始めます。
 * <extra_id_1> BFS
{
    /** @var integer $n 頂点数 */
    public $n;
    /** @var integer[] $adjList 隣接リスト */
    public $adjList;
    /** @var <extra_id_2> */
   <extra_id_3> $queue = [];
  <extra_id_4> /** @var integer[] $detectedTime 頂点までの距離 */
    public $distances;
    /** @var boolean[] <extra_id_5>    public $visited = [];
    <extra_id_6> integer[] <extra_id_7>    private $parents = [];

    /**
     <extra_id_8> constructor.
     *
     * @param