# Mad Libs Generator

# Loop back to this point once loop finishes.

loop = 1
while (loop < 10):
# Questions that the program asks the user.
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
# Displays the story, user input.
    print("---------------------------------------------------")
    print("Be kind to your",noun," - footed", p_noun)
    print("For a duck may be somebody's", noun2,",")
    print("Be kind to your",p_noun,"in",place)
    print("where the weather is always",adjective,".")
    print()
    print("You may think that this the",noun3,",")
    print("Well it is.")
    print("---------------------------------------------------")
#Loop back to loop one.
    loop = loop + 1

input("Thanks for Playing")
    
    