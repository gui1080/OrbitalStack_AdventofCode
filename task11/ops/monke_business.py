
def retireve_monkey_business_level(monkey_objects):
    # get the two most active monkeys
    # multiply item counter
    # return result

    items = []

    for monkey in range(len(monkey_objects)):
        items.append(monkey_objects[monkey].get_item_counter())
    
    items.sort()

    max_item = items[len(items)-1]
    second_max_item = items[len(items)-2]

    return max_item * second_max_item