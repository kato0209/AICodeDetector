<extra_id_0> (
	"fmt"
)

func max(a, b <extra_id_1> {
	if a > <extra_id_2> a
	}
	return <extra_id_3> string) []int {
	const ALPHABET_SIZE = 256
	table := make([]int, ALPHABET_SIZE)
	for i := range table {
		table[i] = -1
	}
	for <extra_id_4> 0; i < len(pattern); i++ {
		table[pattern[i]] = i
	}
	return table
}

func BoyerMoore(text, pattern <extra_id_5> {
	m := <extra_id_6> len(text)
	badCharTable := makeBadCharTable(pattern)

	s := 0 // s is the shift of <extra_id_7> with respect to text
	for s <= (n - m) {
		j := m - 1

		// Decrease index j of pattern while characters of pattern and text are matching at this shift s
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}

		// If the pattern is present at the current shift, then index j will become -1 after the above loop
		if <extra_id_8> 0 {
			return s // Pattern