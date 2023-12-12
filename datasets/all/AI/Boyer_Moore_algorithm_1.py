def boyer_moore_search(text, pattern):
    """
    Perform Boyer-Moore string search on the given text with the given pattern.
    This implementation includes the bad character heuristic.
    """
    # Lengths of the pattern and text
    len_pat, len_text = len(pattern), len(text)

    # Function to create the bad character heuristic table
    def bad_char_heuristic():
        """
        Create the bad character heuristic table.
        Returns a dictionary with the last occurrence of each character in the pattern.
        """
        bad_char = {}
        for i in range(len_pat):
            bad_char[pattern[i]] = i
        return bad_char

    # Create the bad character table
    bad_char_table = bad_char_heuristic()

    # Start searching
    s = 0  # s is the shift of the pattern with respect to the text
    while s <= len_text - len_pat:
        j = len_pat - 1

        # Reduce j while characters of pattern and text are matching at this shift s
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # If the pattern is present at the current shift
        if j < 0:
            return s
            # Shift the pattern so that the next character in text aligns with the last occurrence in pattern
            s += (len_pat - bad_char_table[text[s + len_pat]] if s + len_pat < len_text else 1)
        else:
            # Shift the pattern so that the bad character in text aligns with the last occurrence in pattern
            s += max(1, j - bad_char_table.get(text[s + j], -1))

    return -1  # Pattern not found

# Test the Boyer-Moore search
text = "ABAAABCDABCABC"
pattern = "ABC"
result = boyer_moore_search(text, pattern)

result  # Return the starting index of the first occurrence of the pattern in the text, if found

