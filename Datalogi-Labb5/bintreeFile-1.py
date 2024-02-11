class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):  # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):  # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):  # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def skriv(p):  # Skriver ut trädet i bokstavsordning genom rekursion
    if p is not None:
        skriv(p.left)
        print(p.data)
        skriv(p.right)


def finns(p, value):  # Kollar om trädet innehåller ett visst objekt genom rekursion
    if p is None:
        return False
    if value == p.data:
        return True
    if value < p.data:
        return finns(p.left, value)
    if value > p.data:
        return finns(p.right, value)


def putta(p, newvalue):  # Lägger till nya värden
    if p is None:
        return Node(newvalue)
    else:
        if newvalue < p.data:
            if p.left is None:
                p.left = Node(newvalue)
            else:
                putta(p.left, newvalue)
        elif newvalue > p.data:
            if p.right is None:
                p.right = Node(newvalue)
            else:
                putta(p.right, newvalue)
        #  elif newvalue == p.data:
            #  print('finns redan')
        return p
