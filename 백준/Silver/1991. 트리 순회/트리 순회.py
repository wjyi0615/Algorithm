# 트리 저장용 딕셔너리
tree = {}

# 트리 입력 받기
n = int(input())
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

# 전위 순회
def preorder(node):
    if node == '.':
        return
    print(node, end='')        # (루트)
    preorder(tree[node][0])     # (왼쪽)
    preorder(tree[node][1])     # (오른쪽)

# 중위 순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])      # (왼쪽)
    print(node, end='')         # (루트)
    inorder(tree[node][1])      # (오른쪽)

# 후위 순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])    # (왼쪽)
    postorder(tree[node][1])    # (오른쪽)
    print(node, end='')         # (루트)

# 항상 A가 루트
preorder('A')
print()
inorder('A')
print()
postorder('A')
