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

stream=''
for i in range(len(content)):
    temp=bin(content[i])[2:]
    while len(temp)<8:
        temp='0'+temp
    stream+=temp
    print('processing ' + str(round(100*i/len(content),2)))

i=0
while len(stream)>0:
    i=0
    while sum(1 for item in list(dictionary.keys()) if item.startswith(stream[0:i]))>=1:
        try:
            output.write(dictionary[stream[0:i]])
            stream=stream[i:]
            i=0
            print(len(stream))
        except KeyError:
            i+=1
            continue
    print('panic')
output.close()