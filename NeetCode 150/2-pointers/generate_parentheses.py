def generateParenthesis(n: int) -> list[str]:
    solutions = []
    stack = []

    def recursive(opened=0, closed=0) -> list[str]:
        if opened == closed == n:
            solutions.append(''.join(stack))

        if opened < n:
            stack.append('(')
            recursive(opened + 1, closed)
            stack.pop()

        if closed < n and closed < opened:
            stack.append(')')
            recursive(opened, closed + 1)
            stack.pop()

    recursive()
    return solutions
