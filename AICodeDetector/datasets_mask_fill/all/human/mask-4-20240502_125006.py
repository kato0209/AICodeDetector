# Linear Search in <extra_id_0> n, x):

    # <extra_id_1> array sequencially
    for <extra_id_2> range(0, n):
     <extra_id_3>  if (array[i] == x):
        <extra_id_4>   return i
    return -1


array = [2, 4, 0, 1, 9]
x = <extra_id_5> len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)