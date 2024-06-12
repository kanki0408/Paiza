# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
b = [[0]*N]*N
result = []
count = 0

for i in range(N):
    b[i] = list(map(int,input().split(' ')))

for i in range(N):
    for l in range(N):
        if(i-1 >0):
            if(b[i][l]>b[i-1][l]):
                count+=1
        else:
            count+=1
        if(l-1 >0):
            if(b[i][l]>b[i][l-1]):
                count+=1
        else:
            count+=1
        if(i+1 < N):
            if(b[i][l]>b[i+1][l]):
                count+=1
        else:
            count+=1
        if(l+1 < N):
            if(b[i][l]>b[i][l+1]):
                count+=1
        else:
            count+=1  
        if(count==4):
            result.append(b[i][l])
            count = 0
        else:
            count=0

result = sorted(result,reverse=True)
for i in range(len(result)):
    print(result[i])