def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = mid + 1
   while i <= mid and j <= end:
       if data[i] < data[j]:
           data_temp.append(data[i])
        i = i + 1
    else:
      if data[j] < data[i]:           i = i + 1
       else:
           data_temp.append(data[j])
           j = j + 1

    while i <= mid:
        data_temp.append(data[i])
  