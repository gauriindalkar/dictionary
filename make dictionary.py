list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
d=dict()
n=list2[0]
for i in list1:
    d[i]=n
    n+=1
print(d)