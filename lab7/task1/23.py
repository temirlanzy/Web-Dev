n=int(input())
cnt=0
numbers = [int(input()) for _ in range(n)]
for i in numbers:
    if i == 0:
        cnt+=1
print(cnt)