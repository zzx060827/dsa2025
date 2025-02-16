from stack import Stack
from in2post import infixToPostfix

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

if __name__ == "__main__":
    infix = input("Please input infix expression('q' for Quit): ")
    while infix != 'q':
        postfix = infixToPostfix(infix)
        print("postfix is :", postfix)
        print("Result is :", postfixEval(postfix))
        infix = input("Please input infix expression('q' for Quit): ")
