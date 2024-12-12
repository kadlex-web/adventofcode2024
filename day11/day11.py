'''
Stone Rules:
    All stones have a completely preserved order.
    When we blink the following can happen.
    If a stone is engraved with a 0 -- it becomes a 1.
    If a stone is engraved with even number digits it splits. The left half of the split goes to a left stone, the right right half to a right stone.
        Leading zeroes are cut completely. So 00000 becomes 0.
    If none of the rules apply we multiply the stone by 2024.
    How many stones do we have after 25 steps.

What's the algorithm?
    We start with an arrangement of stones -- which we can load into a list. We want to preserve the type.
        I can simply create a starting list which is equal to our stone arrangement.
    We can loop through each stone in the list and perform an analysis on it. We only do this while the number of blinks is less than 25.
    If a stone is 0:
        take the original stone and transform it's value to 1
    If a stone isn't 0 and it contains an even number of digits than we create two new stones. 
        Each stone has a value equal to half the split.
    If a stone isn't 0 and doesn't have an even number of integer digits. We multiply it's value by 2024.
    Increment up the step by 1 and repeat.
  '''

def calculate_new_arrangement(stone_list, stone_dict, blink=0):
    if blink == 5:
        return stone_list
    new_stones_list = []

    for stone in stone_list:
        if stone in stone_dict:
            stone_dict.get(stone).append(new_stones_list)
        else:
            str_stone = str(stone)
            if len(str_stone) % 2 == 0:
                stone_length = int(len(str_stone)/2)
                left_stone = int(str_stone[0:(stone_length)])
                right_stone = int(str_stone[(stone_length):len(str_stone)])
                new_stones_list.append(left_stone)
                new_stones_list.append(right_stone)
            else:
                new_stone = int(stone) * 2024
                stone_dict[stone] = new_stone
                new_stones_list.append(new_stone)
    return calculate_new_arrangement(new_stones_list, stone_dict, blink + 1)

stone_dict = {
    0 : 1,
}
starting_list = [1117, 0, 8, 21078, 2389032, 142881, 93, 385]
stone1 = [1117]
stone2 = [0]
stone3 = [8]
stone4 = [21078]
stone5 = [2389032]
stone6 = [142881]
stone7 = [93]
stone8 = [385]
sample_list = [125, 17]

def main():
    return len(calculate_new_arrangement(sample_list))

print(main())

'''Possibility for Part II -- break up each stone into an individual stone and calculate its 75 step
sequence -- then add all of them together

The above doesn't work lol -- the number of computations is too great (2x10E22)
But what I think might work is creating a dictionary of all the stones and their values which is build through iteration
Essentially if a stone doesnt have a value we calculate what it's value would be (maybe convert the loop to a function
Then if it does return the value and append to the list?
I think hashmap searching is a O(1) or O(n) at worst whereas what I'm doing is O(n^2) I THINK
Could use dictionary.setdefault to ensure we get the value and if not we get to create the desired key or defaultdict might be better?
Honestly? Regular dictionary might be better'''