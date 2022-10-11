'''
Nome: Gabriel Sandrin Pires R.A: G2713E-7
Nome: Vitória Aparecida Souza Santos R.A: F3428E-4
'''


from circular_Linkedlist import CLinkedList
from circular_node import node

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

