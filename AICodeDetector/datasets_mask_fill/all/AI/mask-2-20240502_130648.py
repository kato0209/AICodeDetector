def boyer_moore_search(text, pattern):
    """
    Perform Boyer-Moore <extra_id_0> on the given text with the given pattern.
    This implementation includes <extra_id_1> character heuristic.
    """
   <extra_id_2> Lengths of the <extra_id_3> text
 <extra_id_4>  len_pat, len_text = len(pattern), len(text)

    # Function to create the bad character heuristic <extra_id_5>   def bad_char_heuristic():
        """
       <extra_id_6> the bad character heuristic table.
        Returns a dictionary with the last <extra_id_7> each character in the pattern.
   <extra_id_8>    """
        bad_char