import random

#A function do shuffle all the characters of a string
def shuffle(string):
    random.shuffle(tempList)
    return ''.join(tempList)



#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter3=chr(random.randint(65,90))
#Generate more characters here
#...

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter3 # + ....

#Output
print(password)

input("Thank you!")
