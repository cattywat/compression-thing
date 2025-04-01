infile=open(input('compressed file: '),'r',encoding='utf8')
dictionary=open(input('dictionary file: '),'r',encoding='utf8').readlines(-1)
outfile=open(input('output file: '),'w',encoding='utf8')
content=infile.readline().split(' ')
infile.close()
for num in content:
    outfile.write(str(dictionary[int(num)])+' ')
outfile.close()