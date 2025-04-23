directory=input('file directory: ')
file=open(directory+'original','br')
dictionary=[]
outfile=open(directory+'compressed','bw')
a=file.read()

while(len(a)>1):
    found=False
    for i in range(len(a)):
        if not (a[0:int((len(a)-i)/2)] in dictionary):
            break
        elif(a[0:-i] in dictionary):
            print(i)
            for k in range(len(dictionary)):
                if(dictionary[k]==a[0:-i]):
                    found=True
                    a=a[-i:]
                    outfile.write(bytes(str(k)+' ',encoding='utf8'))
                    break
    if not found:
        maxlen=0
        total=0
        for j in range(len(a)):
            if(j==1):
                continue
            elif(total>=0.99*len(a)):
                break
            elif(j*a.count(a[0:j])>total):
                maxlen=j
                total=j*a.count(a[0:j])
            elif(a.count(a[0:j])==1):
                break
        dictionary.append(a[0:maxlen])
        outfile.write(bytes(str(len(dictionary)-1)+' ',encoding='utf8'))
        a=a[maxlen:]
    print(len(a))
    print(dictionary[-1])
if(len(a)==1):
    if(a in dictionary):
        for k in range(len(dictionary)):
            if(dictionary[k]==a):
                a=a[-i:]
                outfile.write(bytes(str(k)+' ',encoding='utf8'))
                break
        i+=1
    if not found:
        dictionary.append(a)
        outfile.write(bytes(str(len(dictionary)-1)+' ',encoding='utf8'))

outfile.write(b'\n')
for i in range(len(dictionary)):
    outfile.write(bytes(str(dictionary[i])+'\n',encoding='utf8'))
outfile.close()
file.close()
