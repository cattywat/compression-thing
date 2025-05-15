import frequencyanalyser

length=1000000
file=open(input(),'r',encoding='utf8')
encoder, decoder = frequencyanalyser.analyse(file,length)

final=open('compressed.txt','wb')
final.write(bytes(str(decoder),encoding='utf8'))
final.write(bytes(1))
file.seek(0)
c=file.read(1)
stream=''
for i in range(length-5):
    if(not c):
        break
    stream+=encoder[c]
    if(len(stream)>=8):
        final.write((int(stream[0:8],2)).to_bytes(1,byteorder='big',signed=False))
        stream=stream[8:]
    c=file.read(1)
while(len(stream)<8):
    stream+='0'
final.write((int(stream[0:8],2)).to_bytes(1,byteorder='big',signed=False))
file.close()
final.close()
