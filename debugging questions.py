# question 1
# a = {(1,2):1,(2,3):2}
# print(a[1,2]) 
# output=1

#question 2
# a = {'a':1,'b':2,'c':3}
# print (a['a','b']) 
# output=key error

#question 3
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit) 
# output=3
# {"apple":2,"banana":1,"apple":1}

# question 4
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 
# output=1

#question 5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict) 
# output=30
# {(1,2,4):8,(4,2,1):10,(1,2):12}
 
#question 6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates['box'])) 
# output=2
# print(len(crates[box]))
# output=type error

#question 7
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)
# output=True

