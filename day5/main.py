'''Use a for loop to generate a dictionary where given a pair (in list form, so they can be accessed), if the key value exists append the value to the values. otherwise create the key and store the value in it'''
def change_to_dict(unsorted_rules):
    rules_dictionary = {}
    
    for pair in unsorted_rules:
        # print(pair)
        pair_x = pair[0]
        pair_y = pair[1]
        if pair_x in rules_dictionary: 
            #print("old key")
            rules_dictionary[pair_x].append(pair_y)
        else:
            #print("new key")
            rules_dictionary[pair_x] = [pair_y]
            #print(rules_dictionary)
    return rules_dictionary
'''Create a recursive function which takes an update sequence list and a dictionary. It takes the last interger in the list and sees if its in the dictionary. If it is it returns the entire list of values associated with that key. It then checks if that key is in the list. If it is -- we have a bad update because the keys are all setup to be left-hand rules in the page ordering rules. Therefore if we find an integer as a value we know our current key should be to the right of it, breaking the sequence'''
def upgrade_check(update_list, rules_dictionary):
    if len(update_list) == 1:
        # We've reached the first index meaning the update list is good!
        return True
    else:
        update = update_list[-1]
        associated_rules = []
        
        if update in rules_dictionary:
            associated_rules = rules_dictionary[update]
            for rule in associated_rules:
                if update == rule:
                    return False
                else:
                    upgrade_check(update_list[:-1], rules_dictionary)
        else:
            upgrade_check(update_list[:-1], rules_dictionary)
            
with open("rulestest.txt") as f:
    file_contents = f.read()
    f.close()
    
with open("updatestest.txt") as f:
    update_contents = f.read()
    f.close()

if __name__ == "__main__":
    rules_list = []
    update_lists = []
    approved_updates_list = []
    # Takes the rules and converts them into a list of integers
    for rule in file_contents.split("\n"):
        temp_list = []
        for item in rule.split("|"):
            temp_list.append(int(item))
        rules_list.append(temp_list)
        
    # Takes the list of rules as integers and builds a dictionary to be used as reference
    rules_dictionary = change_to_dict(rules_list)
    
    # Takes the update sequences and converts them into integer lists
    for lst in update_contents.split("\n"):
        temp_list = []
        for update in lst.split(","):
            temp_list.append(int(update))
        update_lists.append(temp_list)

    # Searches through the lists of updates and finds the ones that are correct using a recursive function
    for list in update_lists:
        if upgrade_check(list, rules_dictionary):
            approved_updates_list.append(list)
    print(approved_updates_list)