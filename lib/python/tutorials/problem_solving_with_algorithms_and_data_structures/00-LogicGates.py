#Logic Gates
class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.PinA = None
        self.PinB = None

    def getPinA(self):
        if self.PinA == None:
            inp = int(input("Enter Pin A input for gate "+ self.getLabel()+" --> "))
            if inp > 1 or inp < 0:
                raise ValueError("Only 0 and 1 allowed.")
            self.PinA = inp
            return inp
        else:
            #return self.PinA.getFrom().getOutput()
            return self.PinA

    def getPinB(self):
        if self.PinB == None:
            inp = int(input("Enter Pin B input for gate "+ self.getLabel()+" --> "))
            if inp > 1 or inp < 0:
                raise ValueError("Only 0 and 1 allowed.")
            self.PinB = inp
            return inp
        else:
            #return self.PinB.getFrom().getOutput()
            return self.PinB
    
    def setNextPin(self,source):
        if self.PinA == None:
            self.PinA = source
        else:
            if self.PinB == None:
                self.PinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self,n)
        self.Pin = None

    def getPin(self):
        if self.Pin == None:
            inp = int(input("Enter Pin  input for gate "+ self.getLabel()+" --> "))
            if inp > 1 or inp < 0:
                raise ValueError("Only 0 and 1 allowed.")
            return inp
        else:
            return self.Pin.getFrom().getOutput()
    
    def setNextPin(self,source):
        if self.Pin == None:
            self.Pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class XorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a==0 and b==1) or (a==1 and b==0):
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class HalfAdder(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        g1 = AndGate("G1")
        g2 = XorGate("G2")
        g1.PinA = a
        g1.PinB = b
        g2.PinA = a
        g2.PinB = b
        carry = g1.performGateLogic()
        sum = g2.performGateLogic()
        return (carry,sum)

class Connector:

    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector (g1,g3)
c2 = Connector (g2,g3)
c3 = Connector (g3,g4)
#print(g4.getOutput())
#ha1 = HalfAdder("H1")
#print(ha1.getOutput())

def HalfAdder(a,b):
    g1 = AndGate("G1")
    g2 = XorGate("G2")
    g1.PinA = a
    g1.PinB = b
    carry = g1.performGateLogic()
    g2.PinA = g1.PinA
    g2.PinB = g1.PinB
    sum = g2.performGateLogic()
    return carry, sum

#print(HalfAdder(1,1))

def FullAdder(a,b,c):
    carry_in,sum_in = HalfAdder(a,b)
    g1 = XorGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate ("G3")
    g1.PinA = sum_in
    g1.PinB = c
    sum_out = g1.performGateLogic()
    g2.PinA = sum_out
    g2.PinB = c
    carry2 = g2.performGateLogic()
    g3.PinA = carry_in
    g3.PinB = carry2
    carry_out = g3.performGateLogic()
    return carry_out, sum_out

print(FullAdder(1,1,0))

def adder_8bit(a,b):
    carry0,sum0 = HalfAdder(int(str(a)[7]),int(str(b)[7]))
    carry1,sum1 = FullAdder(int(str(a)[6]),int(str(b)[6]),carry0)
    carry2,sum2 = FullAdder(int(str(a)[5]),int(str(b)[5]),carry1)
    carry3,sum3 = FullAdder(int(str(a)[4]),int(str(b)[4]),carry2)
    carry4,sum4 = FullAdder(int(str(a)[3]),int(str(b)[3]),carry3)
    carry5,sum5 = FullAdder(int(str(a)[2]),int(str(b)[2]),carry4)
    carry6,sum6 = FullAdder(int(str(a)[1]),int(str(b)[1]),carry5)
    carry7,sum7 = FullAdder(int(str(a)[0]),int(str(b)[0]),carry6)
    return carry7,sum7,sum6,sum5,sum4,sum3,sum2,sum1,sum0


print(adder_8bit("11110100","11001000"))
