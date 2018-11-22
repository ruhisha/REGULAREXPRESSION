import re
st=input("enter string")
result=re.match(r"Robert",st)
print(result.group(0))
print(result.start())
print(result.end())
if result==None:
    print("match not found")

else:
    print("match found")

