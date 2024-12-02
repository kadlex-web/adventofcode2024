def difference(a, b):
    return int(a) - int(b)

file = "test2.txt"
file2 = "danger.txt"

# Initial Input
with open(file) as f:
    file_contents = f.read()

# Takes Output of Part I danger_list
with open(file2) as f:
    file_contents2 = f.read()

total_safe = 0
safe_list = []
danger_list = []

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
            elif diff > 0:
                print("unsafe")
                danger_count += 1

    elif int(my_list[0]) < int(my_list[-1]):
        #print("ascending")
        for i in range(1, len(my_list)):
            diff = difference(my_list[i], my_list[i - 1])
            if diff > 3 or diff < 1:
                #print("unsafe")
                danger_count += 1
            elif diff < 0:
                print("unsafe")
                danger_count += 1
                
    elif int(my_list[0]) == int(my_list[-1]):
        danger_count += 1
        
    if danger_count == 0:
        #print("safe levels")
        safe_list.append(my_list)
        total_safe += 1
        
    if danger_count == 1:
        danger_list.append(my_list)

# Output for Part I
"""print("--------------------------")
print(f"Safe Levels:{total_safe}")
print("--------------------------")"""

# Begin Part II
recovered_list = []
for line in file_contents2.split("\n"):
    my_list2 = line.split()
    print(my_list2)
    
    if int(my_list2[0]) > int(my_list2[-1]):
        print("descending")
        for i in range(1, len(my_list2)):
            diff = difference(my_list2[i], my_list2[i - 1])
            if diff < -3 or diff > -1:
                print(f"Unsafe levels found between index {i-1} and {i}")
                print("Analyzing if a fix is possible")
                level_check = abs(difference(my_list2[i-1], my_list2[i+1]))
                if level_check <= 3 and level_check >= 1:
                    print(f"I think we can fix that. Showing a difference of {level_check}")
                    recovered_list.append(my_list2)
                else:
                    print("Think it's too much -- this one is unsafe")
                   
    elif int(my_list2[0]) < int(my_list2[-1]):
        print("ascending")
        for i in range(1, len(my_list2)):
            diff = difference(my_list2[i], my_list2[i - 1])
            if diff > 3 or diff < 1:
                print(f"Unsafe levels found between index {i-1} and {i}")
                print("Analyzing if a fix is possible")
                level_check = abs(difference(my_list2[i-1], my_list2[i+1]))
                if level_check <= 3 and level_check >= 1:
                    print(f"I think we can fix that. Showing a difference of {level_check}")
                    recovered_list.append(my_list2)
                else:
                    print("Think it's too much -- this one is unsafe")
for item in recovered_list:
    print(item)