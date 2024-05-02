<?php
function adjustQuery($originalQuery, $relevantDocs, $nonRelevantDocs) <extra_id_0>   $beta = 0.75;
    $gamma <extra_id_1>  <extra_id_2> $adjustedQuery = $originalQuery;

    // Sum up <extra_id_3> relevant documents
    foreach ($relevantDocs as $doc) {
        foreach ($doc as $term <extra_id_4> {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $beta * $weight;
 <extra_id_5>   <extra_id_6>  }
  <extra_id_7> }

    // Subtract vectors of non-relevant documents
    foreach ($nonRelevantDocs as $doc) {
    <extra_id_8>   foreach ($doc as $term => $weight) {
          