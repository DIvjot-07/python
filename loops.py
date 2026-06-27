print("Numbers from 1-10 :",end=' ')
for i in range(1,11):
    print(i,end=' ')
print("\n")

print("Numbers from 10-1 :",end=' ')
for i in range(10,0,-1):
    print(i,end=' ')
print("\n")

print("Even Numbers from 1-50 :",end=' ')
for i in range(0,50+1,2):
    print(i,end=' ')
print("\n")

print("Odd Numbers from 1-50 :",end=' ')
for i in range(0,50+1,1):
    if(i%2==0):
        continue
    else:
        print(i,end=' ')
print("\n")

i=1
print("Numbers from 1-10 :",end=' ')
while(i<101):
    print(i ,end=' ')
    i += 1
print("\n")

Fruits=["Apple","Mango","Banana", "Cherry"]
print("Fruits :",end=" ")
for i in Fruits:
    print(i ,end=" ")
print('\n')

print("Fruits")
for i , fruit in enumerate(Fruits):
    print(i+1 ," : ",fruit)
print('\n')

print("Numbers from 1-100 that are not multiples of 2,3,5 :",end=" ")
count=0
for i in range(1,101,1):
    if(i%2==0 or i%3==0 or i%5==0):
        continue
    else:
        print(i,end=" ")
        count+=1
print(f"\nCount : {count}")
print("\n")

