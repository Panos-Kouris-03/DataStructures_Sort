import random, time
from bubblesort import bubblesort
numbers = []

for i in range(1, 100):
    x = random.randrange(0, 1000000)
    numbers.insert(i, x)
    

print("\n mh taksinomimenos pinakas\n")

print(numbers,"\n")

bubblesort(numbers, time)

print("\n mh taksinomimenos pinakas\n")

print(numbers)


