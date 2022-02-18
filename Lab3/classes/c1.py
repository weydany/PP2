class String:

    def __init__(self):
        self.str = None

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

ss = String()
ss.getString()
ss.printString()