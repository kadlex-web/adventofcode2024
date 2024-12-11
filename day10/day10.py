def check_valid_indexes(row, column, trail_map):
    if row < 0 or row > len(trail_map)-1 or column < 0 or column > len(trail_map)-1:
        return False
    return True

# Returns a list which contains the indexes to the nearest valid neighbors from a specific origin point
def get_neighbors(origin, trail_map, step):
    coordinates = [[1,0], [-1,0], [0,1], [0,-1]]
    neighbor_indexes = []
    if step == 9:
        return neighbor_indexes
    for value in coordinates:
        neighbor_row = origin[0] + value[0]
        neighbor_column = origin[1] + value[1]
        if check_valid_indexes(neighbor_row, neighbor_column, trail_map):
            neighbor_indexes.append([neighbor_row, neighbor_column])
    for index in neighbor_indexes:
        new_origin = [index[0], index[1]]
        new_step = step + 1
        return neighbor_indexes.extend(get_neighbors(new_origin, trail_map, new_step))

    '''for neighbor in neighbor_indexes:
        neighbor_x = neighbor[0]
        neighbor_y = neighbor[1]
        if check_valid_indexes(neighbor_x, neighbor_y, trail_map):
            neighbor_value = trail_map[neighbor_x][neighbor_y]
            if int(neighbor_value) == (starting_step + 1):
                new_origin = [neighbor_x, neighbor_y]
                next_step = starting_step + 1
                print(f"new_origin{new_origin} next step{next_step}")
                return get_trailhead_score(new_origin, next_step, trail_map)
            else:
                print("next value isnt gradual")'''
            
with open("sample.txt") as f:
    data = f.read()
    f.close()
    
# Trail Map Dataset
trail_map = []
for line in data.split("\n"):
    temp_list = []
    for slope in line:
        if isinstance(slope, str):
            temp_list.append(slope)
        else:
            int_slope = int(slope)
            temp_list.append(int_slope)
    trail_map.append(temp_list)
    

# Once we have the data in a format that is a list of lists.
# Create a list of origin points which are tuple type from the trail map
trailhead_indexes = []
for row in trail_map:
    row_index = trail_map.index(row)
    for i in range(0, len(row)):
        if trail_map[row_index][i] == 0:
            trailhead_indexes.append([row_index, i])
        
# I can than iterate through the list of trailhead indexes and call the get_trailhead_score function on each origin index which will give us a score per trailhead.
# The sum of all trailhead scores is the solution to the puzzle!
    


def main():
    print(get_neighbors([7,2], trail_map, 0))

main()