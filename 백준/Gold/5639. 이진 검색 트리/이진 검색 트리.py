import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기
input = sys.stdin.read

# 입력 읽기
preorder = list(map(int, input().split()))

def solve(start, end):
    if start > end:
        return
    
    root = preorder[start]
    mid = start + 1

    # root보다 큰 값이 처음 나타나는 위치 찾기
    while mid <= end and preorder[mid] < root:
        mid += 1

    # 왼쪽 서브트리
    solve(start + 1, mid - 1)
    # 오른쪽 서브트리
    solve(mid, end)
    # 루트 출력
    print(root)

# 시작
solve(0, len(preorder) - 1)
