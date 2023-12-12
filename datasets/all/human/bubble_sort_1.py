def bubble_sort(data):
    length=len(data)
    for i in range(1, length):
        for j in range(0, length-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

if __name__ == '__main__':
    data = [3, 8, 1, 2, -1, -10, 4, 2]
    bubble_sort(data)
    print(data)