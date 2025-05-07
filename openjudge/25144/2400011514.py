from collections import deque

n = int(input())
if n == 0:
    print(0)
    exit()

children = {}
all_children = set()

for i in range(n):
    left, right = map(int, input().split())
    children[i] = (left, right)
    if left != -1:
        all_children.add(left)
    if right != -1:
        all_children.add(right)

# 找出根节点
root = -1
for i in range(n):
    if i not in all_children:
        root = i
        break

max_width = 0
queue = deque([root])

while queue:
    level_size = len(queue)
    if level_size > max_width:
        max_width = level_size
    for _ in range(level_size):
        node = queue.popleft()
        left, right = children[node]
        if left != -1:
            queue.append(left)
        if right != -1:
            queue.append(right)

print(max_width)