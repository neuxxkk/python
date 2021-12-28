from os import system
system('cls')
def media(*l):
    """
    l: tuple, ints
    x=l[0]+l[1]+l[2]...
    x/len(l)
    """
    x=0
    for i in l:
        if type(i)==tuple: 
            for o in i:
                x+=o
                l=i
        else:x+=i
    return x/len(l)
print(media((10,10,2,5,6,3)))