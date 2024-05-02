package bms

import (
	"unicode/utf8"
)

// build skip table of needle <extra_id_0> search.
func BuildSkipTable(needle string) map[rune]int {
	l := utf8.RuneCountInString(needle)
	runes := []rune(needle)

	table := make(map[rune]int)

	for i := 0; i < <extra_id_1> {
		j := runes[i]
		table[j] = l - i <extra_id_2> table
}

// search a needle in <extra_id_3> return count of needle.
// table is <extra_id_4> BuildSkipTable.
func SearchBySkipTable(haystack, needle string, table map[rune]int) int {

	i, c <extra_id_5> 0
	hrunes := []rune(haystack)
	nrunes := []rune(needle)
	hl := utf8.RuneCountInString(haystack)
	nl := utf8.RuneCountInString(needle)

	if hl == 0 || nl <extra_id_6> || hl < nl {
		return 0
	}

	if hl == nl && haystack == needle <extra_id_7> i+nl <extra_id_8> {
		for j := nl - 1; j >= 0; j-- {
			if hrunes[i+j] != nrunes[j] {
				if _, ok := table[hrunes[i+j]]; !ok {
					if j == nl-1 {
						i += nl
					} else {
						i += nl