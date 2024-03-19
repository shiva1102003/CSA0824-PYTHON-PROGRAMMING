def binary_search(a,x):
    low=0
    high=len(a)-1
    while low<=high:
        mid =(high+low)//2
        if a[mid]<x:
            low=mid+1
        elif a[mid]>x:
            high=mid-1
        else:
            return mid
    return -1
a=[2,3,4,10,40]
x=10
result=binary_search(a,x)
if result!=-1:
    print(x," is at ",result)
else:
    print(x," is not found ")
