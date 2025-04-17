import random


def main():
    
    userInput = int(input("Enter random_number:"))
    randNum=random.randrange(1,5)
    while userInput != randNum:
        print("Wrong Answer", userInput,randNum)
        if userInput > randNum:
            print("THe number you inputed is greater")
        else:
            print("The number you inputed is not greater")
        userInput = int(input("Enter any_number:"))
        randNum=random.randrange(1,5)
        




# def random_number():
# print("The random number is: ", random_number)
# def guess():
#  while guess != random_number:
#   try:
#     guess < random_number

#   except:
#      print("The random number is: ", random_number)
# random_number()

main()    