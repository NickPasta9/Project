# gate_classes.py

from logic_gates import *
from graphic_gates import *

class DigitalValue:

    def __init__(self, p, value):
        self.point = p
        self.value = value # 1 or 0

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value

    def draw(self,win,type):
        if type == "I":
            #entry
            inputText = Entry(self.p,1)
            inputText.draw(win)
            while win.getKey() != "Return":
                continue
            text = inputText.getText()
            field = Text(self.p,text)
            field.draw(win)
            inputText.undraw()
            return text
        elif type == "O":
            #text
            text = Text(self.p,self.result)
            text.draw(win)
           
class And:

    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def setA(self,a):
        self.a = a

    def setB(self,b):
        self.b = b

    def getOutput(self):
        result = and_g(self.a,self.b)
        return DigitalValue(self.p,result)

    def draw(self,win):
        size = 100
        draw_and(self.p.getX(), self.p.getY(), size, win)


class Or:

    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def setA(self,a):
        self.a = a

    def setB(self,b):
        self.b = b

    def getOutput(self):
        result = or_g(self.a,self.b)
        return DigitalValue(self.p,result)

    def draw(self,win):
        size = 100
        draw_or(self.p.getX(), self.p.getY(), size, win)


class Not:

    def __init__(self, p, a):
        self.p = p
        self.a = a

    def setA(self,a):
        self.a = a

    def getOutput(self):
        result = not_g(self.a)
        return DigitalValue(self.p,result)

    def draw(self,win):
        size = 100
        draw_not(self.p.getX(), self.p.getY(), size, win)


class Xor:

    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def setA(self,a):
        self.a = a

    def setB(self,b):
        self.b = b

    def getOutput(self):
        result = xor_g(self.a,self.b)
        return DigitalValue(self.p,result)

    def draw(self,win):
        size = 100
        draw_xor(self.p.getX(), self.p.getY(), size, win)

class Nand:

    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def setA(self,a):
        self.a = a

    def setB(self,b):
        self.b = b

    def getOutput(self):
        result = nand_g(self.a,self.b)
        return DigitalValue(self.p,result)

    def draw(self,win):
        size = 100
        draw_nand(self.p.getX(), self.p.getY(), size, win)


class Connection:

    def __init__(self, fro, to):
        self.fro = fro
        self.to = to

    def getFrom(self):
        return self.fro

    def getTo(self):
        return self.to
