from stack import Stack

def infixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    prefixStack = Stack()
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixStack.push(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                operand2 = prefixStack.pop()
                operand1 = prefixStack.pop()
                prefixStack.push("{} {} {}".format(topToken, operand1, operand2))
                topToken = opStack.pop()
        else: 
            assert(token in "+-*/")
            while opStack.size()>0 and prec[opStack.peek()] >= prec[token]:
                operand2 = prefixStack.pop()
                operand1 = prefixStack.pop()
                topToken = opStack.pop()
                prefixStack.push("{} {} {}".format(topToken, operand1, operand2))
            opStack.push(token)

    while opStack.size()>0:
        operand2 = prefixStack.pop()
        operand1 = prefixStack.pop()
        topToken = opStack.pop()
        prefixStack.push("{} {} {}".format(topToken, operand1, operand2))
    assert(prefixStack.size() == 1)
    return prefixStack.pop()

if __name__ == "__main__":
    infix = input("Please input infix expression('q' for Quit): ")
    while infix != 'q':
        print("postfix is :", infixToPrefix(infix))
        infix = input("Please input infix expression('q' for Quit): ")
