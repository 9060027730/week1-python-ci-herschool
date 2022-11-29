number = input("enter a number ")
# "1234" 
# int(number[i])
total = 0
i = 0
while i < len(number):
    total +=int(number[i])
    i += 1
print(total)