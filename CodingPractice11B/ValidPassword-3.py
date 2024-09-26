s=input()
is_upper=False
is_lower=False
is_digit = False
for i in s:
    if i.isupper():
        is_upper = True
    elif i.islower():
        is_lower = True
    elif i.isdigit():
        is_digit = True
if is_upper and is_lower and is_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    