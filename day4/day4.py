# In theory this should generate all the neighbors around a given node, check if they are valid locations and then return a list of valid neighbors for a given point
    # In most cases - this should be 8 data points, but corners and edges should generate much less
def get_hash_table(data):
    hash_table = {}
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            hash_table[(i, j)] = data[i][j]
    return hash_table
    
def check_string(x, y, hash_table):
    count = 0
    # given an origin point (let's use 0,4)
    # apply each possible transform to it
    transform_list = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
# this is lazy repetitive code and I just don't have the heart to refactor
# yes of course it could be recursion
    for transform in transform_list:
        mod1 = transform[0] + x
        mod2 = transform[1] + y
        key = (mod1, mod2)
        
        if key in hash_table:
            str = hash_table[(x,y)] + hash_table[(mod1, mod2)]
            if str == "XM":
                mod3 = transform[0] + mod1
                mod4 = transform[1] + mod2
                key2 = (mod3, mod4)
                
                if key2 in hash_table:
                    str2 = str + hash_table[(mod3, mod4)]
                    if str2 == "XMA":
                        mod5 = transform[0] + mod3
                        mod6 = transform[1] + mod4
                        key3 = (mod5, mod6)
                        if key3 in hash_table:
                            str3 = str2 + hash_table[(mod5, mod6)]
                            if str3 == "XMAS":
                                count += 1
    return count

def check_crossmas(x, y, hash_table):
    def get_corners_dir(x,y):
        corner_coordinates = [(-1,-1), (-1, 1), (1, -1), (1,1)]
        corner_dir = {}
        directions = ["NW", "NE", "SW", "SE"]
        corners = list(map(lambda n: (n[0] + x, n[1] + y), corner_coordinates))

        for i in range(0, len(directions)):
            corner_dir[directions[i]] = hash_table[corners[i]]
        return corner_dir
    
    if x < 1 or y < 1:
        return 0
    if x > 138 or y > 138:
        return 0
    
    corner_dict = get_corners_dir(x,y)
    if list(corner_dict.values()).count("M") == 2:
        if corner_dict["NW"] == "M" and corner_dict["SW"] == "M":
            if corner_dict["NE"] == "S" and corner_dict["SE"] == "S":
                return 1
            else:
                return 0
        elif corner_dict["NE"] == "M" and corner_dict["NW"] == "M":
            if corner_dict["SE"] == "S" and corner_dict["SW"] == "S":
                return 1
            else:
                return 0
        elif corner_dict["NE"] == "M" and corner_dict["SE"] == "M":
            if corner_dict["NW"] == "S" and corner_dict["SW"] == "S":
                return 1
            else:
                return 0
        elif corner_dict["SE"] == "M" and corner_dict["SW"] == "M":
            if corner_dict["NE"] == "S" and corner_dict["NW"] == "S":
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0



with open("data.txt") as f:
    data = f.read().split("\n")
    f.close()

new_data = []
for lst in data:
    temp_list = []
    for char in lst:
        temp_list.append(char)
    new_data.append(temp_list)

sample_data = []
for lst in new_data:
    temp_list = []
    for value in lst:
        temp_list.append(value)
    sample_data.append(temp_list)

if __name__ == "__main__":
    table = get_hash_table(sample_data)
    x_list = []
    a_list = []

    for key,value in table:
        if table[(key, value)] == "X":
            x_list.append((key, value))

    for key,value in table:
        if table[(key, value)] == "A":
            a_list.append((key, value))

    xmas_count = 0
    for value in x_list:
        xmas_count += check_string(value[0], value[1], table)
    #print(xmas_count)

    crossmas_count = 0
    for value in a_list:
        crossmas_count += check_crossmas(value[0], value[1], table)
    print(crossmas_count)