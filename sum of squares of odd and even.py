a=['18','9','1','12','13','4','30']
b=0
c=0
for i in range(0,7):
    if a[i]%2==0:
        b+=a[i]**2
    else:
        c+=a[i]**2
print(b,c)
