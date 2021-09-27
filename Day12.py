class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores# Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        summ = 0
        for i in range(len(self.scores)):
            summ = summ + self.scores[i]
            
    
    
    
            Avgscore = summ//len(self.scores)
        if Avgscore >= 90 and Avgscore <= 100:
            return "O"
        elif Avgscore >=80 and Avgscore <90:
            return "E"
        elif Avgscore >=70 and Avgscore <80:
            return "A"
        elif Avgscore >=55 and Avgscore <70:
            return "P"
        elif Avgscore >=40 and Avgscore <55:
            return "D"
        elif Avgscore <40:
            return "T"
        
            
            
            
        
line = input().split()