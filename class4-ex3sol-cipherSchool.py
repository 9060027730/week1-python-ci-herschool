name,char = input("enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")
# Rahul - rahul
# H - h
#name.lower().count(char.lower())
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()