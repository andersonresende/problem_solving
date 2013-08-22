class LogicGate: #abstrata
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate): #abstrata
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
			return input("Enter Pin A input for gate "+ \
									self.getLabel()+"-->")
		else:
			return self.pinA.getFrom().getOutput()
    def getPinB(self):
		if self.pinB == None:
			return input("Enter Pin B input for gate "+ \
									self.getLabel()+"-->")
		else:
			return self.pinB.getFrom().getOutput()
    def setNextPin(self,source):
	    if self.pinA == None:
	        self.pinA = source
	    else:
	        if self.pinB == None:
	            self.pinB = source
	        else:
	           raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate): #concreta
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate): #concreta
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0


class NandGate(AndGate):
    def performGateLogic(self):
        if AndGate.performGateLogic(self)==1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def performGateLogic(self):
        if OrGate.performGateLogic(self)==1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate


if __name__ == '__main__':
	# g1 = AndGate("G1")
	# print g1.getLabel()
	# print g1.getOutput()
	# print "\n"
	# g2 = OrGate("G2")
	# print g2.getLabel()
	# print g2.getOutput()


	# g1 = AndGate("G1")
	# g2 = AndGate("G2")
	# g3 = OrGate("G3")
	# c1 = Connector(g1,g3)
	# c2 = Connector(g2,g3)
	# print g3.getOutput()
    g1 = AndGate("G1")
    g2 = NandGate("G2")
    print g1.getOutput()
    print g2.getOutput()
