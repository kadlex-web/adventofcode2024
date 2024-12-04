def find_x(x, y, new_data):
    value = new_data[x][y]
    if value == "X":
        return True
    else:
        return False
        
def find_m(x, y, new_char, new_data):
    if x == 0:
        checked_coords_x = [
            [x, y-1],[x, y+1],[x+1, y-1],[x+1, y],[x+1, y+1]
        ]
        return checked_coords_x
    elif y == 0:
        checked_coords_y = [
            [x-1, y], [x+1, y],[x-1, y+1],[x, y+1],[x+1, y+1]
        ]
        return checked_coords_y
    else:
        checked_coords_any = [
            [x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]
        ]
        return checked_coords_any
        
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