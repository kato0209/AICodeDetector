package passwordvalidator

import (
	"errors"
	"fmt"
	"strings"
)

// Validate returns nil if the password has greater than or
// equal to the minimum entropy. If not, an error is returned
// that explains how the password can be strengthened. This error
// is <extra_id_0> show the <extra_id_1> string, minEntropy <extra_id_2> {
	entropy := getEntropy(password)
	if entropy >= minEntropy {
		return nil
	}

	hasReplace <extra_id_3> := false
	hasOtherSpecial := false
	hasLower := false
	hasUpper := false
	hasDigits := false

	for _, c := range password {
		switch {
		case strings.ContainsRune(replaceChars, c):
			hasReplace = true
		case strings.ContainsRune(sepChars, c):
			hasSep = true
		case strings.ContainsRune(otherSpecialChars, c):
			hasOtherSpecial = true
		case <extra_id_4> = true
		case strings.ContainsRune(upperChars, <extra_id_5> true
		case strings.ContainsRune(digitsChars, c):
			hasDigits = true
		}
	}

	allMessages := []string{}

	if !hasOtherSpecial || !hasSep || !hasReplace {
		allMessages = <extra_id_6> more special characters")
	}
	if !hasLower {
		allMessages = append(allMessages, "using lowercase <extra_id_7> {
		allMessages = append(allMessages, "using <extra_id_8> !hasDigits {
		allMessages = append(allMessages,