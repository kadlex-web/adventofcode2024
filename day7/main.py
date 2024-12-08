'''Finds the list which only have one solution (the product of all values -- in the sample example, just the first case qualifies)
If the total in question exceeds the test value than we have something to work with, but if it comes out less it has no chance of working out?'''
def first_pass(equations_list):
    pass_list = []
    fail_list = []
    for list in equations_list:
        total = 1
        test_value = list[0]
        for value in list[1:]:
            total *= value
        if test_value == total:
            pass_list.append(list)
        else:
            fail_list.append(list)
    return pass_list, fail_list
'''check if any of the values are equal to summing everything -- if not -- the answer is somewhere in between'''
def second_pass(equations_list):
    pass_list = []
    fail_list = []
    for list in equations_list:
        total = 0
        test_value = list[0]
        for value in list[1:]:
            total += value
        if test_value == total:
            pass_list.append(list)
        else:
            fail_list.append(list)
    return pass_list, fail_list
'''If the length is odd run it forward -- if its even run it reverse'''
def check_test_value_even(list):
    test_value = list[0]
    working_list = list[::-1][:-1]
    
    while len(working_list) != 1:
        if test_value % working_list[0] == 0:
            test_value = test_value / working_list[0]
        else:
            test_value = test_value - working_list[0]
        working_list = working_list[1:]

    if test_value - working_list[0] == 0:
        return True
    else:
        return False
'''If the length is odd run it forward -- if its even run it reverse'''
def check_test_value_odd(list):
    test_value = list[0]
    working_list = list[:-1]
    while len(working_list) != 1:
        if test_value % working_list[0] == 0:
            test_value = test_value / working_list[0]
        else:
            test_value = test_value - working_list[0]
        working_list = working_list[1:]

    if test_value - working_list[0] == 0:
        return True
    else:
        return 0

'''Loads the equation data from the a file -- and converts it to a list of lists, as well as changing every string element
into an int element for comparison'''
with open("day7.txt") as f:
    equations_list = []
    data = f.read().split("\n")
    for list in data:
        temp_list = []
        for element in list.split(" "):
            temp_list.append(int(element.replace(":", "")))
        equations_list.append(temp_list)
    f.close()

if __name__ == "__main__":
    total = 0
    test_list = []
    fail_list = []
    for list in equations_list:
        if check_test_value_even(list):
            total += list[0]
            test_list.append(list)
        else:
            fail_list.append(list)
    print(fail_list)