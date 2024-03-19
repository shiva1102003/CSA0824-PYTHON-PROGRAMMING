l=[]
n=int(input("enter any number: "))
m=int(input("enter another number: "))
x=int(input("enter limit: "))
for i in range(0,x+1):
    if i%n==0 and i%m==0:
        l.append(i)
print(sum(l))
