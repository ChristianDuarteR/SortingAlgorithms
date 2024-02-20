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


if __name__ == '__main__':
    arr = [6, 2, 8, 3, 9, 10]
    print(arr)
    print(merge_sort(arr))
