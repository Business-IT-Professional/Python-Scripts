#METHOD No: 1
def names(a):
    a="Your name is: Nabeel Essa"
    print(a)
names("")
names("")


#METHOD No: 2
def names():
    print("Your name is: Nabeel Essa")
    print("Your name is: Nabeel Essa")

names()

#METHOD No: 3
def scripts():
    var_1 ="I like the habit of reading annd continous learning"
    print(var_1)
    print(var_1)
    print(var_1)
    print(var_1)

scripts()

#METHOD No : 4

def database(name):
    if name == "ahmed":
        print("your are manager")
    elif name == "ali":
        print("you are the assistant secretary")
    elif name == "khasif":
        print("you are the head of the department")
    else:
        print("you are the not the authentic person")

database("ali")

#MORE PRACTISE ABOUT THE FUNCTIONS


#1
def canteen():
    print("my canteen is the best")
    print("my canteen is the best")

canteen()

#2
def animals():
    animal_name = "champanzee"
    print(animal_name)
    print(animal_name)
    print(animal_name)
animals()


#3
def forest(trees):
    print(trees+trees)
forest(23)


#4
def conditional_function(cond_i):
    if cond_i == 1:
        print("The addition of:",cond_i,"+",cond_i, "is =",cond_i + cond_i)
    elif cond_i == 2:
        print("The addition of:",cond_i,"+",cond_i, "is =",cond_i + cond_i)
    elif cond_i == 3:
        print("The addition of:",cond_i,"+",cond_i, "is =",cond_i + cond_i)
    elif cond_i == 4:
        print("The addition of:",cond_i,"+",cond_i, "is =",cond_i + cond_i)
    elif cond_i == 5:
        print("The addition of:",cond_i,"+",cond_i, "is =",cond_i + cond_i)
    else:
        print("Plz enter the intergers only from 1 - 5!")



conditional_function(1)
conditional_function(3)
conditional_function(4)
conditional_function("f")


#5
def input_func(input_1=input("Enter your name:"),input_2= int(input("Enter your age:"))):

    if input_1 == "Ahmed" and input_2==5:
        print("Yes! you",'''"''',input_1,'''"''','''are the brother of the Aliya
            and your age is''', '''"''',input_2,'''"''')

    elif input_1=="Aslam" and input_2>5:
        print("Yes! you",'''"''',input_1,'''"''', '''are the step brother of the
            Ayesha and your age is''', input_2)

    elif input_1=="mujtaba" and input_2 >=11:
        print("Yes! you",'''"''',input_1,'''"''','''neither the brother of Zainab
            nor your age is''', input_2)

    else:
        print("We are not supposed to move forward")


input_func()