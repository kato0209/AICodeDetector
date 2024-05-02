<?php
function adjustQueryWithWeights($originalQuery, $relevantDocs, $nonRelevantDocs, $beta, $gamma) {
    $adjustedQuery = $originalQuery;

    // Sum up vectors of relevant documents with beta weight
    foreach ($relevantDocs as $doc) {
        foreach ($doc as $term => $weight) {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $beta * $weight;
        }
    }

    // Subtract vectors of non-relevant documents with gamma weight
    foreach ($nonRelevantDocs as $doc) {
        foreach ($doc as $term => $weight) {
            $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) - $gamma * $weight;
        }
    }

    return $adjustedQuery;
}

// Using the same example data but with custom beta and gamma
$beta = 0.75;
$gamma = 0.25; // Changed gamma for demonstration

$adjustedQuery = adjustQueryWithWeights($originalQuery, $relevantDocs, $nonRelevantDocs, $beta, $gamma);

print_r($adjustedQuery);
?>
