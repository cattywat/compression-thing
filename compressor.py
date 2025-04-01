length=13147026
file=open(input('source file: '),'r',encoding='utf8')
dictionary=[]
outfile=open(input('compressed file: '),'w',encoding='utf8')
for i in range(1000):
    a=file.readline()
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
outfile.close()
diction=open(input('dictionary file: '),'w',encoding='utf8')
for i in range(len(dictionary)):
    diction.write(str(dictionary[i])+'\n')
diction.close()
file.close()