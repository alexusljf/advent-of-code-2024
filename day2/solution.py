from input import reportsList


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def part1(reportsList):
    safe = 0
    for report in reportsList:
        if(is_safe(report)):
            safe += 1
    return safe

# we can now remove 1 item from an unsafe list to make it safe 
def part2(reportsList):
    safe = 0
    for report in reportsList:
        if(is_safe(report)):
            safe += 1
        else:
            saveable = False
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if is_safe(new_report):
                    saveable = True
                    break
            if saveable:
                safe += 1
    return safe

# helper function to check if safe
def is_safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    print(part1(reportsList))
    print(part2(reportsList))