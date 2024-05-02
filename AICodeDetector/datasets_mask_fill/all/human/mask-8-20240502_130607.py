def bubble_sort(data):
  <extra_id_0> length=len(data)
    for i in range(1, length):
    <extra_id_1>   for j <extra_id_2> length-i):
            if data[j] > data[j+1]:
          <extra_id_3>     data[j], data[j+1] = data[j+1], data[j]

if __name__ == '__main__':
 <extra_id_4>  data = [3, 8, 1, 2, -1, <extra_id_5> 2]
    bubble_sort(data)
    print(data)