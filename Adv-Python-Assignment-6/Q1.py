# 1. Data Structures: Implement a custom stack data structure with push, pop, and min operations, all in constant time.

class Stack():
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

        
    def push(self,element):
        self.stack.append(element)
        print(f"Element inserted : {element}")

        if not self.min_stack or element <= self.min_stack[-1]:
            self.min_stack.append(element)
      

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty cannot pop")
            return
        value=self.stack.pop()
        print(f"Element poped : {value}")
        if value == self.min_stack[-1]:
            self.min_stack.pop()
             
    def Display(self):
        print(self.stack)

    def minimum(self):
        if not self.min_stack:
            return "Stack is empty"
        return self.min_stack[-1]

def main():
    S=Stack()

    S.push(11)
    min=S.minimum()
    print(f"Min is {min}")

    S.push(21)
    S.push(1)
    
    min=S.minimum()
    print(f"Min is {min}")
    
    S.Display()
    min=S.minimum()
    print(f"Min is {min}")

    S.pop()
    S.pop()
    min=S.minimum()
    print(f"Min is {min}")
    S.pop()
    S.Display()


if __name__=="__main__":
    main()