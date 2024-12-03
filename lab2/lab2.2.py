import unittest

def insertion_sort(arr, n):
    if n <= 1:
        return arr
    insertion_sort(arr, n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last
    return arr

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    return max(left_max, right_max)

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        numbers = list(map(int, file.readline().strip().split()))
    return n, numbers

class TestAlgorithms(unittest.TestCase):
    
    def test_insertion_sort(self):
        arr = [12, 11, 13, 5, 6]
        self.assertEqual(insertion_sort(arr, len(arr)), [5, 6, 11, 12, 13])
        
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 8, 9]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 8), 4)
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 7), -1)
        
    def test_find_max(self):
        arr = [1, 2, 3, 4, 8, 9]
        self.assertEqual(find_max(arr, 0, len(arr)-1), 9)
        
    def test_read_data_from_file(self):
        n, numbers = read_data_from_file('data2.txt')
        self.assertEqual(n, 5)
        self.assertEqual(numbers, [1, 2, 3, 4, 8, 9])

if __name__ == '__main__':
    unittest.main()
