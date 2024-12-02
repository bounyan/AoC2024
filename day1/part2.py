from collections import Counter

#slicing the list
with open("input.txt", "r") as f:
    textIn = f.read()

lines = textIn.strip().split("\n")

right = []
left = []

for line in lines:
    if "   " in line:
        left_num, right_num = line.split("   ")
        left.append(int(left_num))
        right.append(int(right_num))
    else:
        print("g3artha somewhere")

right_count = Counter(right)

occur = {num: right_count[num] for num in left}

count = 0
for num in left:
    x = int(num) * int(occur[num])
    count += x

print(count)