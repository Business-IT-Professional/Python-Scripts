#Typecasting means the conversion of the datatypes
# Truncation risk: Casting a decimal like 3.9 to
# an integer drops the decimal portion, resulting in 3




#TYPECASTING => Implicit Casting and Explicit Casting
#And Typecasting has the following synonyms:

# • Type conversion (widely used across languages and documentation)
# • Type coercion (often used for automatic or implicit conversions)
# • Type juggling (sometimes used for automatic type changes in
# dynamically typed languages)
# • Widening / narrowing (often used when describing conversions
# to larger or smaller data types)


# a=45
# print(float(45))
# print(int(45+2))
# print(str("45+45"))

#Example:
#Widening / narrowing (often used when describing conversions
# to larger or smaller data types)

# int_a = 4
# print(float(4)) # the conversion from larger smaller data type into the larger datatype



#USE CASES OF USING THE COMMENTS IN SOFTWARE DEVELOPMENT:

# 1. Explaining non-obvious logic: Clarify why an unusual approach or workaround is used rather than repeating what the code already shows.
# 2. Documenting complex algorithms: Summarize inputs, outputs, and edge cases before a dense block of logic.
# 3. Tracking pending tasks (TODO / FIXME): Mark unfinished features, technical debt, or edge cases to revisit later.
# 4. Linking to bug trackers or tickets: Reference an issue ID next to a patch so future readers can trace the historical context.
# 5. Warning against accidental changes: Flag fragile code, timing constraints, or business rules that could break if modified carelessly.



# -----------------------------<PRINTING DATA-TYPE NAMES>-----------------------
# print(type(3))
# print(type("string"))
# print(type(3.5))
# print(type(True))

# -----------------------------<GETTING USER INPUTS>----------------------------


# input_1 = input("enter your name: ")
# print(input_1, "is a good person")

# input_2 = input("your age: ")
# name = "Muhammad Ali"
# print(name, "is", input_2)

# print(name, "is a good person")

# -----------------------------<CONDITIONAL LOGIC>----------------------------


# print(3<4)
# print(4>=3)
# print(3!=9)
# print(4!=2**2)
# print(3==3)

# -----------------------------<CONDITIONAL LOGIC USER INPUTS>----------------------------
# a=5
# while a>0:

#     name_1=input("enter the name:")
#     name_2 = input("enter your name:")
#     print(name_1==name_2)
#     a=a-1
# print("Done!")



# num_a = 3
# num_b = 4
# print(num_a == num_b)



# input_a=input("enter your age:")
# num_b = 6
# input_a=int(input_a) #----Type conversion in different line of code
# print(num_b==input_a)
# print(type(input_a))


# input_a=int(input("enter your age:")) #-----Type conversion in the same line of code
# num_b = 56
# print(num_b==input_a)
# print(type(input_a))


# input_1= float(input("enter the number:"))

# print(input_1, "the type is:", type(input_1))


# -----------------------------<EXPLICIT CONVERSION>----------------------------
# num=1
# num1=2
# num=int(num)
# print(num)


# var_2=int(input("enter the content:"))
# print(type(var_2))

# var_2=input("enter the content:")
# var_2=float(var_2)
# print(type34(var_2))

# -----------------------------<IMPLICIT CONVERSION>----------------------------
# var_1=23
# var_2=4

# var_3=var_1*var_2
# print(var_3, type(var_3))


# var_1=4.5
# var_2=3
# var_3=var_1+var_2
# print(var_3, type(var_3))


# var_3="script"
# var_4="code"
# print(var_3+var_4)


# input_1=input("enter the number:")
# print(input_1, "the type is", type(input_1))

# -----------------------------<THE IF-ELSE-ELSIF STATEMENTS>----------------------------
pot_price = 3400
saucepan_price = 5000
if pot_price == saucepan_price:
    print("Price for both items is same!")
elif pot_price < saucepan_price:
    print("pot price is lesser!")
elif pot_price > saucepan_price:
    print("pot price is greater!")
else:
    print("Not Decided Yet :)")

#<INTERGRATING THE INPUT FOR MORE COMPLEX IF-ELSE STATEMENTS>

input_price = int(input)


# -----------------------------<PYTHON BEGINNER PROJECTS>----------------------------

