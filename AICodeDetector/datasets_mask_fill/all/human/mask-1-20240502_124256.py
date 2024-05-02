def GreatestCommonDivisor(a,b):
 <extra_id_0>  while(b != 0):  # Make Table
  <extra_id_1>     t = a   <extra_id_2>   # a > b and b!= 0    20,8
  <extra_id_3>     a = b       # r = a%b <extra_id_4>       <extra_id_5>  4
        b = t % b   # a = b, b = <extra_id_6> again a = 8 , b = 4
    return a      <extra_id_7> # Return a until b!= <extra_id_8>   
    