'''Loads the equation data from the a file -- and converts it to a list of lists, as well as changing every string element
into an int element for comparison'''
with open("sample.txt") as f:
    equations_list = []
    data = f.read().split("\n")
    for list in data:
        temp_list = []
        for element in list.split(" "):
            element = element.replace(":", "")
            temp_list.append(int(element))
        equations_list.append(temp_list)
    f.close()

if __name__ == "__main__":
    print(equations_list)