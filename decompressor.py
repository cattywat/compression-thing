directory=input('directory: ')
infile=open(directory+'compressed','r',encoding='utf8')
outfile=open(directory+'decompressed','w',encoding='utf8')
content=infile.readline().split(' ')
dictionary=infile.readlines(-1) #open(directory+'dictionary','r',encoding='utf8').readlines(-1)
infile.close()
print(content)
for num in content:
    if(num=='\n'):
        break
    outfile.write(str(dictionary[int(num)].split('\n')[0])+' ')
outfile.close()