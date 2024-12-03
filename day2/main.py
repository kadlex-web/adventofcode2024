def string_to_int_list(list):
    converted_list = []
    int_list = []
    for str in list:
        converted_list.append(str.split(" "))
        
    for list in converted_list:
        temp_list = []
        for str in list:
            temp_list.append(int(str))
        int_list.append(temp_list)    
    return int_list

def safety_check(a,b):
    expression = abs(a-b)
    print(expression)
    if (expression <= 3) and (expression >= 1):
        print("true")
        return True
    else:
        print("false")
        return False

def check_levels(list):
    if len(list) == 2:
        return True
    if safety_check(list[0], list[1]):
        check_levels(list[1:])
    else:
        return False
        
with open("test.txt") as f:
    file_contents = f.read()
    f.close()

def main():
    safe_list = []
    unsafe_list = []
    data = string_to_int_list(file_contents.split("\n"))
    
    for list in data:
        print(list)
        print(check_levels(list))
        if check_levels(list):
            safe_list.append(list)
        else:
            unsafe_list.append(list)
            
    #print(len(safe_list))
    #print(len(unsafe_list))
    
main()