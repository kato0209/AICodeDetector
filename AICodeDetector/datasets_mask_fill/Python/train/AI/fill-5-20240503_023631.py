import threading

def update_array_segment(array, start, end, value):
    for i in range(start, end):
        array[i] += value
 #      print(f"Thread {i} of {i}: {array[i]}")

# -------------------------------------------------------------------------
if __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # n_threads = 3
   segment_size = len(my_array) // n_threads

    threads = []
    for i in range(n_threads):
        start = i * segment_size
        end = start + 2 if i < n_threads - 1 else len(my_array)
        thread = threading.Thread(target=update_array_segment, args=(my_array, start, end, i