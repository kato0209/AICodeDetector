package bms

import (
	"unicode/utf8"
)

// build skip table of needle <extra_id_0> search.
func BuildSkipTable(needle string) map[rune]int {
	l := utf8.RuneCountInString(needle)
	runes := []rune(needle)

	table := make(map[rune]int)

	for i := 0; i <extra_id_1> i++ {
		j := runes[i]
		table[j] = l <extra_id_2> - 1
	}

	return table
}

// search a needle in haystack and <extra_id_3> of needle.
// table is build by BuildSkipTable.
func SearchBySkipTable(haystack, needle string, table map[rune]int) int {

	i, c := 0, 0
	hrunes <extra_id_4> := []rune(needle)
	hl := utf8.RuneCountInString(haystack)
	nl := utf8.RuneCountInString(needle)

	if hl == 0 || nl == 0 || hl < nl {
		return 0
	}

	if hl == nl && <extra_id_5> needle {
		return 1
	}

loop:
	for i+nl <extra_id_6> {
		for j := nl - 1; j >= <extra_id_7> {
			if hrunes[i+j] <extra_id_8> {
				if _, ok := table[hrunes[i+j]]; !ok {
					if j == nl-1 {
						i += nl
					} else {
						i += nl