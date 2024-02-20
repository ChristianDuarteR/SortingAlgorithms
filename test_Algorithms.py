import unittest

from Sorter import QuickSort, InsertionSort, MergeSort


class TestSorting(unittest.TestCase):
    def test_quickSort(self):
        test_arr_one = [6, 3, 1, 7, 9]
        test_arr_two = [9, 3]
        test_arr_three = [9, 3, 12, 5, 8, 15, 1, 6, 10, 7]
        test_arr_fourth = [50, 38, 27, 44, 35, 48, 15, 22, 11, 41, 6, 20, 30,
                           17, 32, 25, 40, 4, 13, 7, 18, 29, 46, 36, 42, 24, 1, 3, 47, 49]
        test_arr_five = [3, 15, 2, 7, 3, 8]
        QuickSort.quick_sort(test_arr_one, 0, len(test_arr_one) - 1)
        QuickSort.quick_sort(test_arr_two, 0, len(test_arr_two) - 1)
        QuickSort.quick_sort(test_arr_three, 0, len(test_arr_three) - 1)
        QuickSort.quick_sort(test_arr_fourth, 0, len(test_arr_fourth) - 1)
        QuickSort.quick_sort(test_arr_five, 0, len(test_arr_five) - 1)

        self.assertEquals(test_arr_one, [1, 3, 6, 7, 9])
        self.assertEquals(test_arr_two, [3, 9])
        self.assertEquals(test_arr_three, [1, 3, 5, 6, 7, 8, 9, 10, 12, 15])
        self.assertEquals(test_arr_fourth, [1, 3, 4, 6, 7, 11, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30,
                                            32, 35, 36, 38, 40, 41, 42, 44, 46, 47, 48, 49, 50])
        self.assertEquals(test_arr_five, [2, 3, 3, 7, 8, 15])

    def test_mergeSort(self):
        test_arr_one = [6, 3, 1, 7, 9]
        test_arr_two = [9, 3]
        test_arr_three = [9, 3, 12, 5, 8, 15, 1, 6, 10, 7]
        test_arr_fourth = [50, 38, 27, 44, 35, 48, 15, 22, 11, 41, 6, 20, 30,
                           17, 32, 25, 40, 4, 13, 7, 18, 29, 46, 36, 42, 24, 1, 3, 47, 49]
        test_arr_five = [3, 15, 2, 7, 3, 8]

        self.assertEquals(MergeSort.merge_sort(test_arr_one), [1, 3, 6, 7, 9])
        self.assertEquals(MergeSort.merge_sort(test_arr_two), [3, 9])
        self.assertEquals(MergeSort.merge_sort(test_arr_three), [1, 3, 5, 6, 7, 8, 9, 10, 12, 15])
        self.assertEquals(MergeSort.merge_sort(test_arr_fourth),
                          [1, 3, 4, 6, 7, 11, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30,
                           32, 35, 36, 38, 40, 41, 42, 44, 46, 47, 48, 49, 50])
        self.assertEquals(MergeSort.merge_sort(test_arr_five), [2, 3, 3, 7, 8, 15])

    def test_insertionSort(self):
        test_arr_one = [6, 3, 1, 7, 9]
        test_arr_two = [9, 3]
        test_arr_three = [9, 3, 12, 5, 8, 15, 1, 6, 10, 7]
        test_arr_fourth = [50, 38, 27, 44, 35, 48, 15, 22, 11, 41, 6, 20, 30,
                           17, 32, 25, 40, 4, 13, 7, 18, 29, 46, 36, 42, 24, 1, 3, 47, 49]
        test_arr_five = [3, 15, 2, 7, 3, 8]
        InsertionSort.insertionSort(test_arr_one)
        InsertionSort.insertionSort(test_arr_two)
        InsertionSort.insertionSort(test_arr_three)
        InsertionSort.insertionSort(test_arr_fourth)
        InsertionSort.insertionSort(test_arr_five)

        self.assertEquals(test_arr_one, [1, 3, 6, 7, 9])
        self.assertEquals(test_arr_two, [3, 9])
        self.assertEquals(test_arr_three, [1, 3, 5, 6, 7, 8, 9, 10, 12, 15])
        self.assertEquals(test_arr_fourth, [1, 3, 4, 6, 7, 11, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30,
                                            32, 35, 36, 38, 40, 41, 42, 44, 46, 47, 48, 49, 50])
        self.assertEquals(test_arr_five, [2, 3, 3, 7, 8, 15])


if __name__ == 'main':
    unittest.main()
