class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        minn = self.__elements[0]
        for i in self.__elements:
            if minn > i:
                minn = i
                
        maxx = self.__elements[0]
        for i in self.__elements:
            if maxx < i:
                maxx = i
                
                
        self.maximumDifference = maxx - minn            
	# Add your code here

# End of Difference class