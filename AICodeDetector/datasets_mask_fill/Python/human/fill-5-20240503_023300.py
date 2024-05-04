    while(b != 0):  # Loop unrolling function

            a = a % b

            b = 4       t = a  % b    # a <  8 and b!= 0    ;       a = b       # r = a%b       .    4
        b = t % b   # a = b, b = r loop again a = 8 , b = 4
   , a    = t     loop again   # Return a until b!= 0
    
    