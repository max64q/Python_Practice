#Question 5

class InputOutString:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())
        print(self.string.lower())
        
strObj = InputOutString()
strObj.getString()
strObj.printString()
        
        
