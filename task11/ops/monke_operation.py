def monkey_test(monkey_objects, monkey, inventory_element):

    print("Testing - " + str(inventory_element))

    try: 

        operation = monkey.get_operation()
        divisible_by_x = monkey.get_divisible()

        if operation[0] == "*":

            if operation[1] != "old":
                
                new_item = (int(inventory_element) * int(operation[1])) // 3
                result = (new_item) % divisible_by_x

            else:

                new_item = (int(inventory_element) * int(inventory_element)) // 3
                result = (new_item) % divisible_by_x

        elif operation[0] == "+":
            
            if operation[1] != "old":
                
                new_item = (int(inventory_element) + int(operation[1])) // 3
                result = (new_item) % divisible_by_x

            else:

                new_item = int(inventory_element) + int(inventory_element) // 3
                result = (new_item) % divisible_by_x

        # element divided by 3 is what is going to 
        # be given to other monkey

        print("new item is -> " + str(new_item))

        # divisible_by_x == True!
        if result == 0:
            
            monkey.throw_gift(inventory_element)
            destination = monkey.get_if_true()
            monkey_objects[destination].get_gift(new_item)

        # divisible_by_x == False!
        else:
            monkey.throw_gift(inventory_element)
            destination = monkey.get_if_false()
            monkey_objects[destination].get_gift(new_item)

        monkey.raise_item_counter()
        return True
    
    except:

        return False