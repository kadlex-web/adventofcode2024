import re


# could be refactored to take two arguments: str and regex_expression, would help break up the puzzle into parts
def find_all(str):
    expression = "mul\([0-9]+,[0-9]+\)"
    expression2 = "don't\(\)|do\(\)|mul\([0-9]+,[0-9]+\)"
    found_sequences = re.findall(expression2, str)
    return found_sequences

# Function takes a list as input. analyzes all the strings in the list and alters the dos and donts to "keywords" which can be analyzed in mega_multiply method. Returns a list of transformed dos/donts but unaltered mul() statements
def do_dont_replace(list):
    new_list = []
    for str in list:
        if str == "do()":
            new_str = str.replace("do()", "on")
            new_list.append(new_str)
        elif str == "don't()":
            new_str = str.replace("don't()", "off")
            new_list.append(new_str)
        else:
            new_list.append(str)
    return new_list

# Method trims the mul() statements so they are represented as XXX*XXX or some similar format. Comma could be left in to save a line of code. Wonder if the trimming could be refactored to one line
def trim(list):
    trimmed_list = []
    for str in list:
        new_str = re.sub("mul\(", "", str)
        new_str = re.sub(",", "*", new_str)
        new_str = re.sub("\)", "", new_str)
        trimmed_list.append(new_str)
    return trimmed_list

# use string.split to split string at the * character and then converts strings to int and multiplys them, returning the value
def multiply(str):
    values = str.split("*")
    return int(values[0]) * int(values[1])

# Evaluates a list item to see if it is an expression or it alters state. then checks to see if it can do the operation based on state and performs it if possible
def mega_multiply(list):
    do_state = True
    total = 0
    for expression in list:
        if expression == "on":
            do_state = True
        elif expression == "off":
            do_state = False
        else:
            if do_state:
                total += multiply(expression)
    return total

with open("day3.txt") as f:
    file_contents = f.read()

# Call print(main()) for solution / change expression in find_all
def main():
    total = 0
    matches = trim(find_all(file_contents))
    for expression in matches:
        total += multiply(expression)
    return total


# call print(main2()) for solution
def main2():
    matches = trim(do_dont_replace(find_all(file_contents)))
    return mega_multiply(matches)

print(main2())
