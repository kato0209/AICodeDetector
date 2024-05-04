def merge(data, start, mid, end):
    <extra_id_0> []
    i = start
    j = mid + 1
 <extra_id_1>  while i <= mid and j <= end:
       <extra_id_2> data[i] < data[j]:
           <extra_id_3>   <extra_id_4>        i <extra_id_5> + 1
  <extra_id_6>     else:
   <extra_id_7>        data_temp.append(data[j])
 <extra_id_8>          j = j + 1

    while i <= mid:
        data_temp.append(data[i])
  