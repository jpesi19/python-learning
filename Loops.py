#Looping for beginners
#Simple Ex 1
i = 0
print("Example 1: ")
while i<3:
    print(i)
    i+=1
#Simple Ex 2
j=0
print("Example 2: ")
while j<4:
    print(j)
    if(j==3):
        break
    j+=1
#Simple Ex 3, using break to exit a loop
k = 0
print("Example 3: ")
while k<6:
    print(k)
    if k==3:
        break
    k+=1
#Simple Ex 4, using continue to stop and continue a loop
l = 0
print("Example 4: ")
while l<6:
    l+=1
    if l==3:
        continue
    print(l)

#Simple Ex 5, using else when condition is no longer true
q = 1
print("Example 5:")
while q < 6:
    print(q)
    q+=1
else:
    print("q is no longer less than 6")

y = 0
while y<3:
    z = 0
    while z<3:
        if z % 2 == 1 and y % 2 == 1: 
            print("1-1")
        elif z % 2 == 1 and y % 2 ==0:
            print("1-0")
        elif z % 2 == 0 and y % 2 == 1: 
            print("0-1")
        elif z % 2 == 0 and y % 2 ==0:
            print("0-0")    
        z+=1 
    y+=1    
