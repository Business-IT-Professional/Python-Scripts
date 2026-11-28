#------------------<Loops>---------------------
#WHILE LOOP
#Multiple Experiments

#Exp No 1
input_var=int(input("enter the number: "))
input_var_1=int(input("enter the limit: "))
input_var_2=int(input("enter the number to be incremented: "))
while input_var_1>input_var:
    print(input_var_2," + 1 = ",input_var_2+1 )
    input_var_2=+1
    input_var_1= input_var_1-1
print("Done!")

#OUTPUT:
# 7  + 1 =  8
# 1  + 1 =  2
# 1  + 1 =  2
# 1  + 1 =  2
# 1  + 1 =  2
# Done!

#Exp No 2
input_var=int(input("enter the number: "))
input_var_1=int(input("enter the limit: "))
input_var_2=int(input("enter the number to be incremented: "))
while input_var_1>input_var:
    print(input_var_2," + 1 = ",input_var_2+1 )
    input_var_2= input_var_2+1
    input_var_1= input_var_1-1
print("Done!")

#OUTPUT
# 2  + 1 =  3
# 3  + 1 =  4
# 4  + 1 =  5
# 5  + 1 =  6
# Done!

#MORE OF WHILE-LOOPS
vari_1=15
while vari_1>10:
    print("Nabeel! you are the most genius person of the world")
    vari_1=vari_1-1
print("Done!")


#MORE DYNAMIC APPROACH
print("Remember you got only 5 chances!")
str_input = input("Enter the required word:")
string="house and mountains"
input_1 = 4
while str_input != string:
    print("You are outstanding Nabeel Essa believe me!")
    str_input = input("Enter the word again:")
    input_1 = input_1 - 1
    if input_1 == 0:
        break
    if str_input == string:
        break
print("Done!")

#OUTPUT (IF THE CONDITION IS NOT RIGHT)
# Remember you got only 5 chances!
# Enter the required word:cat
# You are outstanding Nabeel Essa believe me!
# Enter the word again:t
# You are outstanding Nabeel Essa believe me!
# Enter the word again:t
# You are outstanding Nabeel Essa believe me!
# Enter the word again:t
# You are outstanding Nabeel Essa believe me!
# Enter the word again:t
# Done!


#OUTPUT (IF THE CONDITION IS RIGHT)
# Remember you got only 5 chances!
# Enter the required word:house and mountains
# Done!



