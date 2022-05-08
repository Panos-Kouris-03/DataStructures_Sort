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

    total_time = end - start

    return total_time
