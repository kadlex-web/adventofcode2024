def difference(a, b):
    return int(a) - int(b)

file = "adventofcodeday2.txt"
file2 = "danger.txt"

#Initial Input
with open(file) as f:
    file_contents = f.read()

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

#Begin Part II
recovered_list = []
final_list = []
temp_list = []

for line in danger_list:
    temp_list.append(line)
    if int(line[0]) > int(line[-1]):
        print("descending")
        for i in range(1, len(line)):
            diff = difference(line[i], line[i - 1])

            if diff < -3 or diff > -1:
                print(f"Unsafe levels found between index {i-1} and {i}")
                print(f"{i+1}      {len(line)}")
                if (i + 1) == len(line):
                    print("I think we can fix that. The bad level is last in the sequence.\n")
                    recovered_list.append(line)
                    break

                level_check = abs(difference(line[i-1], line[i+1]))
                if level_check <= 3 and level_check >= 1:
                    print(f"I think we can fix that. Showing a difference of {level_check}\n")
                    recovered_list.append(line)
                else:
                    print("Think it's too much -- this one is unsafe\n")
                    final_list.append(line)
                 
    elif int(line[0]) < int(line[-1]):
        print("ascending")
        for i in range(1, len(line)):
            diff = difference(line[i], line[i - 1])

            if diff > 3 or diff < 1:
                print(f"Unsafe levels found between index {i-1} and {i}")
                print(f"{i + 1}      {len(line)}")
                if (i + 1) == len(line):
                    print("I think we can fix that. The bad level is last in the sequence.\n")
                    recovered_list.append(line)
                    break
                level_check = abs(difference(line[i-1], line[i+1]))
                if level_check <= 3 and level_check >= 1:
                    print(f"I think we can fix that. Showing a difference of {level_check}\n")
                    recovered_list.append(line)
                else:
                    print("Think it's too much -- this one is unsafe\n")
                    final_list.append(line)
    else:
        print("I think the lines are equal")
        final_list.append(line)

print(len(temp_list))
print(len(safe_list))
print(len(danger_list))
print(len(recovered_list))
print(len(final_list))

for list in final_list:
    print(list)