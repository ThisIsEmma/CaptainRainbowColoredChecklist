checklist = list()

def isIndexValid(index, checklist): #Stretch challenge, update any applicable functions 
    if index < len(checklist):      #with the ability to verify that all index values are accurate  
        return True
    else:
        return False 


def create(item):
    checklist.append(item)

def read(index):
    intIndex = int(index)
    if isIndexValid(intIndex, checklist) == True:
        return checklist[intIndex]
    else:
        return print("Invalid index, please try again")

def update(index, item):
    intIndex = int(index)
    if isIndexValid(intIndex, checklist) == True:
        checklist[intIndex] = item
    else:
        print("Invalid index, please try again")

def destroy(index):
    intIndex = int(index)
    if isIndexValid(intIndex, checklist) == True:
        checklist.pop(intIndex)
    else:
        print("Invalid index, please try again")

def list_all_items():
    index = 0
    for list_item in checklist:
        print(f'{index} {list_item}')
        index += 1


def mark_completed(index):
    intIndex = int(index)
    itemCompleted = checklist[intIndex]
    itemCompleted = '√ ' + itemCompleted 
    update(intIndex, itemCompleted)
    print(f'{itemCompleted}'); 

def clearTerminal(): #stretch challenge - clear terminal to make input more legible/user friendly
    print("\033c")

def select(function_code):
    # Create item
    if function_code == "c":
        input_item = user_input("\nInput item:\n")
        create(input_item)
        clearTerminal()
        print(f'{input_item} added!')


    # Read item
    elif function_code == "r":
        item_index = user_input("\nIndex Number?\n")
        clearTerminal()
        print(read(item_index))
        

    # Print all items
    elif function_code == "s":
        clearTerminal()
        list_all_items()


    #Update (replace an existing item in the list)
    elif function_code == "u":
        item_description = user_input("\nWhat should we add ?\n")
        item_index = user_input("\nWhich position should we place it ?(Index number)\n")
        update(item_index, item_description)
        clearTerminal()
        print(f'{item_description} added !')
    
    #Erase an item
    elif function_code == "d":
        print('Below is the content of the list:\n')
        list_all_items()
        item_index = user_input("\nWhich item should we remove? (enter index position)\n")
        clearTerminal()
        print(f'{checklist[int(item_index)]} deleted.')
        destroy(item_index)
    
    #Mark as completed
    elif function_code == "m":
        print('Here is the content content of the list.\n')
        list_all_items()
        item_index = user_input('\nWhich item did we complete? (Please enter index position)\n')
        clearTerminal()
        mark_completed(item_index)

    #Exit function
    elif function_code == "q":
        clearTerminal()
        print('Exited program\n')
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):

    user_input = input(prompt)
    return user_input.lower() #Stretch challenge - Allow user to use upper or lowercase for function selection 

running = True
while running:
    selection = user_input(
        "\nPress C to add to list\nR to Read from list\nS to show complete list\nU to update\nD to delete\nM to mark an item as complete\nQ to exit program.\n")
    running = select(selection)
