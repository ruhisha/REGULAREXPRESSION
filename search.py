import re
st=input("enter the string")
result=re.search(r"Hello",st)
print(result.group(0))
print(result.start())
print(result.end())
if result==None:
    print("search not found")
else:
    print("search found")

