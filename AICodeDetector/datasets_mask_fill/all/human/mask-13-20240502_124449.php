<?php
// Convert an UTF-8 encoded string to a <extra_id_0> suitable for
// functions such as levenshtein.
// <extra_id_1> function simply uses (and updates) a tailored dynamic encoding
// (in/out map parameter) where non-ascii characters are remapped to
// the range [128-255] in order of appearance.
//
// Thus it supports up to 128 different multibyte code points max over
// the whole set of strings sharing this encoding.
//
function utf8_to_extended_ascii($str, &$map)
{
   <extra_id_2> find all <extra_id_3> (cf. utf-8 encoding specs)
    $matches = array();
  <extra_id_4> if (!preg_match_all('/[\xC0-\xF7][\x80-\xBF]+/', $str, $matches))
   <extra_id_5>    return <extra_id_6> plain ascii string
    <extra_id_7>   // update the encoding map <extra_id_8> characters not already met
    foreach ($matches[0] as $mbc)
