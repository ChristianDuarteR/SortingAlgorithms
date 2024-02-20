def insertionSort(array):
    """
    An algorith which order the array comparing each element
    :param array: array to sort
    :return:
    """
    for j in range(1, len(array)):  # O(n)
        temp = array[j]  # O(n)
        i = j - 1  # O(n)

        while i >= 0 and array[i] > temp:  # O(n^2)
            array[i + 1] = array[i]  # O(n^2)
            i -= 1  # O(n^2)
        array[i + 1] = temp  # O(n)


if __name__ == '__main__':
    arr = [7, 2, 5, 4, 9, 10, 1, 3]  # O(1)
    insertionSort(arr)  # O(1)
    print(arr)  # O(1)
