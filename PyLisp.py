import re, operator


#PyLisp 
#interpreter for Lisp written in python

#Sample Data
line = "(* (2)(- 130 2)(+ 1 1 1 1)(/ 9745939781548 101912))"

#Do formatting on bad input data
validOps = ["+", "-", "*", "/", "%"]
for validOp in validOps:
    if validOp in line:
        line = line.replace("(%s" % validOp, "( %s" % validOp)
        line = line.replace("%s(" % validOp, "%s (" % validOp)
line = re.sub(r"(\d)(\))", r"\1 \2", line)
line = re.sub(r"(\()(\d)", r"\1 \2", line)
rep = {"((" : "( (", "))" : ") )", ")(" : ") ("}
rep = dict((re.escape(k), v) for k, v in rep.iteritems())
pattern = re.compile("|".join(rep.keys()))
line = pattern.sub(lambda m: rep[re.escape(m.group(0))], line)

#Reducer: takes an operator i.e. "+" and a list of ints to reduce
def reducer(operation, listOfNumbers):
    op = {'+' : operator.add,'-' : operator.sub,'*' : operator.mul,'/' : operator.div, '%' : operator.mod,}[operation]
    return reduce(lambda x, y: (op(x,y)), listOfNumbers)

#Interpret a line of Lisp
def process_line(line):
    opstack = []
    operandStack = []
    operands = []
    finalOperands = []

    #Iterate through list of Lisp code
    for index, x in enumerate(line.split()):
        if x in ["(", "+", "-", "*", "/", "%"]:
            opstack.append(x)
        if x.isdigit():
            operandStack.append(int(x)) 
        if x == ")":
            
            #If we get to the last ')'
            if index == (len(line.split()) - 1) - line.split()[::-1].index(')'):
                for item in finalOperands:
                    operands.append(item)
                op = opstack.pop()
                print "LISP EXPRESSION: ", line , "\n\nEvaluates to: ", reducer(op, operands), "\n"
                break
            for item in operandStack:
                operands.append(item)
            operandStack = []

            #Get operation
            op = opstack.pop()

            #Account for single nums in parens => ( 3 )
            if not op in ["+", "-", "*", "/", "%"]:
                finalOperands.append(operands[0])   
            else:
                
                #Get rid of '('
                opstack.pop()

                #Append inner result to finalOperands
                finalOperands.append(reducer(op, operands))
            operands = []
process_line(line)