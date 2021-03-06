class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def isEmpty(self):
        return len(self.s) == 0 # True, False

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def size(self):
        return len(self.s)

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

def isOper(item):
    if item == '+' or item == '-' or item == '*' or item == '/':
        return True
    else:
        return False


def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def Postfix(eq):
    eqList = eq.split(" ")
    s = Stack()
    postEq = []

    for item in eqList:
        if item == '(':
            s.push(item)
        elif item == ')':
            while True:
                _tmp = s.pop()
                if _tmp == '(':
                    break
                else:
                    postEq.append(_tmp)
        elif item == "+" or item == "-":
            while isOper(s.peek()) == True:
                postEq.append(s.pop())
            s.push(item)
        elif item == "*" or item == "/":    
            while s.peek() == "*" or s.peek() == "/":
                postEq.append(s.pop())
            s.push(item)
        elif isNum(item) == True:
            postEq.append(item)
    while s.isEmpty() == False:
        postEq.append(s.pop())
    print(postEq)
    S = Stack()
    for item in postEq:
        if isOper(item) == False:
            S.push(item)
        else:
            num2 = float(S.pop())
            num1 = float(S.pop())
            if item == '+': S.push(str(num1 + num2))
            elif item == '-': S.push(str(num1 - num2))   
            elif item == '*': S.push(str(num1 * num2)) 
            elif item == '/': S.push(str(num1 / num2))
    return(S.pop())

eq = "( 12.3 + 10 ) * 3 / 6"
print(eq)
print(Postfix(eq))