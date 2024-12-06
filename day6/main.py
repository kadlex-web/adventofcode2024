def find_start(data):
    for list in data:
        for char in list:
            if char == "^":
                return data.index(list), list.index(char)
            
def patrol(x, y, map, direction):
    if y == 0 and direction == "left":
        print("guard is about to leave the map on the left")
        map[x][y] = "X"
        return map
    elif x == 0 and direction == "up":
        print("guard is about to leave the map upward")
        map[x][y] = "X"
        return map      
    elif x == len(map) - 1 and direction == "down":
        print("guard is about to leave the map downward")
        map[x][y] = "X"
        return map
    elif y == len(map) - 1 and direction == "right":
        print("guard is about to leave the map to the right")
        map[x][y] = "X"
        return map

    else:
        map[x][y] = "X"
        if direction == "up":
            next_square = map[x-1][y]
            if next_square == "X" or next_square == ".":
                return patrol(x-1, y, map, direction)
            elif next_square == "#":
                return patrol(x, y, map, "right")
        elif direction == "right":
            next_square = map[x][y+1]
            if next_square == "X" or next_square == ".":
                return patrol(x, y+1, map, direction)
            elif next_square == "#":
                return patrol(x, y, map, "down")
        elif direction == "down":
            next_square = map[x+1][y]
            if next_square == "X" or next_square == ".":
                return patrol(x+1, y, map, direction)
            elif next_square == "#":
                return patrol(x, y, map, "left")
        elif direction == "left":
            next_square = map[x][y-1]
            if next_square == "X" or next_square == ".":
                return patrol(x, y-1, map, direction)
            elif next_square == "#":
                return patrol(x, y, map, "up")    

def total_squares(map):
    total_x = 0
    for list in map:
        for char in list:
            if char == "X":
                total_x += 1
    return total_x

with open ("day6.txt") as f:
    data = f.read()
    map = []
    for list in data.split("\n"):
        temp_list = []
        for string in list:
            new_str = string.strip()
            temp_list.append(new_str)
        map.append(temp_list)
    f.close()

def main():
    x, y = find_start(map)
    direction = "up"
    moving = True
    while moving:
        if y == 0 and direction == "left":
            print("guard is about to leave the map on the left")
            map[x][y] = "X"
            moving = False
        elif x == 0 and direction == "up":
            print("guard is about to leave the map upward")
            map[x][y] = "X"
            moving = False   
        elif x == len(map) - 1 and direction == "down":
            print("guard is about to leave the map downward")
            map[x][y] = "X"
            moving = False
        elif y == len(map) - 1 and direction == "right":
            print("guard is about to leave the map to the right")
            map[x][y] = "X"
            moving = False
        else:
            map[x][y] = "X"
            if direction == "up":
                next_square = map[x-1][y]
                if next_square == "X" or next_square == ".":
                    x = x-1
                elif next_square == "#":
                    direction = "right"  
            elif direction == "right":
                next_square = map[x][y+1]
                if next_square == "X" or next_square == ".":
                    y = y + 1
                elif next_square == "#":
                    direction = "down"
            elif direction == "down":
                next_square = map[x+1][y]
                if next_square == "X" or next_square == ".":
                    x = x + 1
                elif next_square == "#":
                    direction = "left"
            elif direction == "left":
                next_square = map[x][y-1]
                if next_square == "X" or next_square == ".":
                    y = y - 1
                elif next_square == "#":
                    direction = "up"
    return total_squares(map)
print(main())