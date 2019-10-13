import random #importing a library

r = random.randint(0, 1000000)
while True:
    number = int( input ("What is your age:") )
    if   19 < number :
        print ("    ")
        print ("You are an Adult")
    if 10 < number <= 19:
        print ("    ")
        print ("You are an Adolescent")
    if 2 <= number <= 10:
        print ("    ")
        print ("You are a Child")
    if number <= 1:
        print ("    ")
        print ("You are an Infants")
            