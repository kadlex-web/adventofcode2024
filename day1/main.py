with open("day1input.csv") as f:
    file_contents = f.read().split()

list1 = []
list2 = []
for i in range(0, len(file_contents)):
    if i % 2 == 0:
        list1.append(int(file_contents[i]))
    else:
        list2.append(int(file_contents[i]))
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

total = 0
for i in range(0, len(sorted_list1)):
    total += abs(sorted_list1[i] - sorted_list2[i])

total2 = 0
for x in sorted_list1:
    multiple = 0
    for y in sorted_list2:
        if x == y:
            multiple += 1
    total2 += (x * multiple)

print(total2)
        