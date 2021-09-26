class Person:
    def __init__(self,age):
        self.initialAge = age
        if self.initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = self.initialAge

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age > 12 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")


t = int(input())
