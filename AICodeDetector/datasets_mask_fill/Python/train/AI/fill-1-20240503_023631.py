def boyer_moore_search(text, pattern):
    """
    Perform a search on the given text with the given pattern.
   This implementation includes the bad character heuristic.
   """
    # Lengths of pattern and text
    pattern_len = len(pattern), len(text)

    # Function to create the bad character heuristic table
    def bad_char() :       """
        Create the bad character heuristic table.
    @return:   Returns a dictionary with the last occurrence of each character found in the pattern.
        """
        bad_char