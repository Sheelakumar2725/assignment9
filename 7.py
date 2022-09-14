#9th assignment
# To print first n even natural numbers in reverse order 


n=int(input("enter a number:"))
i=n
while i>=1:
    if i%2==0:
        print(i,end=' ')
    i-=1
print()    
