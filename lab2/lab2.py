import re
import unittest

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        line = f.readline().strip()
        match = re.search(r'\[(.*?)\]', line)
        if match:
            return list(map(int, match.group(1).split(',')))
        else:
            raise ValueError("No array found in the file")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

        sorted_arr = []
        i = j = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sorted_arr.append(left_half[i])
                i += 1
            else:
                sorted_arr.append(right_half[j])
                j += 1
        while i < len(left_half):
            sorted_arr.append(left_half[i])
            i += 1
        while j < len(right_half):
            sorted_arr.append(right_half[j])
            j += 1

        return sorted_arr
    return arr
class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.arr = read_data_from_file('data.txt')

    def test_merge_sort(self):
        sorted_arr = merge_sort(self.arr[:])
        print(f"(Merge Sort): {sorted_arr}")
        self.assertEqual(sorted_arr, sorted(self.arr))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)