from functools import total_ordering
import re


def search(str):
    expression = "mul\([0-9]+,[0-9]+\)"
    found_sequences = re.findall(expression, str)
    return found_sequences


def trim(list):
    trimmed_list = []
    for str in list:
        new_str = re.sub("mul\(", "", str)
        new_str = re.sub(",", "*", new_str)
        new_str = re.sub("\)", "", new_str)
        trimmed_list.append(new_str)
    return trimmed_list


def multiply(str):
    values = str.split("*")
    return int(values[0]) * int(values[1])

file = "day3.txt"
with open(file) as f:
    file_contents = f.read()

# Call print(main()) for solution
def main():
    total = 0
    matches = trim(search(file_contents))
    for expression in matches:
        total += multiply(expression)
    return total

def main2():
    print("lets go")

main2()