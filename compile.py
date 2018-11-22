import re
st=input("enter the string")
result=re.findall(r"\w",st)
print(result)
print("...............")
import re
st=input("enter the string")
result=re.findall(r"\w*",st)
print(result)
print(".................")
import re
st=input("enter the string")
result=re.findall(r".",st)
print(result)
print("..............")
import re
st=input("enter the string with digits ")
result=re.findall(r"\d",st)
print(result)