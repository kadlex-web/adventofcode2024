def difference(a, b):
    return int(a) - int(b)

file = "test2.txt"

with open(file) as f:
    file_contents = f.read()

total_safe = 0
safe_list = []

for line in file_contents.split("\n"):
    my_list = line.split()
    danger_count = 0

    if int(my_list[0]) > int(my_list[-1]):
        #print("descending")
        for i in range(1, len(my_list)):
            diff = difference(my_list[i], my_list[i - 1])
            if diff < -3 or diff > -1:
                #print("unsafe")
                danger_count += 1

    elif int(my_list[0]) < int(my_list[-1]):
        #print("ascending")
        for i in range(1, len(my_list)):
            diff = difference(my_list[i], my_list[i - 1])
            if diff > 3 or diff < 1:
                #print("unsafe")
                danger_count += 1
        
    if danger_count == 0:
        #print("safe levels")
        safe_list.append(my_list)
        total_safe += 1

print("--------------------------")
print(f"Safe Levels:{total_safe}")
print("--------------------------")

for item in safe_list:
    print(item)