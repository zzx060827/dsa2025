from stack import Stack
from in2post import infixToPostfix

def postfixEval(postfixExpr):
    doMath = {'*': lambda x, y : x * y,
              '/': lambda x, y : x / y,
              '+': lambda x, y : x + y,
              '-': lambda x, y : x - y
              }
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath[token](operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

if __name__ == "__main__":
    infix = input("Please input infix expression(tokens seperated by blank, 'q' for Quit): \n")
    while infix != 'q':
        postfix = infixToPostfix(infix)
        print("postfix is :", postfix)
        print("Result is :", postfixEval(postfix))
        infix = input("More expression('q' for Quit): \n")
