from random import randrange
from time import time
from sorts import bubblesort, shell_sort, bubblesort_number_sorting

time_bubblesort = 0
time_shell_sort = 0

for j in range(100, 1100, 100):

    numbers_unsorted = []
    numbers_sorted = []

    for i in range(1, j):

        x = randrange(0, 100)
        numbers_unsorted.insert(i, x)

    print("senario:", j/100)
    print("Unsorted Array", numbers_unsorted, "\n")

    numbers_sorted = bubblesort_number_sorting(numbers_unsorted)
    
    time = bubblesort(numbers_unsorted)
    time_bubblesort+=time
    print("\ntime for bubblesort: ", time, "\n")
    
    time = shell_sort(numbers_unsorted)
    time_shell_sort+=time
    print("\ntime for shell sort: ", time, "\n")

    print("Sorted:", numbers_sorted, "\n")