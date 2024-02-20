def quick_sort(array, smaller, higher):
    """
    Sort an array using recursion
    :param array: The array to sort
    :param smaller: Index of the first element on array (0)
    :param higher: Index of the last element of array
    :return:
    """
    if smaller < higher:  # O(1)
        # Dividing and select the pivot
        pivot = partition(array, smaller, higher)   # O(1)

        quick_sort(array, smaller, pivot - 1)   # O(n/2)
        quick_sort(array, pivot + 1, higher)    # O(n/2)


def partition(array, smaller, higher):
    """

    :param array: divide an array around a pivot and return the final position of the pivot
    :param smaller: Index of the first element on array (0)
    :param higher: Index of the last element of array
    :return: (int) the final position of pivot
    """
    # Selecting pivot like the higher
    pivot = array[higher]

    # Where is the smallest number
    i = smaller - 1

    for j in range(smaller, higher):
        if array[j] <= pivot:
            # New Smaller
            i = i + 1
            # Switching the smaller and bigger on array
            (array[i], array[j]) = (array[j], array[i])

    # Switching the pivot on the final iteration so the pivot is in the middle on array
    (array[i + 1], array[higher]) = (array[higher], array[i + 1])

    # Return the new pilot which is the element next to the last pivot
    return i + 1


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

def merge_sort(arr):
    """
    Function which uses recursion to order the array
    :param arr:  to sort
    :return: a sorted array
    """

    # If we don't have more elements on array is sorted
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge the parts to get a new array
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """

    :param left: the left sub_array part
    :param right: the right sub_array part
    :return: a new array which is sorted
    """
    newArray = []

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0] > 0:
            newArray.append(right[0])
            right.pop(0)
        else:
            newArray.append(left[0])
            left.pop(0)

    # The condition is going to break when one of the two arrays get empty, so complete the sorted array
    while len(left) > 0:
        newArray.append(left[0])
        left.pop(0)
    while len(right) > 0:
        newArray.append(right[0])
        right.pop(0)

    return newArray