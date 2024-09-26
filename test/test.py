import os

a = os.path.join("runs/checkpoints/all_mix", "33")

print(a)


A = [80, 70, 60, 50, 10, 30, 20, 10]

# 获取满足条件1的下标
indices = []
for i in [2, 3, 4, 6, 7]:
    if i < len(A):
        indices.append(i)
count = 7
# 找到值最小的3个下标
if len(indices) <= count:
    print(indices)
    exit(0)

min_indices = []
for i in range(count):
    min_index = min(indices, key=lambda x: A[x])
    min_indices.append(min_index)
    indices.remove(min_index)

print(min_indices)
