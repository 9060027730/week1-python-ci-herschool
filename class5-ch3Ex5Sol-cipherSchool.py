name = str(input("Please enter your name "))
# harshit

# name.count("h"),name.count(name[0])=2
# name.count("a"),name.count(name[1])=1
# name.count("r"),name.count(name[2])=1
# name.count("s"),name.count(name[3])=1
# name.count("h"),name.count(name[4])=2
# name.count("i"),name.count(name[5])=1
# name.count("t"),name.count(name[06)=1

# output
# name[0]=h:2
# a : 1
# r : 1
# s : 1
# h : 2
# i : 1
# t : 1
temp_var=""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1