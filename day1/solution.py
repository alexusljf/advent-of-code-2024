from input import list1, list2
from collections import Counter

# given 2 lists, sum up the differences between the two lists and return the sum
def part1(list1, list2):
    result = 0
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])
    return result

# given 2 lists, multiply the digit in list1 by number of occurence in list2 and return the sum of the result
def part2(list1, list2):
    result = 0
    counter2 = Counter(list2)
    for i in list1:
        if i in counter2.keys():
            result += i * counter2[i]
    return result

if __name__ == '__main__':
    print("Part 1: " + str(part1(list1, list2)))
    print("Part 2: " + str(part2(list1, list2)))