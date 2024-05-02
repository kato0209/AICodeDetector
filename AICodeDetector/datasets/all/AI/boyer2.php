<?php
function buildBadCharTable($pattern) {
    $table = [];
    $len = strlen($pattern);
    for ($i = 0; $i < $len; $i++) {
        $table[$pattern[$i]] = $i;
    }
    return $table;
}

function boyerMooreSearchImproved($text, $pattern) {
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
            $shifts += ($shifts + $m < $n) ? $m - ($badCharTable[$text[$shifts + $m]] ?? $m) : 1;
        } else {
            $shifts += max(1, $j - ($badCharTable[$text[$shifts + $j]] ?? -1));
        }
    }
}

// Example usage
$text = "ABCAABCD";
$pattern = "ABC";
boyerMooreSearchImproved($text, $pattern);
?>
