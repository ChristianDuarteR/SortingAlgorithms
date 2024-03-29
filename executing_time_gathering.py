import time
import algorithms
import constants
import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    return [
        # --> Si esta ordenado el peor llega a ser MergeSort
        take_time_for_algorithm(samples, lambda arr: algorithms.quick_sort(arr, 0, len(arr) - 1)),
        take_time_for_algorithm(samples, algorithms.merge_sort),
        take_time_for_algorithm(order(samples), algorithms.insertionSort),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""

def order(matrix):
    for array in matrix:
        array.sort()
    return matrix

def take_time_for_algorithm(samples_array, sorting_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]