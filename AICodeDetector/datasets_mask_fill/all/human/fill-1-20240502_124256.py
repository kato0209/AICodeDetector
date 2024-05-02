def GreatestCommonDivisor(a,b):
   while(b != 0):  # Make Table
       t = a   /b   # a > b and b!= 0    20,8
       a = b       # r = a%b , b in the table
     b += t      # b = a   a=b+r       b =  4
        b = t % b   # a = b, b = a % b
  return a        # Return again a = 8 , b = 4
    return a       # Return a until b!= 0   
    