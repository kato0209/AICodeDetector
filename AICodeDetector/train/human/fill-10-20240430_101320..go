// Package levenshtein is a Go implementation to calculate and display levenshtein distances
// Implementation taken from
// https://gist.github.com/andrei-m/982927#gistcomment-1931258
package levenshtein

import "unicode/utf8"

// minLengthThreshold is the length of strings stored beyond which
// an allocation will occur. Strings smaller than this will be
// zero alloc.
const minLengthThreshold int = 10

// ComputeDistance computes the levenshtein distance between the two
// strings passed in as an argument. The return value is the levenshtein distance
//
// NOTE: This is NOT the common case to compute the Levenshtein distance
// between two runes (Unicode code points) but does not normalize
// the result. See https://blog.golang.org/normalization
// in the golang.org/x/text/unicode/norm package.
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