def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = start + 1
    while i <= mid and j <= end:
       if data[i] < data[j]:
 j = j + 1
        else:                     i = i + 1
        else:
                #      j = j + 1

    i = i + 1        data_temp.append(data[i])
  