from pre import cls
cls()

def f(*n,s=0):
    data={}
    data['total']=len(n)
    data['maior']=max(n)
    data['menor']=min(n)
    data['média']=sum(n)/len(n)
    if s:data['status']='RUIM' if sum(n)/len(n)<60 else 'BOM'
    return data

print(f(1,5,6,2,3)) 