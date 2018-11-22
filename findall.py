import re
st=input("enter string")
result=re.findall(r"Hai",st)
print(result)
print(len(result))
print(result[0])
if result==[]:
    print("pattern not found")
else:
    print("pattern found")