def check_valid_indexes(row, column, trail_map):
    if row < 0 or row > len(trail_map)-1 or column < 0 or column > len(trail_map)-1:
        return False
    return True

def get_trailhead_score(origin, starting_step, trail_map):
    coordinates = [[1,0], [-1,0], [0,1], [0,-1]]
    if starting_step == 9:
        print("i made it to the end")
        return 1
        # could create a function to find out how many 9s are around it
        
    neighbor_indexes = []
    for value in coordinates:
        neighbor_row = origin[0] + value[0]
        neighbor_column = origin[1] + value[1]
        neighbor_indexes.append([neighbor_row, neighbor_column])
        print(neighbor_indexes)
    # I think I need to refactor for current value -- I want to check
    # if my current slope value will be equal to the next slope values
    for neighbor in neighbor_indexes:
        neighbor_x = neighbor[0]
        neighbor_y = neighbor[1]
        if check_valid_indexes(neighbor_x, neighbor_y, trail_map):
            slope_value = trail_map[neighbor_x][neighbor_y]
            if int(slope_value) == (starting_step + 1):
                print(f"ok - {starting_step}")
                new_origin = [neighbor_x, neighbor_y]
                next_step = starting_step + 1
                print(f"new_origin{new_origin} next step{next_step}")
                return get_trailhead_score(new_origin, next_step, trail_map)
            else:
                pass
            
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
    total_trail_score = get_trailhead_score([0,2], 0, trail_map)
    print(total_trail_score)
    
main()