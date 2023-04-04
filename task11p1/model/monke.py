
class Monke:

    def __init__(self, MonkeyList):

        self.index = int(MonkeyList[0][0])

        # list of integers
        self.inventory = [int(x) for x in MonkeyList[1]]

        # I'll keep "operation" as a
        # list of strings because
        # It may be some "old * old" operation 
        self.operation = MonkeyList[2]

        self.divisible = int(MonkeyList[3][0])
        self.if_true = int(MonkeyList[4][0])
        self.if_false = int(MonkeyList[5][0])

        self.item_inspection_counter = 0
    
    def __repr__(self):

        string = "This is monkey " + str(self.index) + "\n"

        string = string + "His inventory consists of : \n" + str(self.inventory) + "\n"

        string = string + "This monkey needs to perform this operation : old " + str(self.operation[0]) + " " + str(self.operation[1])  + "\n"
        
        string = string + "Is this division divisible by " + str(self.divisible) + "?\n"
        
        string = string + "If true, give item to monkey with the index " + str(self.if_true) 

        string = string + "\nIf false, give item to monkey with the index " + str(self.if_false)
        
        return "\n" + string + "\n"
    
    # ------------------------------------
    
    def raise_item_counter(self):
        self.item_inspection_counter += 1
        return

    # ------------------------------------

    def get_item_counter(self):
        return self.item_inspection_counter

    def get_inventory(self):
        return self.inventory.copy()

    def get_if_true(self):
        return self.if_true

    def get_if_false(self):
        return self.if_false

    def get_operation(self):
        return self.operation
    
    def get_divisible(self):
        return self.divisible

    # ------------------------------------
    
    def is_inventory_empy(self):
    
        if self.inventory == []:
            return True
        else:
            return False
    
    # Monkey gives this element to someone else
    def throw_gift(self, item):
        # inventory is an array of integers
        # item is also an integer

        temp_inventory = self.inventory
        temp_inventory.remove(item)
        self.inventory = temp_inventory
        return

    # Monkey now have something new in inventory
    def get_gift(self, item):
        # inventory is an array of integers
        # item is also an integer

        temp_inventory = self.inventory
        temp_inventory.append(item)
        self.inventory = temp_inventory
        return
    
    # ------------------------------------
    
