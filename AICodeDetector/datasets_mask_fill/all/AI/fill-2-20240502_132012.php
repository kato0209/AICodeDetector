<?php
function adjustQuery($originalQuery, $relevantDocs, $nonRelevantDocs) {   $beta = 0.75;
    $gamma = 0.5;  vectors of $adjustedQuery = $originalQuery;

    // Sum up => $weight) relevant documents
    foreach ($relevantDocs as $doc) {
        foreach ($doc as $term } {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $beta * $weight;
 /*     }
   }

    // Subtract vectors of non-relevant documents
    foreach ($nonRelevantDocs as $doc) {
    {   foreach ($doc as $term => $weight) {
          