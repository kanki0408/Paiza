# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,M = map(int,input().split(' '))
b = [[0]*2]*M
c = [0]*N
result = [0]*1
for i in range(M):
    b[i] = list(map(int,input().split(' ')))

for i in range(M):
    for l in range(N):
        if(b[i][0]==l):
            c[l] += 1

result[0] = c.index((max(c)))
for i in range(len(c)):
    if(c[0]==c[i]):
        result.append(c.index((max(c))))
    
for i in range(len(result)):
    print(result[i])
    
    
    # coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,M = map(int,input().split(' '))
b = [[0]*2]*M
c = [0]*N
result = [0]*1
for i in range(M):
    b[i] = list(map(int,input().split(' ')))

for i in range(M):
    for l in range(N):
        if(b[i][0]==l):
            c[l] += 1
check = max(c)
for i in range(len(c)):
    if(c[i] == check):
        result.append(i)
    
for i in range(len(result)):
    print(result[i])