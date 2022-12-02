'''
Creating a python project in orderto create a new game called the madlib through using string concatention
'''

#Taking Inputs from the user Through the propmt command#

print ("Hi There WE ar actually Glad To Have You Here , will be creating an Entire Introduction For You. Just Enter the following details.")
name = input ("Enter Your Name here : ");
age = input("Enter Your Age here : ");


#Converting The Age entered by the user into a numeric value#

age = int(age);

if age >= 18:
    profession = input("enter your proffession & Company in which you work : ")

else:

    school = input("Enter Your school Name Here : ")





Hobby = input("Enter Your Hobby Here : ");
Favourite_destination = input("Enter Your Favourite Destination : ");


#printing the if-else staement as per the age inputs given by the user#
if age <= 17 :
 Create_Statement = f"Hi there my name is {name}.My Age is {age}.I study in {school}.My hobbies are {Hobby}.mY favourite " \
                   f"tourist destination is {Favourite_destination}."
 print(Create_Statement)
 
 
else:
 Create_Statement = f"Hi there my name is {name}.My Age is {age}.i am {profession} by profession.My hobbies are {Hobby}.mY favourite " \
                    f"tourist destination is {Favourite_destination}."
 print(Create_Statement)