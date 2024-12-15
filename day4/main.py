def get_hash_table(data):
    hash_table = {}
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            hash_table[(i, j)] = data[i][j]
    return hash_table

def find_x(x, y, new_data):
    value = new_data[x][y]
    if value == "X":
        return True
    else:
        return False
        
def find_m(x, y, new_char, new_data):
    checked_coords = []
    m_list = []
    if x == 0:
        checked_coords = [
            [x, y-1],[x, y+1],[x+1, y-1],[x+1, y],[x+1, y+1]
        ]
    elif y == 0:
        checked_coords = [
            [x-1, y], [x+1, y],[x-1, y+1],[x, y+1],[x+1, y+1]
        ]
    else:
        checked_coords = [
            [x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]
        ]
    for element in checked_coords:
        x = element[0]
        y = element[1]
        print(y)
        if new_data[x][y] == new_char:
            print(f"found m at {x},{y}")
    return m_list
        # We need to fix the index problem. While I accounted for an index of 0 becoming -1 I didn't account for the fact
        # that you could end up with an x or y value exceeding the length in either direction
        # Now take the run of coordinates (the arguments will determine what loop runs)
        # iterate through each list of coordinates and see what character it is. if the character is an M, than we have 'XM' so far
        # we need to save the location of each M to then pass to the next function

with open("sample.txt") as f:
    data = f.read().split("\n")
    f.close()

new_data = []
for list in data:
    temp_list = []
    for char in list:
        temp_list.append(char)
    new_data.append(temp_list)

sample_data = []
for list in new_data:
    temp_list = []
    for value in list:
        temp_list.append(value)
    sample_data.append(temp_list)

if __name__ == "__main__":
    table = get_hash_table(sample_data)
    x_list = []
    for key,value in table:
        if table[(key, value)] == "X":
            x_list.append((key, value))
    print(x_list)