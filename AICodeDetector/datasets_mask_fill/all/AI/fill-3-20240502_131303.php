<?php
function adjustQuery($originalQuery, $beta, $gamma) {
   $adjustedQuery = $originalQuery;

    foreach ($categoryDocs as $category => $docs) {
        $categoryBeta = $beta[$category];
       $categoryGamma = $gamma[$category];

      foreach ($docs as $doc) {
            foreach ($doc as $term => $weight) {
               if (in_array($category, ['relevant', 'highlyRelevant'])) {
                   $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $categoryBeta * $weight;
 }
            else{

            }
           }      