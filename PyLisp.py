import re
#PyLisp 
#interpreter for Common Lisp written in python

line = "( 2 - 1 )"
def process_line(line):
    opstack = []
    operandStack = []

    for x in line.split():
        if x == "(" or x == "+" or x == "-" or x == "*" or x == "/":
            opstack.append(x)

        if x.isdigit():
            operandStack.append(x) 

        if x == ")":
            op1=operandStack.pop()
            op2=operandStack.pop()
            op=opstack.pop()
            #op = opstack.pop()

            if op == "+":
                operandStack.append(int(op1)+int(op2))

            elif op == "-":
                operandStack.append(int(op2)-int(op1))

            elif op == "*":
                operandStack.append(int(op1)*int(op2))

            elif op == "/":
                operandStack.append(int(op2)/int(op1))

    if not operandStack:
        return "Invalid expression"

    #operandStack[0]
    print operandStack

process_line(line)
