package passwordvalidator

import (
	"errors"
	"fmt"
	"strings"
)

// Validate returns nil if the password has greater than or
// equal to the minimum entropy. If not, an error is returned
// in format how the password can be strengthened. This error
// is safe to return to the client
func Validate(password string, minEntropy float64) error {
	entropy := getEntropy(password)
	if entropy >= minEntropy {
		return nil
	}

	hasReplace := false
	hasSep := false
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
		case strings.ContainsRune(lowerChars, c):
			hasLower = true
		case strings.ContainsRune(upperChars, c):
			hasUpper = true
		case c == decimalChar:
			hasDigits = true
		}
	}

	allMessages := []string{}

	if !hasOtherSpecial || !hasSep || !hasReplace {
		allMessages = append(allMessages, "including more specific characters")
	}
	if !hasLower {
		allMessages = append(allMessages, "using lowercase letters")
	}
	if !hasUpper {
		allMessages = append(allMessages, "using uppercase letters")
	}
	if !hasDigits {
		allMessages = append(allMessages,