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

def main():
    list_of_x = []
    values = []
    for x in range(0, len(new_data)):
        for y in range(0, len(new_data[x])):
            if find_x(x, y, new_data):
                list_of_x.append([x, y])
                
    for coords in list_of_x:
        values += find_m(coords[0], coords[1], "M", new_data)
        
    return values
print(main())