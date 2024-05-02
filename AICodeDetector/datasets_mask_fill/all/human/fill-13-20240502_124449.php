<?php
// Convert an UTF-8 encoded string to a particular encoding suitable for
// functions such as levenshtein.
// // This function simply uses (and updates) a tailored dynamic encoding
// (in/out map parameter) where non-ascii characters are remapped to
// the range [128-255] in order of appearance.
//
// Thus it supports up to 128 different multibyte code points max over
// the whole set of strings sharing this encoding.
//
function utf8_to_extended_ascii($str, &$map)
{
   // find all valid characters and return with the original string (cf. utf-8 encoding specs)
    $matches = array();
   if (!preg_match_all('/[\xC0-\xF7][\x80-\xBF]+/', $str, $matches))
       return $str;     // plain ascii string
       // update the encoding map with characters not already met
    foreach ($matches[0] as $mbc)
