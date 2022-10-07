from mimetypes import init
from circular_node import node

class list:
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

            print("------")
            print("novo no - ",valor)
            print("inicio da lista- ",self.inicio.valor)
            print("proximo da lista- ",self.inicio.proximo.valor)
            print("anterior da lista- ",self.inicio.anterior.valor)
