import ast

file=open(input(),'rb')
output=open('decompressed.txt','w',encoding='utf8')

c=file.readlines()
dictionary = ast.literal_eval(c[0].split(bytes(1),1)[0].decode(encoding='utf8'))
stream = ''
for i in range(len(c)):
    if(i==0):
        content=c[0].split(bytes(1),1)[1]
        for j in range(len(content)):
            stream+=format(content[j],'08b')
    else:
        content=c[i]
        for j in range(len(content)):
            stream+=format(content[j],'08b')

i=0
while len(stream)>0:
    i=0
    while sum(1 for item in list(dictionary.keys()) if item.startswith(stream[0:i]))>=1:
        try:
            if(dictionary[stream[0:i]]=='EOF'):
                stream=stream[i:]
                break
            output.write(dictionary[stream[0:i]])
            stream=stream[i:]
            i=0
            print(len(stream))
        except KeyError:
            i+=1
    print('panic or done')
output.close()