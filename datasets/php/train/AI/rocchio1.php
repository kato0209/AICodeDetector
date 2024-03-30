<?php
function adjustQuery($originalQuery, $relevantDocs, $nonRelevantDocs) {
    $beta = 0.75;
    $gamma = 0.15;
    $adjustedQuery = $originalQuery;

    // Sum up vectors of relevant documents
    foreach ($relevantDocs as $doc) {
        foreach ($doc as $term => $weight) {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $beta * $weight;
        }
    }

    // Subtract vectors of non-relevant documents
    foreach ($nonRelevantDocs as $doc) {
        foreach ($doc as $term => $weight) {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) - $gamma * $weight;
        }
    }

    return $adjustedQuery;
}

// Example vectors (term => weight)
$originalQuery = ['term1' => 1, 'term2' => 2];
$relevantDocs = [
    ['term1' => 2, 'term3' => 3],
    ['term2' => 1, 'term4' => 4],
];
$nonRelevantDocs = [
    ['term1' => 1, 'term2' => 5],
];

$adjustedQuery = adjustQuery($originalQuery, $relevantDocs, $nonRelevantDocs);

print_r($adjustedQuery);
?>
