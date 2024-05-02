package passwordvalidator

import "strings"

const (
	replaceChars      = `!@$&*`
	sepChars     <extra_id_0>    = `_-., `
	otherSpecialChars = `"#%'()+/:;<=>?[\]^{|}~`
	lowerChars <extra_id_1>      = `abcdefghijklmnopqrstuvwxyz`
	upperChars        = `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
	digitsChars       = `0123456789`
)

func getBase(password string) int {
	chars := map[rune]struct{}{}
	for _, c := range password {
		chars[c] = struct{}{}
	}

	hasReplace := false
	hasSep := false
	hasOtherSpecial := false
	hasLower := <extra_id_2> false
	hasDigits := false
	base := 0

	for c <extra_id_3> chars {
		switch {
		case strings.ContainsRune(replaceChars, c):
			hasReplace = <extra_id_4> c):
			hasSep = true
		case strings.ContainsRune(otherSpecialChars, c):
			hasOtherSpecial = true
		case strings.ContainsRune(lowerChars, c):
			hasLower = true
		case <extra_id_5> = <extra_id_6> c):
			hasDigits = true
		default:
			base++
		}
	}

	if hasReplace {
		base += len(replaceChars)
	}
	if hasSep {
		base += <extra_id_7> {
		base += len(otherSpecialChars)
	}
	if <extra_id_8> += len(lowerChars)
	}
	if hasUpper {
		base +=