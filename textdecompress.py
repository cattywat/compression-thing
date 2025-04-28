import ast

file=open(input(),'rb')
output=open('decompressed.txt','w',encoding='utf8')

c=file.readlines()
c=c[0].split(bytes(1))
dictionary = ast.literal_eval(c[0].decode(encoding='utf8'))
content = c[1].decode(encoding='utf8')