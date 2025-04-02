directory=input('file directory: ')
file=open(directory+'original','r',encoding='utf8')
dictionary=[]
outfile=open(directory+'compressed','w',encoding='utf8')
a=file.readline()
i=1
while a!='':
    b=a.split()
    for j in range(len(b)):
        found=False
        for k in range(len(dictionary)):
            if(b[j]==dictionary[k]):
                found=True
                outfile.write(str(k))
                break
        if(not found):
            dictionary.append(b[j])
            outfile.write(str(len(dictionary)-1))
        outfile.write(' ')
    print(i)
    a=file.readline()
    i+=1
#outfile.close()
#diction=open(directory+'dictionary','w',encoding='utf8')
outfile.write('\n')
for i in range(len(dictionary)):
    outfile.write(str(dictionary[i])+'\n')
outfile.close()
file.close()