import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    commands = data[1:]

    stack = []
    result = []
    idx = 0

    for _ in range(n):
        cmd = commands[idx]
        if cmd == '1':
            idx += 1
            x = int(commands[idx])
            stack.append(x)
        elif cmd == '2':
            if stack:
                result.append(str(stack.pop()))
            else:
                result.append('-1')
        elif cmd == '3':
            result.append(str(len(stack)))
        elif cmd == '4':
            result.append('1' if not stack else '0')
        elif cmd == '5':
            if stack:
                result.append(str(stack[-1]))
            else:
                result.append('-1')
        idx += 1

    print('\n'.join(result))

if __name__ == "__main__":
    main()
