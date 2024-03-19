string = "My name is CHAITU"
lowercase = 0
uppercase = 0
for char in string:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
print(f"The number of lowercase letters is: {lowercase}")
print(f"The number of uppercase letters is: {uppercase}")
