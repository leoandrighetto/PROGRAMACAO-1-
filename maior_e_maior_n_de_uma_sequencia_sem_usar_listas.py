maior=0
menor=0
n=int(input())
maior=n
menor=n
while n!=0:
  n=int(input())
  if n>maior:
    maior=n
  if n<menor and n!=0:
    menor=n
print(maior)
print(menor)
