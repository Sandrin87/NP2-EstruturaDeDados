class node:
    def __init__(self, valor, proximo = None, anterior = None):
        self.valor = valor
        self.proximo = proximo if proximo is not None else self.valor
        self.anterior = anterior if anterior is not None else self.valor