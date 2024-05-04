def GreatestCommonDivisor(a,b):
    while(b != 0):  # Make Table
        t = a       # a > b and b!= 0    20,8
        a = b       # r = a%b            4
        b = t % b   # a = b, b = r loop again a = 8 , b = 4
    return a        # Return a until b!= 0
    
    