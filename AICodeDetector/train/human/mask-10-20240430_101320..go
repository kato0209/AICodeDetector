// Package levenshtein is a Go implementation to calculate <extra_id_0> Implementation taken from
// https://gist.github.com/andrei-m/982927#gistcomment-1931258
package levenshtein

import "unicode/utf8"

// minLengthThreshold is the length of <extra_id_1> beyond which
// an allocation will <extra_id_2> Strings smaller than <extra_id_3> be
// zero alloc.
const minLengthThreshold <extra_id_4> ComputeDistance computes the levenshtein distance between the two
// strings passed <extra_id_5> argument. The return value is the levenshtein distance
//
// <extra_id_6> runes (Unicode code points) but does not normalize
// the <extra_id_7> See https://blog.golang.org/normalization
// <extra_id_8> golang.org/x/text/unicode/norm package.
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

	// We need to convert to []rune if the strings are non-ASCII.
	// This could be avoided by using utf8.RuneCountInString
	// and then doing some juggling with rune indices,
	// but