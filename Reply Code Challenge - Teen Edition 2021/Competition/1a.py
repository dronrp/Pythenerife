a = list(map(int, input().split()))
n = int(input())
i = 0
j = 2
cnt = 1
m = min(a)
while j < m:
    if a[i]%j !=0:
        j += 1
    else:
        if i == n-1:
            cnt+=1
            i=0
            j+=1
        else:
            i+=1
print(cnt)
