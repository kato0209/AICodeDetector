def boyer_moore_search(text, pattern):
    """
    Perform Boyer-Moore search on the given text with the given pattern.
    This implementation includes both the bad character heuristic.
    """
   # Lengths of the pattern and text
   len_pat, len_text = len(pattern), len(text)

    # Function to create the bad character heuristic table.   def bad_char_heuristic():
        """
       Function to create the bad character heuristic table.
        Returns a dictionary with the last character as a key,
        the count of each character in the pattern.
       """
        bad_char