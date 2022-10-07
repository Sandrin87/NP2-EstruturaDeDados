from circular_node import node

class CLinkedList:
    def __init__(self,primeiroNo):
        self.inicio = primeiroNo if primeiroNo is not None else node(None)

        self.inicio.proximo = self.inicio
        self.inicio.anterior = self.inicio

    def insere_ultima_posicao(self, valor):
        novo_no = node(valor)

        if self.inicio is None:
            self.inicio = novo_no    

            self.inicio.proximo = self.inicio
            self.inicio.anterior = self.inicio
        else:
            novo_no.anterior = self.inicio.proximo
            self.inicio.proximo = novo_no
            self.inicio.anterior = novo_no.anterior
    
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
            if (self.head == None):
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

    def PrintList(self):
      current = self.head
      if(current != None):
        print("The List contains:", end=" ")
        while (True):
            print(current.data, end=" ")
            current = current.next
            if(current == self.head):
                break
        print()
      else:
        print("The list is empty")



                
