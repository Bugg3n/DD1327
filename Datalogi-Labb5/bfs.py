from bintreeFile import *
from linkedQFile import LinkedQ


def add_word3(tree):  # Skapar ett binärträd
    with open('word3.txt', 'r', encoding="utf-8") as file:
        for rows in file:
            tree.put(rows.strip())
    return tree


def make_children(node, children):  # Skapar olika ordvariationer
    alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
    for i in range(len(node)):
        parent = list(node)
        for letter in alphabet:
            parent[i] = letter  # Testar att byta ut varje bokstav i ordet till varje bokstav i alfabetet
            tmp = ''.join(parent)
            if tmp in word_list and tmp not in old:  # Om ordet inte redan finns, sparas den till barnkön
                children.enqueue(tmp)
                old.put(tmp)
                if tmp == goal:
                    print('det finns en väg till', goal)  # Om målet hittas, avbryts programmet och detta skrivs ut
                    exit()
    return children


word_list = Bintree()
add_word3(word_list)
old = Bintree()
q = LinkedQ()

start_node = input("Startord: ").lower()
goal = input("Slutord: ").lower()

if start_node not in word_list:  # Om man skriver in fel ord, berättar programmet det
    print(start_node + " finns inte i ordlistan.")
    if goal not in word_list:
        print(goal + " finns inte i ordlistan.")
    exit()
elif goal not in word_list:
    print(goal + " finns inte i ordlistan.")
    exit()

q.enqueue(start_node)  # Lägger till startnoden i kön

while not q.isEmpty():  # Så länge det finns något i kön
    nod = q.dequeue()
    q = make_children(nod, q)  # Skapa barnen till nästa i kön
print("det finns ingen väg")
