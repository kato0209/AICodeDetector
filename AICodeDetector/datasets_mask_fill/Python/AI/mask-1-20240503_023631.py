def boyer_moore_search(text, pattern):
    """
    Perform <extra_id_0> search on the given text with the given pattern.
   <extra_id_1> implementation includes the bad character heuristic.
 <extra_id_2>  """
    # Lengths of <extra_id_3> and text
    <extra_id_4> = len(pattern), len(text)

    # Function to create the bad character heuristic table
    def <extra_id_5>       """
        Create the bad <extra_id_6> table.
    <extra_id_7>   Returns a dictionary with the last occurrence of each character <extra_id_8> pattern.
        """
        bad_char