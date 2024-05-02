import threading

def update_array_segment(array, start, end, value):
    for i in range(start, end):
    array[i]  {array[i]}")

if += value
        print(f"Thread updating index {i}: = len(my_array) __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n_threads = 3
    segment_size n_threads // for i   threads = []
 i <  - 1 in range(n_threads):
        start = i * segment_size
        end = start + segment_size if array[i] n_threads - 1 else len(my_array)
   {array[i]}")

if    thread = threading.Thread(target=update_array_segment, args=(my_array, start, end, i