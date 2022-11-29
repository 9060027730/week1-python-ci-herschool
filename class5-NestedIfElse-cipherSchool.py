# Extercise solution
winning_number=27
user_input = int(input("Guess a number b/w 1 and 100 :"))
if user_input == winning_number:
    print("you WIN !!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")