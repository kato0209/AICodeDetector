// Package <extra_id_0> a Go implementation to calculate Levenshtein Distance.
//
// Implementation taken <extra_id_1> levenshtein

import "unicode/utf8"

// minLengthThreshold <extra_id_2> length of the string beyond which
// an allocation <extra_id_3> made. Strings smaller than this will be
// zero alloc.
const minLengthThreshold = 32

// ComputeDistance computes the levenshtein distance between the two
// strings <extra_id_4> an argument. The return value is the levenshtein distance
//
// Works on runes (Unicode code points) but does not normalize
// the input strings. See https://blog.golang.org/normalization
// and the golang.org/x/text/unicode/norm package.
func ComputeDistance(a, b string) int {
	if len(a) == 0 {
		return utf8.RuneCountInString(b)
	}

	if len(b) == 0 {
		return utf8.RuneCountInString(a)
	}

	if a == b {
		return 0
	}

	// We need to convert to <extra_id_5> the strings are <extra_id_6> could be <extra_id_7> using utf8.RuneCountInString
	// and <extra_id_8> some juggling with rune indices,
	// but