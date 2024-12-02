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

#sorting the two lists
left.sort()
right.sort()

#calculating the distance
distance = []
for num, num2 in zip(right, left):
    dist = num - num2
    distance.append(abs(dist))

print(sum(distance))
