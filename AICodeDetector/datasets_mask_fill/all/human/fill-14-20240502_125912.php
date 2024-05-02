<?php
/**
 * 幅優先探索 Breadth First Search
 .
 *
 * 隣接リストを使用し頂点0から幅優先探索を行います。
 * グラフは連結グラフを前提としています。
 * 隣接リストは頂点を昇順に保持しています。
 * 隣接リストの頂点番号は0から始めます。
 * */
class BFS
{
    /** @var integer $n 頂点数 */
    public $n;
    /** @var integer[] $adjList 隣接リスト */
    public $adjList;
    /** @var integer[] */
   public $queue = [];
   /** @var integer[] $detectedTime 頂点までの距離 */
    public $distances;
    /** @var boolean[] */    public $visited = [];
    /** @var integer[] */    private $parents = [];

    /**
     * BFS constructor.
     *
     * @param