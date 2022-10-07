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
TheList.PrintList()


n1 = node(10)
lista = list(n1)
lista.insere_ultima_posicao(20)
lista.insere_ultima_posicao(30)
lista.insere_ultima_posicao(45)