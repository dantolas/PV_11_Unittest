
class Node:
    """
    An inner class to hold a value, and the next/prev reference for the linked list.
    """
        
    def __init__(self,value) :
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    """
    An implementation of the queue data structure.
    """



    def __init__(self) :
        """
        Default constructor.
        """

        self.root = None
        self.tail = None
        self.length = 0


    def __len__(self):
        return self.length

    def __contains__(self,item):


        currentNode = self.root

        for i in range(self.length):
            if(currentNode.value == item) : return True
            currentNode = currentNode.next

        return False
    
    def __getitem__(self,key):
        if(not isinstance(key,int)):
            raise Exception("Index must be an integer")

        if(key >= self.length):
            raise Exception("Index out of bounds exception")
        
        currentNode = self.root

        for i in range(key):
            currentNode = currentNode.next
        return currentNode.value
    
    def __setitem__(self,key,value):
        if(not isinstance(key,int)):
            raise Exception("Index must be an integer")

        if(key >= self.length):
            raise Exception("Index out of bounds exception")
        
        currentNode = self.root

        for i in range(key):
            currentNode = currentNode.next

        currentNode.value = value
        return
    
    def __iter__(self):
        self.a = self.root
        return self
    
    def __next__(self):
            x = self.a

            if(x == False):
               raise StopIteration 
            
            if(x == self.tail):
                self.a = False
                return x

            self.a = x.next
            return x

            
        

    def add(self,value):
        """
        Adds an item to the end of the list.
        """
        self.length += 1

        node = Node(value)        

        if(self.root is None):
            self.root = node
            self.tail = node
            self.root.next = self.tail
            self.root.prev = self.tail
            self.tail.prev = self.root
            self.tail.next = self.root
            return
        
        self.tail.next = node
        self.root.prev = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = self.root


    def pop(self):
        """
        Removes the first element of the list.
        """

        if(self.length <= 0):
            raise Exception("Cannot pop empty queue");

        returnNode = self.root

        self.root = self.root.next
        self.tail.next = self.root
        self.root.prev = self.tail
     
        self.length -= 1
        return returnNode.value


    
    def remove(self,index):
        """
        Removes element at index.
        """
        if(index >= self.length):
            raise Exception("Index out of bounds exception")
        
        currentNode = self.root

        for i in range(index):
            prevNode = currentNode
            currentNode = currentNode.next
            
        prevNode.next = currentNode.next
        self.length -= 1
        del currentNode

    def count(self,member):
        currentNode = self.root
        count = 0
        for i in range(self.length-1):
            if(currentNode.value == member):
                count = count + 1
            currentNode = currentNode.next


        
    
    def get(self,index):
        """
        Returns element at index.
        """
        if(index >= self.length):
            raise Exception("Index out of bounds exception")
        
        currentNode = self.root

        for i in range(index):
            currentNode = currentNode.next
        return currentNode.value

        
    def printString(self):
        """
        Returns a string of the entire list to be printed into the console.
        """
        currentNode = self.root.next
        printString = str(self.root.value)+"|"
        while(currentNode != self.root):
            printString += str(currentNode.value)+"|"
            currentNode = currentNode.next


        return printString


    def popAll(self):
        returnlist = []
        
        returnlist.append(self.root.value)
        currentNode = self.root.next

        while(currentNode != self.root):
            returnlist.append(currentNode.value)
            currentNode.prev = None
            currentNode = currentNode.next

        return returnlist


