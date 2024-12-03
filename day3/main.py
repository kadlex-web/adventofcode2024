import re


def find_all(str):
    expression = "mul\([0-9]+,[0-9]+\)"
    expression2 = "don't\(\)|do\(\)|mul\([0-9]+,[0-9]+\)"
    found_sequences = re.findall(expression2, str)
    return found_sequences


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


file = "day3.txt"
with open(file) as f:
    file_contents = f.read()


# Call print(main()) for solution
def main():
    total = 0
    matches = trim(find_all(file_contents))
    for expression in matches:
        total += multiply(expression)
    return total


# call print(main2()) for solution


def main2():
    matches = do_dont_replace(find_all(file_contents))
    trimmed_matches = trim(matches)
    print(mega_multiply(trimmed_matches))


main2()