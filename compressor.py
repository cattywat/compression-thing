directory=input('file directory: ')
file=open(directory+'original','r',encoding='utf8')
dictionary=[]
outfile=open(directory+'compressed','w',encoding='utf8')
a=file.read()

while(len(a)>0):
    i=0
    while i<len(a):
        found=False
        for k in range(len(dictionary)):
            if(dictionary[k]==a[0:-i]):
                found=True
                a=a[-i:]
                outfile.write(str(k)+' ')
                break
        i+=1
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
        outfile.write(str(len(dictionary)-1))
        a=a[maxlen:]

outfile.write('\n')
for i in range(len(dictionary)):
    outfile.write(str(dictionary[i])+'\n')
outfile.close()
file.close()
