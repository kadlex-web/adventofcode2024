# Function which takes a given string and splits it into pieces of two. [23, 33, 13...40,2] in the example case
def split_string_by_two(string):
  return [string[i:i+2] for i in range(0, len(string), 2)]
# Function takes an id_number and a file + free space combination and generates the appropriate file + free space.
# For 23 : [0, 0, ., ., .,] / For 33: [1, 1, 1, ., ., .]
def create_file(id_number, file):
    sequence = []
    if len(file) == 2:
        for i in range(0, int(file[0])):
            sequence.append(id_number)
        for i in range(0, int(file[1])):
            sequence.append(".")
    else:
        for i in range(0, int(file[0])):
            sequence.append(id_number)
    return sequence
    
def build_sequence(sequence):
    new_sequence = []
    for value in sequence:
        if type(int):
            new_sequence.append(str(value))
        else:
            new_sequence.append(value)
    joined_string = "".join(new_sequence)
    return joined_string
    
# This would bring in a string of the sample text: "2333133121414131402"
with open("sample.txt") as f:
    data = f.read()
    f.close()
# This is a list of files plus the following free space sequence 
result = split_string_by_two(data)

# This is a loop going through the result list which will use a function called create_file which takes an id number(as noted by i) and file + free space combination as noted by result[i].
# The result is then extended onto the existing filesum_list
filesum_list = []
for i in range(0, len(result)):
    filesum_list.extend(create_file(i, result[i]))

print(build_sequence(filesum_list))