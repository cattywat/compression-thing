import frequencyanalyser
import math

length=100000
file=open(input(),'r',encoding='utf8')
encoder, decoder = frequencyanalyser.analyse(file,length)

final=open('compressed.txt','wb')
final.write(bytes(str(decoder),encoding='utf8'))
final.write(bytes(1))
file.seek(0)
c=file.read(1)
for i in range(length-5):
    if(not c):
        break
    try:
        print(encoder[c])
        print(int(encoder[c],2))
        print(int(encoder[c],2).to_bytes(math.ceil(len(encoder[c])/8)))
        final.write((int(encoder[c],2)).to_bytes(math.ceil(len(encoder[c])/8)))
    except KeyError as e:
        print(e.args[0])
    c=file.read(1)
file.close()
final.close()
