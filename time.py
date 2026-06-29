import time
start=time.time()
for i in range(1,101):
    print(i)
print(time.time()-start)
start=time.time()
i=1
while(i<101):
    print(i)
    i+=1
    
print(time.time()-start)