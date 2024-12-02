def difference(a, b):
    return abs(a - b)

file = "test.txt"

with open(file) as f:
    file_contents = f.read()

for line in file_contents.split("\n"):
    i = 1
    while i < len(line.split()):
        diff = difference(int(line.split()[i-1]), int(line.split()[i]))
        i += 1
        print(diff)
