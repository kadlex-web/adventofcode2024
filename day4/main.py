def find_x(x, y, new_data):
    value = new_data[x][y]
    if value == "X":
        return True
    else:
        return False
        
def find_next(x, y, new_char, new_data):
    next_list = []
    if x == 0 and y == 0:
        search_list1 = [
            {"char": new_data[x][y+1],
            "loc_x": x,
            "loc_y": y+1}, 
             {"char": new_data[x+1][y],
             "loc_x": x+1,
             "loc_y": y}, 
            {"char": new_data[x+1][y+1],
            "loc_x": x+1,
            "loc_y": y+1}
        ]
        for element in search_list1:
            if element["char"] == new_char:
                next_list.append(element)
        # only add x and add y (we are at the first character at the top of the grid)
    elif x == 0:
        pass
        # only add x, can subtract and add y (we are in the first row)
    elif y == 0:
        pass
        # only add y, can substract or add x (we are in the first column)
    else:
        pass
        # we can perform any operation we want
    return next_list

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
    for x in range(0, len(new_data)):
        for y in range(0, len(new_data[x])):
            if find_x(x, y, new_data):
                print(f"Found an x at {x},{y}")
                
main()