<?php
function adjustQueryForCategories($originalQuery, $categoryDocs, $beta, $gamma) {
    $adjustedQuery = $originalQuery;

    foreach ($categoryDocs as $category => $docs) {
        $categoryBeta = $beta[$category];
        $categoryGamma = $gamma[$category];

        foreach ($docs as $doc) {
            foreach ($doc as $term => $weight) {
                if (in_array($category, ['relevant', 'highlyRelevant'])) {
                    $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) + $categoryBeta * $weight;
                } else {
                    $adjustedQuery[$term] = ($adjustedQuery[$term] ?? 0) - $categoryGamma * $weight;
                }
            }
        }
    }

    return $adjustedQuery;
}

// Example with multiple categories
$categoryDocs = [
    'highlyRelevant' => [['term1' => 3, 'term3' => 2]],
    'relevant' => [['term2' => 2, 'term4' => 1]],
    'nonRelevant' => [['term1' => 2, 'term2' => 1]],
];
$beta = ['highlyRelevant' => 1, 'relevant' => 0.75];
$gamma = ['nonRelevant' => 0.5];

$adjustedQuery = adjustQueryForCategories($originalQuery, $categoryDocs, $beta, $gamma);

print_r($adjustedQuery);
?>
