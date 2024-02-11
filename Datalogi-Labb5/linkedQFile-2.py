class Node:  # Supportklass för varje objekt i kön.
    def __init__(self, data, next=None):
        self.data = data  # innehåller datan i objektet
        self.next = next  # pekar på objektet bakom i kön


class LinkedQ:  # Klass för själva kön
    def __init__(self):
        self._first = None  # Pekar på första objektet i kön
        self._last = None  # Pekar på sista objektet i kön

    def isEmpty(self):  # Kollar om kön är tom
        return self._last is None

    def enqueue(self, data):  # Lägger till ett objekt länst bak i kön
        tmp = Node(data)  # Sparar det nya objeketet i en temporär lokal variabel
        if self.isEmpty():  # Om kön är tom blir det nya objektet både först och sist
            self._first = tmp
            self._last = tmp
        else:  # Annars pekar det tidigare sista objektet på det nya och det nya blir det nya sista
            self._last.next = tmp
            self._last = tmp

    def dequeue(self):  # Tar bort och returnerar det fösta objektet i kön
        if self.isEmpty():  # Kollar om kön är tom, isf rutureras none
            return None
        else:
            tmp2 = self._first.data
            if self.size() == 1:  # Om det är sista objektet som tas bort blir både första och sista ojektet none
                self._first = None
                self._last = None
            else:  # Annars blir nästa objekt i listan det nya första
                self._first = self._first.next
            return tmp2

    def size(self):  # Visar hur lång kön är
        tmp = self._first
        i = 0
        while tmp is not None:  # Räknar varje objekt som inte är none
            tmp = tmp.next
            i = i + 1
        return i
