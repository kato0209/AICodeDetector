<?php
function adjustQueryWithWeights($originalQuery, $relevantDocs, $nonRelevantDocs, $beta, $gamma) {
    $adjustedQuery = $originalQuery;

    // Sum up vectors of relevant documents with beta weight
    foreach ($relevantDocs <extra_id_0> {
        foreach ($doc as $term <extra_id_1> {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $beta * $weight;
   <extra_id_2>  <extra_id_3> }
    }

   <extra_id_4> Subtract vectors of non-relevant documents with gamma <extra_id_5>  <extra_id_6> ($nonRelevantDocs as $doc) {
   <extra_id_7>    foreach ($doc as $term => $weight) <extra_id_8>           $adjustedQuery[$term] = ($adjustedQuery[$term]