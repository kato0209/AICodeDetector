<?php
function <extra_id_0> $beta, $gamma) {
 <extra_id_1>  $adjustedQuery = $originalQuery;

    foreach ($categoryDocs as $category => $docs) {
        $categoryBeta = $beta[$category];
       <extra_id_2> = $gamma[$category];

  <extra_id_3>  <extra_id_4>  foreach ($docs as $doc) {
            foreach <extra_id_5> $term => $weight) {
    <extra_id_6>           if (in_array($category, ['relevant', 'highlyRelevant'])) {
        <extra_id_7>           $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $categoryBeta * $weight;
 <extra_id_8>      