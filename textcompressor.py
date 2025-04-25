import frequencyanalyser

length=100000
file=open(input(),'r',encoding='utf8')
encoder, decoder = frequencyanalyser.analyse(file,length)

final=open('compressed.txt','w',encoding='utf8')
final.write(str(decoder)+'\n')
c=file.read(1)
for i in range(length-5):
    try:
        final.write(encoder[c])
    except KeyError as e:
        print(e.args[0])
    c=file.read(1)
file.close()
final.close()