import re
st=input("enter the string  ")
result=re.findall(r"\w+",st)
print(result)
print("..................")
