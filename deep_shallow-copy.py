import copy
a=[1,2,3,4]
b=a
print("a:",a,"\nb:",b,"\n")
b.append(5)
print('After Appending')
print("a:",a,"\nb:",b,"\n")  #both a and b changed

#Shallow copy
print("Shallow copy")
a=[1,2,3,4]
b=a.copy()
print("a:",a,"\nb:",b,"\n")
b.append(5)
print('After Appending')
print("a:",a,"\nb:",b,"\n")

c=[[1,2],[3,4]]
d=c.copy()
print("c",c,"\nd:",d,"\n")
d[0].append(5)
print('After Appending')
print("c",c,"\nd:",d,"\n") #inner list still changes

#Deep copy
print("Deep copy")
c=[[1,2],[3,4]]
d=copy.deepcopy(c)
print("c",c,"\nd:",d,"\n")
d[0].append(5)
print('After Appending')
print("c",c,"\nd:",d,"\n")