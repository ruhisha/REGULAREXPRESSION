import re
st=input("enter the string  ")
result=re.findall(r"^\w+",st)
print(result)
print("..................")
import re
st=input("enter the string  ")
result=re.findall(r"\w+$",st)
print(result)
print("..................")
import re
st=input("enter the string  ")
result=re.findall(r"\d\w+",st)
print(result)
print("..................")
import re
st=input("enter the string  ")
result=re.findall(r"\b\w.",st)
print(result)
print("..................")

