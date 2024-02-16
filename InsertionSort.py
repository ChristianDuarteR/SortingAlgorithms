def insertionSort(array):
    """
    An algorith which order the array comparing each element
    :param array: array to sort
    :return:
    """
    for j in range(1, len(array)):
        temp = array[j]
        i = j - 1

        while i >= 0 and array[i] > temp:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = temp


if __name__ == '__main__':
    arr = [7, 2, 5, 4, 9, 10, 1, 3]
    insertionSort(arr)
    print(arr)
