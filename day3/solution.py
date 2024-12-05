from input import results

# matches has list of tuples with the following format: (number1, number2) both are strings
# want to return the sum of the product of the two numbers

def part1(matches):
    sum = 0
    for match in matches:
        if match == 'do()' or match == "don't()":
            continue
        print(match[1:-1])
        numbers = match[1:-1].split(',')
        sum += int(numbers[0]) * int(numbers[1])
    return sum

# there are do() and don't() that disable and enable mul operations
def part2(matches):
    sum = 0
    flag = True
    for match in matches:
        if match == 'do()':
            flag = True
            continue
        elif match == "don't()":
            flag = False
            continue
        # print(match[1:-1])
        if flag:
            numbers = match[1:-1].split(',')
            sum += int(numbers[0]) * int(numbers[1])
    return sum

if __name__ == '__main__':
    print(part1(results))
    print(part2(results))