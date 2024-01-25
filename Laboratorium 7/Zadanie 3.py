import unittest

def quicksort(arr):
    for a in arr:
        if not isinstance(a, int):
            raise TypeError
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        mniejsze = [x for x in arr[1:] if x <= pivot]
        wieksze = [x for x in arr[1:] if x > pivot]
        return quicksort(mniejsze) + [pivot] + quicksort(wieksze)

class test_quicksort(unittest.TestCase):
    def test_quicksort_int(self):
        self.assertEqual(quicksort([5,8,2,-40,90,-2,0]), [-40,-2,0,2,5,8,90], "Lista nie jest prawodłowo posortowana")

    def test_quicksort_float(self):
        with self.assertRaises(TypeError):
            quicksort([5, 8, 2, -40, 90.9, -2, 0])

if __name__ == '__main__':
    unittest.main()