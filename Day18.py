import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self,data):
        self.stack.append(data)
        
    def popCharacter(self):
        return self.stack.pop();
    
    def enqueueCharacter(self,data):
        self.queue.append(data)
        
    def dequeueCharacter(self):
        return self.queue.pop(0);
    # Write your code here

# read the string s