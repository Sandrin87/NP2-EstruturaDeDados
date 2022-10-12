'''
Nome: Gabriel Sandrin Pires R.A: G2713E-7
Nome: Vitória Aparecida Souza Santos R.A: F3428E-4
'''


from circular_Linkedlist import CLinkedList
from circular_node import node

TheList = CLinkedList() 

TheList.addFront(10)
TheList.addFront(20)
TheList.addFront(30)
TheList.addFront(40)

TheList.PrintList()

print("\nList after inserting at a certain position: ")
TheList.addAtPosition(70, 2)
TheList.PrintList()

# Search an element in the list
TheList.SearchElement(2)
TheList.SearchElement(30)

# Delete the last node
print("\nList after deleting the last node:")
TheList.DeleteLast()
TheList.PrintList()

print("\nList after deleting elements.")
TheList.DeleteElement(30)
TheList.DeleteElement(70)
TheList.PrintList()

print("\nList with insertion at the end. ")
TheList.addLast(100)
TheList.addLast(110)
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

print("\n")
print("---"*10)
print("Testes extras: \n")

Lista = CLinkedList()
Lista.PrintList()
Lista.DeleteAtIndex(2)
Lista.DeleteElement(22)
Lista.DeleteFirst()
Lista.DeleteLast()
Lista.SearchElement(20)
Lista.GetAtIndex(3)

Lista.addLast(3)
Lista.PrintList()
Lista.addFront(2)
Lista.PrintList()
Lista.addAtPosition(5.5, 2)
Lista.PrintList()