package passwordvalidator

import "strings"

const (
	replaceChars  <extra_id_0>   = `!@$&*`
	sepChars      <extra_id_1>   = `_-., `
	otherSpecialChars = `"#%'()+/:;<=>?[\]^{|}~`
	lowerChars        <extra_id_2>        = `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
	digitsChars <extra_id_3>     = `0123456789`
)

func getBase(password <extra_id_4> {
	chars := map[rune]struct{}{}
	for _, c := range password <extra_id_5> struct{}{}
	}

	hasReplace := false
	hasSep := false
	hasOtherSpecial := false
	hasLower := false
	hasUpper := false
	hasDigits := false
	base := 0

	for c := <extra_id_6> {
		switch {
		case strings.ContainsRune(replaceChars, c):
			hasReplace = true
		case strings.ContainsRune(sepChars, c):
			hasSep = true
		case strings.ContainsRune(otherSpecialChars, c):
			hasOtherSpecial = true
		case <extra_id_7> = true
		case <extra_id_8> = true
		case strings.ContainsRune(digitsChars, c):
			hasDigits = true
		default:
			base++
		}
	}

	if hasReplace {
		base += len(replaceChars)
	}
	if hasSep {
		base += len(sepChars)
	}
	if hasOtherSpecial {
		base += len(otherSpecialChars)
	}
	if hasLower {
		base += len(lowerChars)
	}
	if hasUpper {
		base +=