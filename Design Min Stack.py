"""class minStack():
    def __init__(self):
        self.stack = []
        self.minSt = []
    def push(self,value):
        self.stack.append(value) 
        minval = min(value , self.minSt[-1] if self.minSt else value  ) 
        self.minSt.append(minval)
    def pop(self):
        self.stack.pop()
        self.minSt.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minSt[-1]                
    """
# added question by me by me : re-create it all for Max and Min access in O(1), btw I solved just like NeetCode this time which is a huge Yay for me !!! lol. 
class Minstack():
    def __init__(self):
        self.stacknormal = []
        self.minstack = []
        self.maxstack = []
    def push(self,value) -> None: #I should start add a return value I think, ok from now on !     
        self.stacknormal.append(value)
        minval = min(value,self.minstack[-1] if self.minstack else value )
        maxval = max(value,self.maxstack[-1] if self.maxstack else value )
        self.maxstack.append(maxval)
        self.minstack.append(minval)
    def pop(self) -> None: #usually the pop method returns what it pops (last element in a stack)
        self.stacknormal.pop()
        self.minstack.pop()
        self.maxstack.pop()
    def top(self) -> int:
        return self.stacknormal[-1]
    def get_min_in_O1(self) -> int:
        return self.minstack[-1]
    def get_max_in_O1(self) -> int:
        return self.maxstack[-1]
        
#mission completed, lesson learned Let's Goooooooooooooooooooooo! 