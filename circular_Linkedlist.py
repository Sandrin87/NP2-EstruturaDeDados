
'''
Nome: Gabriel Sandrin Pires R.A: G2713E-7
Nome: Vitória Aparecida Souza Santos R.A: F3428E-4
'''
class node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next if next is not None else self.data
        self.prev = prev if prev is not None else self.data
class CLinkedList:
    def __init__(self, firstNode = None):
       self.head = firstNode if firstNode == None else node(firstNode)
    
    def DeleteFirst(self):
        previous = self.head
        nextOne = self.head

        if(self.head is None):
            print("\n Empty List")
            return None
        if(previous.next == previous):
            self.head = None
            return None
        
        while(previous.next != self.head):
            previous = previous.next
            nextOne = previous.next
        
        previous.next = nextOne.next
        self.head = previous.next
        return self.head
    
    def addFront(self, element):
        newNode = node(element)
        if(self.head == None):
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
            return
        else:
            current = self.head
            while(current.next != self.head):
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode 

    def addLast(self, element):
        newNode = node(element)
        if(self.head == None):
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
            return
        else:
          current = self.head
          while(current.next != self.head):
            current = current.next
        current.next = newNode
        newNode.next = self.head
        newNode.prev = current
        self.head.prev = newNode

    def addAtPosition(self, element, position):
        newNode = node(element)
        current = self.head
        counter = 0
        if(current != None):
            counter += 1
            current = current.next
        while(current != self.head):
            counter += 1
            current = current.next
        
        if (position < 1 or position > (counter+1)):
           print("\nInvalid position.")
        elif (position == 1):
          if(self.head == None):
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
          else:
            while(current.next != self.head):
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            
        else: 
          current = self.head
          for i in range(1, position-1):
              current = current.next
          newNode.next = current.next
          newNode.next.prev = newNode
          newNode.prev = current
          current.next = newNode

    def SearchElement(self, searchValue):
        current = self.head
        found = 0
        i = 0

        if(current != None):
          while (True):
            i += 1
            if(current.data == searchValue):
                found += 1
                break
            current = current.next
            if(current == self.head):
                break
          if(found == 1):
              print("\n",searchValue, "if found at index =", i)
          else:
              print("\n",searchValue, "is not found in the list.")
        else:
          print("The list is empty.")

    def DeleteLast(self):
        if(self.head != None):
            if(self.head.next == self.head):
                self.head = None
            else:
              current = self.head
              while(current.next.next != self.head):
                current = current.next
            lastNode = current.next
            current.next = self.head
            self.head.prev = current
            lastNode = None

    def DeleteElement(self, delValue):
        if(self.head == None):
            return None
        current = self.head
        prev1 = None
        
        while(current.data != delValue):
            
            if(current.next == self.head):
                print("\nList doesn't have node, with value = ", delValue)
                return self.head
            
            prev1 = current
            current = current.next
        
        if (current.next == self.head and prev1 == None):
            self.head = None
            return self.head
        
        if(current == self.head):
            self.DeleteFirst()
        
        elif (current.next == self.head):
            self.DeleteLast()

        else:

           temp = current.next
           prev1.next = temp
           temp.prev = prev1
        
        return self.head
        


    def DeleteAtIndex(self, index):
        _len = self.Length()
        cont = 1
        previous = self.head
        nextOne = self.head

        if(self.head is None):
            print("\nThe list is empty")

        if(index >= _len or index < 0):
            print("\nIndex Not Found. ") 
            return None

        if(index == 0):
            self.head = self.DeleteFirst()
            return self.head

        while(_len > 0):
            if(index == cont):
                previous.next = nextOne.next
                return self.head

            previous = previous.next
            nextOne = previous.next
            _len -= 1
            cont += 1
        return self.head        

    def GetAtIndex(self, index):
        cont = 0
        start = self.head
        ended = False
        if(start is not None):                
            if(index == 0):
                print(f"The list contains the index:{index}, the following data is: {start.data}")

            while(cont != index):
                start = start.next
                cont += 1

                if start == self.head:
                    ended = True
                    break
            
                if cont == index:
                    print(f"The list contains the index: {index}, the following data is: {start.data}")
            if ended:
                print("The List does not contains the given index.")

    def PrintList(self):
      current = self.head
      if(current != None):
        print("\nThe List contains:", end=" ")
        while (True):
            print(current.data, end=" ")
            current = current.next
            if(current == self.head):
                break
        print()
      else:
        print("The list is empty, 0 elements.")


    def Length(self):
        current = self.head
        cont = 0

        if(self.head is None):
            return 0
        else:
            while(True):
                current = current.next
                cont += 1
                if(current == self.head):
                    break
        return cont

TheList = CLinkedList() 

TheList.addFront(6)
TheList.addFront(4)
TheList.addFront(3)
TheList.addFront(2)
TheList.addFront(1)

TheList.PrintList()

print("\nList after inserting at a certain position: ")
TheList.addAtPosition(5, 5)
TheList.PrintList()


TheList.SearchElement(2)
TheList.SearchElement(30)


print("\nList after deleting the last node:")
TheList.DeleteLast()
TheList.PrintList()

print("\nList after deleting elements.")
TheList.DeleteElement(30)
TheList.PrintList()

print("\nList with insertion at the end. ")
TheList.addLast(6)
TheList.addLast(7)
TheList.addLast(8)
TheList.addLast(9)
TheList.PrintList()

print("\nGetting the data from index. ")
TheList.GetAtIndex(0)

print("\nDeleting the first element of the list. ")
TheList.DeleteFirst()
TheList.PrintList()

print("\nDeleting the element at index given. ")
TheList.DeleteAtIndex(0)
TheList.PrintList()

print("\nSize of the List. ")
print(TheList.Length())

TheList.DeleteElement(2)
TheList.DeleteElement(8)
TheList.DeleteElement(4)
TheList.DeleteElement(3)
print("\nList after deleting an element:")
TheList.PrintList()

print("\nSize of the List. ")
print(TheList.Length())
