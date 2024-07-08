arr=[]
n=int(input("Enter the no.of limit"))
for i in range(n):
    arr.append(int(input("Enter the no")))
for i in range (1,n):
    elem=arr[i]
    if elem<arr[i-1]:
        for j in range(i+1):
            if elem<arr[j]:
                index=j
                for k in range(i,j,-1):
                    arr[k]=arr[k-1]
                    break
    else:
        continue
    arr[index]=elem
print("The sorted list is :-",arr)                    