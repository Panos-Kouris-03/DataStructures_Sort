from time import time


def bubblesort(numbers_un):
    numbers = numbers_un.copy()

    start = time()

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    end = time()

    total_time = end - start

    return total_time


def bubblesort_number_sorting(numbers_unsorted):
    numbers = numbers_unsorted.copy()

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def shell_sort(numbers_unsorted):
    numbers = numbers_unsorted.copy()

    start = time()

    table_length = len(numbers_unsorted)

    gap = len(numbers_unsorted) // 2

    while gap > 0:

        for i in range(gap, table_length):

            temp = numbers[i]
            j = i

            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap

            numbers[j] = temp
        gap = gap // 2

    end = time()
    print("list: ", numbers)

    return end - start


def heap_sort(numbers_unsorted):
    numbers_to_sort = numbers_unsorted.copy()

    table_length = len(numbers_unsorted)

    time_start = time()

    def thinks_in_to_place(table_array, interger, tl):
        start = 2 * interger
        end = (2 * interger) + 1

        if start <= tl and table_array[start] > table_array[interger]:
            largest = start
        else:
            largest = interger
        if end < tl and table_array[end] < table_array[largest]:
            largest = end
        if largest != interger:
            temp = table_array[interger]
            table_array[interger] = table_array[largest]
            table_array[largest] = temp

    for i in range(table_length // 2 - 1, -1, -1):
        thinks_in_to_place(numbers_to_sort, i, table_length)

    for i in range(table_length - 1, 0, -1):
        numbers_to_sort[i], numbers_to_sort[0] = numbers_to_sort[0], numbers_to_sort[i]
        thinks_in_to_place(numbers_to_sort, i, table_length)

    time_stop = time()
    return time_stop - time_start
