n=int(input())
n2=int(input())

for p in range(n):
    print()
    for i in range(n,n+n2,1):
        print(i,end=" ")
    n-=1

