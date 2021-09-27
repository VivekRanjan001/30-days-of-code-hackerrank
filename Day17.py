class Calculator:
    def power(self,n,p):
        if n>-1 and p>-1:
            return n**p
        else:
            return "n and p should be non-negative"
            #Write your code here

myCalculator=Calculator()