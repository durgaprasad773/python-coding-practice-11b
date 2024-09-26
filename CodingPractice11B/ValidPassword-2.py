s=input()
is_valid = False
for i in s:
    if i.isupper():
        is_valid=True
if is_valid:
    print("Valid Password")
else:
    print("Invalid Password")