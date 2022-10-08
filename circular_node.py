class node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next if next is not None else self.data
        self.prev = prev if prev is not None else self.data