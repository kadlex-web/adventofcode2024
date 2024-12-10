# Function which takes a given string and splits it into pieces of two. [23, 33, 13...40,2] in the example case
def split_string_by_two(string):
    return [string[i:i + 2] for i in range(0, len(string), 2)]


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


# Creates a string of the sequence
def build_sequence(sequence):
    new_sequence = []
    for value in sequence:
        if type(int):
            new_sequence.append(str(value))
        else:
            new_sequence.append(value)
    joined_string = "".join(new_sequence)
    return joined_string


# This calculates the number of free spaces(instances of "." created in the filesystem. Useful to determine how long the loop needs to run for moving the file blocks
def calculate_total_free_spaces(data):
    total = 0
    free_list = data[1::2]
    for num in free_list:
        total += int(num)
    return total
'''Returns a list of all the free space sequences'''
def get_free_spaces(data):
    free_list = []
    for value in data[1::2]:
        free_list.append(value)
    return free_list

def get_file_blocks(data):
    free_list = []
    for value in data[::2]:
        free_list.append(value)
    return free_list

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

# Now we have to fill the gaps and figure out an exit condition....
formatted_list = filesum_list.copy()
count = 0
current_tail = -1
while count < calculate_total_free_spaces(data):
    next_free = formatted_list.index(".")
    if formatted_list[current_tail] == ".":
        pass
    else:
        formatted_list[current_tail], formatted_list[
            next_free] = formatted_list[next_free], formatted_list[
                current_tail]
    count += 1
    current_tail -= 1

first_free = formatted_list.index(".")
sliced_list = formatted_list[0:first_free]
total = 0
for i in range(0, len(sliced_list)):
    total += (sliced_list[i] * i)

print(build_sequence(filesum_list))
'''Thoughts on a solution:
I could refactor the calculate_total_free_spaces function to give me a list of all the free space
gaps.
I could then compare the free space gaps to the values of each block in reverse order.
My hang-up is that I don't know the best way to denote each file_id value as something that could replace
blank gaps..?
If I constructed a dictionary of the file values how would it look?
The key would be the id number and the value store would be the string value of the filesum
Essentially {0: 23, 1: 33} etc etc.
What if I built a regex for each of my desired outcomes'''

'''Dictionary of dictionary? How does this help my plight?
Start with the last id_value in the set.
Loop through the set of free spaces to see if it fits anywhere.
If it does -- construct the sequence in that location and subtract from the available free space.
We want to pass the dictionary of values to a function and then construct the sequence live?

I think I'm getting too complicated with this.
{
id_value: {
    file_block: file[0],
    free_space: file[1],
    }
id_value: {
    file_block: file[0],
    free_space: file[1]}
    }'''

# Use the dictionary as a resource to see if values fit in certain places? Then create a regex expression using sub -- which takes a count.
# So I could take the id -- see if file_block is less than or equal to the free_space. if it is I could say replace the n characters with the id number
# using re.sub. the process could be repeated until all the values have been gone through.
# I could get the last index of the list which would correspond to the id value and then use the file blocks and free spaces list to test the condition.
# then use the re.sub to replace the appropriate number of "." with id numbers and replace all of the ending numbers with "."