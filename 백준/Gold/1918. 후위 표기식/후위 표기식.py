def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '(':0}
    stack = []
    output = []

    for char in expression:
        if char.isalpha():  # 피연산자면 바로 출력
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # '(' 제거
        else:  # 연산자일 경우
            while stack and precedence[stack[-1]] >= precedence[char]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# 입력
expression = input().strip()

# 출력
print(infix_to_postfix(expression))
