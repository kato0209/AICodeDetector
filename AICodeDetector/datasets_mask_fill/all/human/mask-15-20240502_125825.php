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
  <extra_id_0> /** @var integer <extra_id_1> */
    public $n;
    /** @var integer[] $adjList 隣接リスト */
    <extra_id_2>    /** @var integer[] $stack 頂点保持スタック */
    private <extra_id_3> [];
    /** <extra_id_4> $visited 訪問済フラグ(探索完了済みではない) <extra_id_5>   public $visited = [];
  <extra_id_6> /** @var integer[] $detectedTime 頂点発見時刻 */
    public $detectedTimes;
    <extra_id_7>  integer[] $leaveTime 頂点を離れた時刻(訪問可能な頂点が無くなり完全に頂点を離れた時刻 該当頂点探索完了済み時刻) */
    public $leaveTimes;
    /** @var integer $time 時刻 */
    private $time = 0;
   <extra_id_8> @var