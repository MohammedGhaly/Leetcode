def evalRPN(tokens: list[str]) -> int:
    operands = set(['+', '-', '*', '/'])
    stack = []
    for token in tokens:
        if token not in operands:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            res = int(eval(f'{a} {token} {b}'))
            stack.append(res)
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print((evalRPN(tokens)))
tokens = ["4", "13", "5", "/", "+"]
print((evalRPN(tokens)))
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print((evalRPN(tokens)))
