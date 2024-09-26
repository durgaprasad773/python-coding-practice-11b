s=input()
res=""
for i in s:
    res = i + res
if res == s:
    print(True)
else:
    print(False)