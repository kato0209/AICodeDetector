<?php
// Functions for bad character rule as before

function boyerMooreSearchWithGoodSuffix($text, $pattern) {
    // Assuming implementation of the Good Suffix table creation function
    // For simplicity, this snippet will not implement the full good suffix heuristic
    // but will include a placeholder for where that logic would go.

    $badCharTable = buildBadCharTable($pattern);
    $n = strlen($text);
    $m = strlen($pattern);
    $shifts = 0;

    while ($shifts <= ($n - $m)) {
        $j = $m - 1;

        while ($j >= 0 && $pattern[$j] == $text[$shifts + $j]) {
            $j--;
        }

        if ($j < 0) {
            echo "Pattern found at position " . $shifts . "\n";
            // Placeholder for good suffix shift
            $shifts += ($shifts + $m < $n) ? $m - ($badCharTable[$text[$shifts + $m]] ?? $m) : 1;
        } else {
            // Bad Character Rule
            $bcShift = max(1, $j - ($badCharTable[$text[$shifts + $j]] ?? -1));
            // Placeholder for Good Suffix Rule shift calculation
            $gsShift = $m; // Simplification for example purposes
            $shifts += max($bcShift, $gsShift);
        }
    }
}

// Example usage remains the same
?>
