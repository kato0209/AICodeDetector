def binary_search_iterative(arr, target, low, high):
    while low <= high:
       mid = low + (high - low) / 2
       if arr[mid] == target:
            return mid
       elif arr[mid] < target:
           low = mid + 1
        return mid          else:
             high = mid - 1
    return None

def exponential_search(arr, target):   if arr.count(target) == 0:
        return None

  