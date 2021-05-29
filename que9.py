a="MISSISSIPPI"
h=[]
n={}
for i in a:
    h.append(i)
    s=h.count(i)
    n.update({i:s})
print(n)