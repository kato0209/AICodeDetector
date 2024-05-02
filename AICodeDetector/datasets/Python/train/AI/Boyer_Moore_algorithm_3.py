def boyer_moore_search(text, pattern):
    def build_bad_char_table(pattern):
        """
        Builds the bad character table.
        The table contains the rightmost occurrence of each character in the pattern.
        If a character is not in the pattern, it is assigned -1.
        """
        table = [-1] * 256  # Assuming ASCII character set
        for i, char in enumerate(pattern):
            table[ord(char)] = i
        return table

    bad_char_table = build_bad_char_table(pattern)
    m, n = len(pattern), len(text)
    s = 0  # s is the shift of the pattern with respect to text

    while s <= n - m:
        j = m - 1

        # Keep reducing index j of pattern while characters of pattern and text are matching
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # A match is found
            return s  # Return the position where the match starts

            # Shift the pattern so that the next character in text aligns with the last occurrence of it in pattern
            # If the character is not in the bad_char_table, shift the pattern completely
            s += (m - bad_char_table[ord(text[s + m])] if s + m < n else 1)
        else:
            # Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern
            s += max(1, j - bad_char_table[ord(text[s + j])])

    # No match found
    return -1

# Example usage
text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"
boyer_moore_search(text, pattern)
