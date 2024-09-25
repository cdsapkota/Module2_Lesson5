list = []

def add_items(x):
    list.append(x)
    return list

def remove_items(x):
    list.remove(x)
    return list

continue_adding = True

while continue_adding:
    item = input("Would you like to add an item (yes or no)? ")
    if item.lower() == "yes":
        item_name = input("Please enter the name of the item that you want to add. ")
        add_items(item_name)
    elif item.lower() == "no":
        remove_item = input("Would you like to remove an item (yes or no)? ")
        if remove_item.lower() == "yes":
            try:
                item_name = input("Please enter the name of the item that you want to remove. ")
                remove_items(item_name)
            except ValueError:
                print("Item not found in this list.")
        elif remove_item.lower() == "no":
            print(f"Here is your list \n{"\n".join(list)}")
            continue_adding = False
        else:
            print("Incorrect response.")
    else:
        print("Incorrect response.")