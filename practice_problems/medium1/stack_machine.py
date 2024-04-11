

# def minilang(string):
#     stack = []
#     register = 0

#     for token in string.split():
#         match token:
#             case 'PUSH':
#                 stack.append(register)
#             case 'ADD':
#                 register += stack.pop()
#             case 'SUB':
#                 register -= stack.pop()
#             case 'MULT':
#                 register *- stack.pop()
#             case 'DIV':
#                 register //= stack.pop()
#             case 'REMAINDER':
#                 register %= stack.pop()
#             case 'POP':
#                 register = stack.pop()
#             case 'PRINT':
#                 print(register)
#             case _:
#                 register = int(token)
#     return register

def minilang(program):
    stack = []
    register = 0

    for token in program.split():
        match token:
            case "ADD":
                register += stack.pop()
            case "DIV":
                register //= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "SUB":
                register -= stack.pop()
            case "PUSH":
                stack.append(register)
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _:
                register = int(token)

    return register



minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed because the `program` argument has no `PRINT` commands)
