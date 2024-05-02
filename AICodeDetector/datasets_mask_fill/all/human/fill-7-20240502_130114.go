// Package levenshtein provides a Go implementation to calculate Levenshtein Distance.
//
// Implementation taken from: http://stackoverflow.com/a/1979388/365528
package levenshtein

import "unicode/utf8"

// minLengthThreshold is the maximum length of the string beyond which
// an allocation is made. Strings smaller than this will be
// zero alloc.
const minLengthThreshold = 32

// ComputeDistance computes the levenshtein distance between the two
// strings as an argument. The return value is the levenshtein distance
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

	// We need to convert to integers as the strings are case insensitive
	// since they could be compared using utf8.RuneCountInString
	// and it may lead to some juggling with rune indices,
	// but