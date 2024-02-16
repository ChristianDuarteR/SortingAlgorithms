def quick_sort(array, smaller, higher):
    """
    Sort an array using recursion
    :param array: The array to sort
    :param smaller: Index of the first element on array (0)
    :param higher: Index of the last element of array
    :return:
    """
    if smaller < higher:
        # Dividing and select the pivot
        pivot = partition(array, smaller, higher)

        quick_sort(array, smaller, pivot - 1)
        quick_sort(array, pivot + 1, higher)


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


if __name__ == "__main__":
    arr = [4, 6, 2, 5, 8, 9, 5, 10]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
