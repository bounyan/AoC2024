with open("input.txt", "r") as f:
    textIn = f.read()

lines = textIn.strip().split("\n")

reports = []
for line in lines:
    if " " in line:
        nums = list(map(int, line.split(" ")))
        reports.append(nums)
    else:
        print("g3artha somewhere idk")

def is_safe_report(report):
    increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))
    valid_differences = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

    return (increasing or decreasing) and valid_differences

def can_be_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

safe_count = 0

for rep in reports:
    if is_safe_report(rep) or can_be_safe_with_dampener(rep):
        safe_count += 1

print(safe_count)
