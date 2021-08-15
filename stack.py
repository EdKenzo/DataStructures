'''
LIFO
push (ins)and pop (del)
nb in this case setting limit to 5
'''
class stack:
    def __init__(self):
        self.data = []
    def length(self):
        return len(self.data)
    def push(self,data):
        if len(self.data)< 5:
            self.data.append(str(data))
        else:
            return "overflow"
    def pop(self):
        if len(self.data)>0:
            self.data.pop()
        else:
            return "underflow"
    def print(self):
        if len(self.data) == 0:
            return "Empty"
        else:
            print ('\n v\n v\n'.join(self.data))
            
a = stack()
a.push(10)
a.push(17)
a.push(13)

a.pop()
a.print()

    
