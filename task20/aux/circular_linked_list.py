# When I came across the problem, I figured it would be
# manageable to solve it with just Python lists.
# When the problem specifies that the last element of the list 
# refers to the first element of the same list, 
# I realized that it was a *linked list data structure* task

# https://www.geeksforgeeks.org/circular-linked-list/

class Node:
    
    # A list is made out of a chain of nodes
    # Every node has It's data, and a link to the next node
    # Last node refers to the first node from the list
    # That's why It's a circular list

    def __init__(self, data = None):
        self.data = data
        self.next = self

class CLL:

    # Head will be a Node object once the list is not empty 
    # "count" keeps track of how big the list is
    def __init__(self):
        self.head = None 
        self.count = 0
    
    def __repr__(self):
        string = ""
        
        # Meaning the list is brand new
        # Or just empty at this point
        if(self.head == None):
            string = "Circular Linked List Empty"
            return string
        
        string = "Circular Linked List \n Head -> \n" + str(self.head.data) + "\n"      
        
        # next node
        temp = self.head.next 

        # The last node sets "self.next"
        # To the head of the CLL
        while(temp != self.head):
            string = string + " -> " + str(temp.data) + "\n"
            temp = temp.next
        string = string + "End of CLL.\n\n"
        return string
    
    # returns how big is the CLL is at the moment
    def size(self):
        return self.count

    # add element to the list!
    def insert(self, data, index):

        # Index may be out of range...
        if (index > self.count) | (index < 0):
            # new index is (index % int(self.count()))
            index = (index % self.count)
        
        # If there is nothing in the list
        if self.head == None:
            self.head = Node(data)
            self.count += 1
            return
        
        # iterating the list
        temp = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            temp = temp.next
        
        # Correct place for insertion found!

        # The new desired node goes 
        # between "temp" and "aux_temp"
        aux_temp = temp.next 
        temp.next = Node(data)
        temp.next.next = aux_temp
        if(index == 0):
            self.head = temp.next
        self.count += 1
        return
    
    # "append" is an "insert" at the end of the list
    def append(self, data):
        self.insert(data, self.count)
        return
    
    # remove element from the list
    def remove(self, index):

        # Index may be out of range...
        if (index >= self.count) | (index < 0):
            # new index is (index % int(self.count()))
            index = (index % self.count)
        
        # If count == 1
        # The last element in the list is going to be removed
        if self.count == 1:
            self.head = None
            self.count = 0
            return
        
        # iterating the list
        before = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            before = before.next

        # removing a node is basically updating that
        # the i-1 element is now connected to i+1
        after = before.next.next
        
        before.next = after
        
        if(index == 0):
            self.head = after
        self.count -= 1

        return
    
    # Given value of node and occurrence
    # return this node's index
    def index_by_data_occur(self, data, occur):
        
        temp = self.head
        times_seen = 0

        for i in range(self.count):
            if(temp.data == data):
                if times_seen == (occur-1):

                    return i

                else:

                    times_seen = times_seen + 1 
                    
            temp = temp.next
        return None

    # Given the first occurence of certain node
    # return this node's index
    def index_by_data(self, data):
        
        temp = self.head

        for i in range(self.count):
            if(temp.data == data):
                return i
            temp = temp.next
        return None

    # Given an index, get node's data
    def data_from_index(self, index):
        # Index may be out of range...
        if (index >= self.count) | (index < 0):
                # new index is (index % int(self.count()))
                index = (index % self.count)
        
        temp = self.head

        for i in range(index):
            
            temp = temp.next

        return temp.data
    
    # Find zero, and then retrieve "ith" element 
    # counting from zero
    def node_from_zero(self, index):
        
        # start at the head
        temp = self.head

        # find zero
        while temp.data != 0:
            
            temp = temp.next

        # once I find zero
        # start counting
        for i in range(index):
            
            temp = temp.next    

        # return ith element from zero
        return temp

    # Given an index, get node object
    def node_from_index(self, index):
        # Index may be out of range...
        if (index >= self.count) | (index < 0):
                # new index is (index % int(self.count()))
                index = (index % self.count)
        
        temp = self.head

        for i in range(index):
            
            temp = temp.next

        return temp

    # moving a node to the right
    def move_positive(self, index):
        original_list_size = self.count
        times_moved = self.data_from_index(index)
        self.remove(index)    
        if ((index + times_moved) > self.count): 
            self.insert(times_moved, ((index+times_moved) % original_list_size) + 1)
        else:
            self.insert(times_moved, ((index+times_moved) % original_list_size))
        return 
    
    # moving a node to the left
    def move_negative(self, index):
        original_list_size = self.count
        times_moved = self.data_from_index(index)
        self.remove(index)
        if(((index+times_moved) % original_list_size) == 0):
            self.append(times_moved)
        else:
            self.insert(times_moved, ((index+times_moved) % original_list_size)-1)
        return 
    