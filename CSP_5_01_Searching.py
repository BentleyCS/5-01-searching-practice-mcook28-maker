import random
from random import randint
import random

def randomSearch(items: list, target) -> int:
    tries = 0
    while True:
        tries += 1
        i = random.randint(0, len(items) - 1)
        if items[i] == target:
            print("Found it in", tries, "tries")
            return i


print(randomSearch([1,3,5,9,7,12,11,10,2,4,6,8], 5))


def linearSearch(items: list, target) -> tuple[int, int]:
    checks = 0
    for i in range(len(items)):
        checks += 1
        if items[i] == target:
            return i, checks
    return -1, checks


print(linearSearch([1,3,5,9,7,12,11,10,2,4,6,8], 5))


def binarySearch(items: list, target) -> tuple[int, int]:
    low = 0
    high = len(items) - 1
    checks = 0

    while low <= high:
        checks += 1
        mid = (low + high) // 2

        if items[mid] == target:
            return mid, checks
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, checks


# IMPORTANT: binary search requires a sorted list
sorted_items = sorted([1,3,5,9,7,12,11,10,2,4,6,8])
print(binarySearch(sorted_items, 5))