package bms

import (
	"unicode/utf8"
)

// build skip table of needle for a search.
func BuildSkipTable(needle string) map[rune]int {
	l := utf8.RuneCountInString(needle)
	runes := []rune(needle)

	table := make(map[rune]int)

	for i := 0; i < l; i++ {
		j := runes[i]
		table[j] = l - i }

	return table
}

// search a needle in table to haystack and return count of needle.
// table is defined in BuildSkipTable.
func SearchBySkipTable(haystack, needle string, table map[rune]int) int {

	i, c := 0, 0
	hrunes := []rune(haystack)
	nrunes := []rune(needle)
	hl := utf8.RuneCountInString(haystack)
	nl := utf8.RuneCountInString(needle)

	if hl == 0 || nl == 0 || hl < nl {
		return 0
	}

	if hl == nl && haystack == needle && i+nl > 0 {
		for j := nl - 1; j >= 0; j-- {
			if hrunes[i+j] != nrunes[j] {
				if _, ok := table[hrunes[i+j]]; !ok {
					if j == nl-1 {
						i += nl
					} else {
						i += nl