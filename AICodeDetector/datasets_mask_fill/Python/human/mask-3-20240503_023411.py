# Linear <extra_id_0> Python


def linearSearch(array, n, x):

  <extra_id_1> # <extra_id_2> array sequencially
    for i in range(0, n):
  <extra_id_3>    <extra_id_4> (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found <extra_id_5> ", result)