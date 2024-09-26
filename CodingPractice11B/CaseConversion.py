s=input()
f = s[0]
string = s[1:]
res =""
for i in string:
    if i.isupper():
        res = res + " " + i
    else:
        res= res +i
print(f+res)