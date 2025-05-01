import ast

file=open(input(),'rb')
output=open('decompressed.txt','w',encoding='utf8')

c=file.readlines()
dictionary = ast.literal_eval(c[0].split(bytes(1),1)[0].decode(encoding='utf8'))
content = b''
for i in range(len(c)):
    if(i==0):
        content+=c[0].split(bytes(1),1)[1]
    else:
        content+=c[i]

print(dictionary)