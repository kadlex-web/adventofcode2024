import collections
# In theory this should generate all the neighbors around a given node, check if they are valid locations and then return a list of valid neighbors for a given point
    # In most cases - this should be 8 data points, but corners and edges should generate much less
def get_valid_neighbors(x,y, hash_table):
    final_neighbors_list = []
	neighbor_coordinates = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
	neighbors_list = list(map(lambda list: [list[0] + x, list[1] + y], neighbor_coordinates))
    de = collections.deque(neighbors_list)
    while len(de) > 1:
        coord = de.popleft()
        # need to fix second conditional piece because we don't have the parameters of the graph
        if coord[0] >= 0 and coord[0] <= len(data_table - 1):
            if coord[1] >= 0 and coord[1] <= len(data_table -1):
                coord.append(final_neighbors_list)
                
# Do a deque for each step and feed the new neighbors input each time?
# Kinda just recursion tho
