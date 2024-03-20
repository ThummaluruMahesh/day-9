# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

'''
s1 = "hello how are you"
s2 = "hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")


for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
are
you
is
'''

# 3.)Wrire a code print the 8th fibanochi number
#0,1,1,2,3,5,8
'''
n1 = 0
n2 = 1
ans = 0+1 ==> 1

n1 =1
n2 = 1
ans = 1+1 ==>2

n1 = 1
n2 = 2
ans = 1+2 ==>3
'''



# ! Find the  8th fibanochi number
'''
num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)

 34

'''

# ! constructors
# Eg :2
'''
class profile:
    def _init_(self):
        print("hello world")

obj = profile()
obj._init_()

hello world
'''

#  Eg:3

# * parametarised constructor
'''
class profile:
    def __init__(self, id, name, age):
        print(id,name,age)

obj = profile(1, "mahi",22)

1 mahi 22

'''

# ? Eg:4
'''
class c1:
    email = "mahesh@gmail.com"
    
    def m1(self):
        name = "mahi"
        place = "cbe"
        print(name,place)
        print(self.email)

object = c1()
object.m1()

mahi cbe
mahesh@gmail.com

'''

# ? Eg:5
'''
class c1:
    def m1(self):
        name = "mahi"
        age = 22
        return name,age
    def display(self):
       # ! print(name,age)
       # ! print(self.name,self.age)
       print(self.m1())

object = c1()
object.display()

('mahi', 22)

'''
# ? Eg:6
# ? To use the variable inside the constructor in another methods
'''
class class1:
    def __init__(self):
        self.name = "mahi"
        self.email = "mahesh@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name,self.email)


c1 = class1() 
c1.display()

mahi mahesh@gmail.com

'''

# ! ----> Inheritance
#The process of utilising the methods and attributes of parent class
#through the object of child class it is called as inheritance

# ? 5 types of inheritance
# single inheritance
# multilevel inheritance
# multiple inheritance
# hybrid inheritance
# heirarichal inheritance

# * Single Inheritance
# ? It has only one parent class and only one child class 
# ! Eg:1
'''
class parent:
    def m1():
        print("I am parent class")

parent.m1()

I am parent class

class child:
    def m2(self):
        print("I am child class")
'''
'''
class parent(child):
    def m1(self):
        print("I am parent class")


class child:
    def m2(self):
        print("I am child class")

p = parent()
p.m2()

#obj = child()
#obj.m1()

'''

# ! Eg:2
'''
class c1:
    def __init__(self):
        print(" I am constructor from parent class")

class child1(c1):
    pass
obj = child1()

I am constructor from parent class
'''
# ! Eg:3
'''
class parent:
    name = "mahi"


class child(parent):
    name = "name1"
    
    def display(self):
        print(self.name)

d = child()
d.display()

name1
'''


# ! Multilevel inheritance

# ? Eg:1
'''
class voice:
    def sound(self):
        print("All the animals have thair own voice")


class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")


all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


bark
meow
All the animals have thair own voice
speak
'''

# ? Eg:2
'''
class honda_city:
    def honda_city_engine_specs(self,cc,hp,torque,fuel_type,num_of_piston):
        print(cc,hp,torque,fuel_type,num_of_piston)

    def honda_city_body_specs(self,color,weight,height,length,vehical_type):
        print(color,weight,height,length,vehical_type)


class amaze:
    def amaze_engine_specs(self,cc,hp,torque,fuel_type,num_of_piston):
        print(cc,hp,torque,fuel_type,num_of_piston)

    def amaze_body_specs(self,color,weight,height,length,vehical_type):
        print(color,weight,height,length,vehical_type)


class civic:
    def civic_engine_specs(self,cc,hp,torque,fuel_type,num_of_piston):
        print(cc,hp,torque,fuel_type,num_of_piston)

    def civic_body_specs(self,color,weight,height,length,vehical_type):
        print(color,weight,height,length,vehical_type)


class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engine_specs(1500, 230,2979,"petrol",4)
honda.civic_body_specs("white",2000,5.5,8,"hatchback")

'''
# ! Multiple Inheritance
# ? It has multiple parent and 1 child
'''
class while_petrol:
    def function1(self):
        print("used to airplans")

class Organic_petrol:
    def function_o(self):
        print("used for bike, cars")


class premium_petrol:
    def function_p(self):
        print("sports cars, bikes")

class petrol(while_petrol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols types")

p = petrol()
p.defanition()
p.function_o()

petrols types
used for bike, cars

'''

# ! Eg:2
# MRO --> method resolution order
'''
class addition:
    def add(self,a,b):
        print(a+b)

class subract:
    def sub(self,a,b):
        print(a-b)

class multiply:
    def mul(self,a,b):
        print(a*b)

class division(addition,subract,multiply):
    def div(self,a,b):
        print(a/b)
        
calc = division()
calc.add(3,4)
calc.mul(5,2)

7
10
'''
'''
class addition:
    def add(self,a,b):
        print(a+b)

    def mul(self,a,b):
        print(a%b)
    
class subract:
    def sub(self,a,b):
        print(a-b)

class multiply:
    def mul(self,a,b):
        print(a*b)

class division(addition,subract,multiply):
    def div(self,a,b):
        print(a/b)
        
calc = division()
calc.add(3,4)
calc.mul(5,2)

7
1
'''

# ! Heirarical inheritance
'''
class catagory:
    def weight(self,weight):
        print(weight)

class Tomato(catagory):
    def tomato_specs(self):
        color ="black"
        taste ="neutral taste"

class carrot(catagory):
    def carrot_specs(self):
        color ="green"
        taste ="sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

30gms
'''
'''
class catagory:
    def weight(self,weight):
        print(weight)

    def display(self,color,taste):
        print(color,taste)

class Tomato(catagory):
    def tomato_specs(self):
        color ="black"
        taste ="neutral taste"
        self.display(color, taste)

class carrot(catagory):
    def carrot_specs(self):
        color ="green"
        taste ="sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t.tomato_specs()
t.weight("20gms")

30gms
black neutral taste
20gms
'''

# ! Hybrid inheritance
# ? The combination of above 4 inheritance is called Hybrid inheritance
'''
class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class3")

class c4(c3):
    def m4(self):
        print("class4")

    def m3(self):
        print(" i am m3 from c4")

class c5(c4):
    def m5(self):
        print("class5")
        
class c6(c5, c3):
    def m6(self):
        print("class6")

obj = c6()
obj.m3()

 i am m3 from c4

'''

# ! -------> polymorphism
# poly - many, morph --> form
# A function which has the ability to perform more than 1 functionality
# then iot is considerd to be as plioymorphism


# * plyomorphism in builtin functions
# len() ---> which is used to find the length of list, tuple, dict etc.....
# index()
# max()
# min()
# count()
# pop()


# * ploymorphism in operators
# +
'''
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

16
k1
[1, 2, 3, 5, 6]

'''

# *
'''
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)

42
3 4 5 6 12
#def f1(*args)
'''
'''
l1 = [1,2,3,4]
print(l1*10)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
'''


# ploymorphism in classes
# we can achieve polymorphism in 2 ways
# 1.) method overloading ---> it is not possible in python
# 2.) method overloading

# 1.) tasks
# write the code for the below tasks using function
# 1.) {"shirt":1000,"pant":1500,"shoes":900,"handkey":30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 's'

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 ---> [5,6 1,2,3,4]
# n=3 --> [4,5,6,1,2,3]

 
'''
Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -
'''







