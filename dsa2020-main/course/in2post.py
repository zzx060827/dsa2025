from stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            assert(token in "+-*/")
            while opStack.size()>0 and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)

    while opStack.size()>0:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

if __name__ == "__main__":
    infix = input("Please input infix expression('q' for Quit): ")
    while infix != 'q':
        print("postfix is :", infixToPostfix(infix))
        infix = input("Please input infix expression('q' for Quit): ")
