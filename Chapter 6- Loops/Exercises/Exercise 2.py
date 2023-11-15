'''A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 

age, and then tell them the cost of their movie ticket'''

while True:
    age =  input("What is your age? ")
    if age == 'Quit':
        break
    age = int(age)
    #For age 3-12
    if age <=12:
        print("Your ticket is 10$")
        #For age 3
    elif age <3:
        print("Your ticket is free")
        #For age 12+
    else:
        print("your ticket is 15$")

   # print(f"The cost of your movie ticket is")
