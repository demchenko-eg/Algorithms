n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
In = [0] * n
Out = [0] * n
for u, v in A:
    Out[u - 1] += 1
    In[v - 1] += 1
for i in range(n):
    print(In[i], Out[i])