import threading

class ArrayBlocker:
    def __init__(self, array):
        self.array = array
        self.lock = threading.Lock()

    def update_element(self, index, value):
        with self.lock:
            if 0 <= index < len(self.array):
                self.array[index] = value
                print(f"Array updated at index {index}: {self.array}")
            else:
                print(f"Index {index} is out of bounds")

def thread_function(array_blocker, index, value):
    array_blocker.update_element(index, value)

# テストコード
if __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5]
    array_blocker = ArrayBlocker(my_array)

    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_function, args=(array_blocker, i, i * 10))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final array state: {my_array}")
