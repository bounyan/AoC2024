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

safe_count = 0

for rep in reports:
    if is_safe_report(rep):
        safe_count += 1

print(safe_count)
