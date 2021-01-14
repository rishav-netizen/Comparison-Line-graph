#
#
#
#
#
#
#
# hello everyone!!
# I am Rishav 
#This is a python map plotter 
# Which I have made 
# In this map plotter 
# it will take user inputs 
# of two people  
# about their marks 
# with their names 
# and after those in puts are taken successfully 
# the graphs will be plotted 
# depending on their inputs 
# it will be a comparison graph
# it will be a line graph 
# the graph will be very accurate 
# 
#Hope you all enjoy it 
#
# !!!!
# !!!!
# !!!!
#
# Thank You for watching 
# !!!!!!
#
#
#
#
#
#
#
#
#
#
import matplotlib.pyplot as plt
# import sklearn
subjects=['English','Hindi','Maths','Science','SST']
mr1=[]
mr2=[]
n1=input("Enter 1st Student Name-: ")
print("")
print(n1,"Enter your marks below.")
e1=int(input("Enter Your English Marks: "))
h1=int(input("Enter Your Hindi Marks: "))
m1=int(input("Enter Your Maths Marks: "))
s1=int(input("Enter Your Science Marks: "))
st1=int(input("Enter Your Social Studies Marks: "))
mr1.append(e1)
mr1.append(h1)
mr1.append(m1)
mr1.append(s1)
mr1.append(st1)
print("")
print("")
n2=input("Enter 2nd Student Name-: ")
print("")
print(n2,"Enter your marks below.")
e2=int(input("Enter Your English Marks: "))
h2=int(input("Enter Your Hindi Marks: "))
m2=int(input("Enter Your Maths Marks: "))
s2=int(input("Enter Your Science Marks: "))
st2=int(input("Enter Your Social Studies Marks: "))
mr2.append(e2)
mr2.append(h2)
mr2.append(m2)
mr2.append(s2)
mr2.append(st2)
print("Now graphs will be plotted on",n1,"'s",'and',n2,"'s",'marks.')
plt.plot(subjects,mr1,label=n1)
plt.plot(subjects,mr2,label=n2)

#plt.bar(subjects,mr1,label=n1)
#plt.bar(subjects,mr2,label=n2)

#plt.scatter(subjects,mr1,label=n1)
#plt.scatter(subjects,mr2,label=n2)

#plt.pie(subjects,mr1)#,label=n1
#plt.pie(subjects,mr2)#,label=n2

plt.title('Performance Chart')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.grid()
#plt.grid()   makes grip
plt.legend()
plt.show()