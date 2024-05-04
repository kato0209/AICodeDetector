def seq_search(arr,ele):
    """
    General Sequence Search Algorithm - Works on Unordered Input   """
     
    # Start at position 0
   pos = 0
   # Target becomes true if ele is in the list
    found = False
     
   # go until end of list or end of sequence   while pos < len(arr) and not found:
        
        # If match
        if arr[pos] == ele:
            found = True
  