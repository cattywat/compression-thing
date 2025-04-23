directory=input('directory: ')
infile=open(directory+'compressed','br')
outfile=open(directory+'decompressed','bw')
content=infile.readline().decode('utf8').split(' ')
dictionary=infile.readlines(-1)
infile.close()
for num in content:
    if(num=='\n'):
        break
    outfile.write(bytes(str(dictionary[int(num)].decode('utf8').split('\n')[0])+' ',encoding='utf8'))
outfile.close()