class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        c = 0

        if len(tokens) < 2:
            return int(tokens[0])

        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t  == '+':
                    c = a + b
                elif t  == '-':
                    c = a - b
                elif t  == '*':
                    c = a * b
                elif t  == '/':
                    c = int(a/b)
                stack.append(c)

        return c
