str="siddaganga_polytechnic"
st="abc"
op = ""
for i in range(0,len(str),3):
  substr= str[i:i+3]
  op = op+substr
  if not (i == len(str)-1):
    op = op+st
print(str)
print(st)
