from circular_node import node

class CLinkedList:
    def __init__(self, firstNode = None):
       self.head = firstNode if firstNode == None else node(firstNode)
    
    def removeItemFromFirstPosition(self):
        if(self.head is not None):
            firstNode = self.head
            lastNode = self.head.prev
            self.head = firstNode.next
            self.head.prev = lastNode
            del(firstNode)
            

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
            return
        current = self.head
        found = False
        while(current):
            if(current.data == delValue):
                found = True
                break
            current = current.next
        if(found == True):
            prevNode = current.prev
            nextNode = current.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            return   
        else:
            print("\nElement not found.")

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
                    print(f"The list contains the index:{index}, the following data is: {start.data}")
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
        print("The list is empty")



                
