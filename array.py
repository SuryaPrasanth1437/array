N=int(input())
K=int(input())
sum1=0
for num in range(1,N+1):
    if K>0:
        sum1+=num
        K=K-1
        
print(sum1)
