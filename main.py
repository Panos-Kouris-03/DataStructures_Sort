from random import randrange
from time import time
from bubblesort import bubblesort, quickshort

for j in range(100, 1100, 100):

    numbers_unsorted = []
    numbers_sorted = []

    for i in range(1, j):

        x = randrange(0, 100)
        numbers_unsorted.insert(i, x)

    print("senario:", j/100)
    print("Unsorted Array", numbers_unsorted, "\n")

    numbers_sorted = bubblesort(numbers_unsorted, time), quickshort(numbers_unsorted,time)


    print("unSorted:", numbers_unsorted, "\n")
    print("Sorted:", numbers_sorted, "\n")