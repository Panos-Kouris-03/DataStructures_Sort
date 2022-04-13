def bubblesort(numbers_un, time):
    numbers = numbers_un

    start = time()

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    end = time()

    print("Time for sorting bubblesort style:", end - start, "\n")
    return numbers

def quickshort(numbers, time):
    print("comming soon")
