# program to print minimum and maximum elements of a list
l=[]
n=int(input("Enter n:"))
for i in range(0,n):
    x=int(input())
    l.append(x)
min=l[0]   
max=l[0]
for i in range(1,n):
    if l[i]>max:
        max=l[i]
    else:
        min=l[i]
print("maximum element is: ",max)
print("minumum element is: ",min)
