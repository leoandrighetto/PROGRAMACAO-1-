l=[0,1]
n=int(input())
for i in range(n):
    l.append(l[-1]+l[-2])
if n in l:
    print('sim')
else:
    print('não')
