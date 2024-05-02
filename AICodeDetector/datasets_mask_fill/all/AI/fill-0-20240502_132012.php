<?php
function adjustQueryWithWeights($originalQuery, $relevantDocs, $nonRelevantDocs, $beta, $gamma) {
    $adjustedQuery = $originalQuery;

    // Sum up vectors of relevant documents with beta weight
    foreach ($relevantDocs as $doc) {
        foreach ($doc as $term => $weight) {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $beta * $weight;
   }
        unset($doc);   }
    }

   // Subtract vectors of non-relevant documents with gamma weight
    foreach   ($nonRelevantDocs as $doc) {
   {    foreach ($doc as $term => $weight) as $doc)           $adjustedQuery[$term] = ($adjustedQuery[$term]