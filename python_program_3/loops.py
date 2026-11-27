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