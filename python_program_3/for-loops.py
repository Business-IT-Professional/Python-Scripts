#METHOD No: 1
strings =["dianasours", "tiger", "forest", "mountains", "trees","grass"," glacier", "stream"]
for str_i in strings:
    print("Nabeel you are Great!")


#METHOD No: 2
for var_2 in range (10):
    if var_2==5:
        continue #Often  used to skip the required entity
    print(var_2)


#METHOD No: 3
for var_4 in range(5+1):
    if var_4 ==3:
        continue
    print(var_4)


#METHOD No: 4
var_5=[1,2,4,5,6,12,45,56,67]
for var_4 in var_5:
    print(var_4)



#(1)
list_1 =["start", "stars", "wind", "green field", 3000, 4000,5000,6000]
for var_5 in list_1:
    if var_5 == 3000:
        break
    print(var_5)


#A SMALL DIFFENCE BETWEEN THE BOTH CODES AS #1 PRINTS THE CONTENT AND STOPS AT THE REQUIRED POINT,
#WHILE THE #2 PRINTS THE CONTENT AND ALONG WITH THAT IT PRINTS THE ENTITY AT WHICH
# IT HAVE TO STOP BY SKIPING IT, IS BECAUSE THE PRINT() IS ABOVE THE CONDITION.


#(2)
list_1 =["start", "stars", "wind", "green field", 3000, 4000,5000,6000]
for var_5 in list_1:
    print(var_5)
    if var_5 == 3000:
        break
