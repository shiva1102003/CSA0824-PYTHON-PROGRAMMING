n=int(input("enter a number: "))
sum=0
for i in range(1,n):
    rem=n%i
    if rem==0:
        sum+=i
if sum==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
