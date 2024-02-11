class Pipe:
    def __init__(self, flowrate, superpower=False, next=None):
        self.flowrate = flowrate
        self.next = next
        self.superpower = superpower

    def giveSuperPower(self):
        self.superpower = True

    def removeSuperPower(self):
        self.superpower = False

    def setNext(self, next):
        self.next = next

    def setFlowrate(self, flowrate):
        if flowrate < 1:
            self.flowrate = flowrate

