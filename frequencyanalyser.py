def sort(toSort):
    for i in range(len(toSort)-1):
        swapped=False
        for j in range(len(toSort)-1-i):
            if(toSort[j][1]>toSort[j+1][1]):
                temp=toSort[j]
                toSort[j]=toSort[j+1]
                toSort[j+1]=temp
                swapped=True
        if(not swapped):
            return toSort
    return toSort
def breakdown(tree):
    if(type(tree)!=list):
        return {0:tree}

    left=breakdown(tree[0])
    right=breakdown(tree[1])

    final={}
    for key, value in left.items():
        temp='0'+str(key)
        final.update({temp:value})
    for key, value in right.items():
        temp='1'+str(key)
        final.update({temp:value})
    
    return final

def analyse(file,length):
    char=file.read(1)
    dictionary=[[char,1]]

    for i in range(length):
        char=file.read(1)
        found=False
        for i in range(len(dictionary)):
            if(dictionary[i][0]==char):
                dictionary[i][1]+=1
                found=True
        if not found:
            dictionary.append([char,1])

    tree=sort(dictionary)

    while(len(tree)>1):
        a=tree.pop(0)
        b=tree[0]
        tree[0]=[[a[0],b[0]],a[1]+b[1]]
        tree=sort(tree)

    decode=breakdown(tree[0][0])
    encode={}
    for key, value in decode.items():
        encode.update({value:key})
    return [encode,decode]
