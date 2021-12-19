from pre import cls
cls()

l=(
    int(input(f'number1: ')),
    int(input(f'number2: ')),
    int(input(f'number3: ')),
    int(input(f'number4: ')),
    int(input(f'number5: '))
)
p=[]
nines=0
three=False
for i in range(len(l)):
    if l[i]%2==0:p.append(l[i])

three=l.index(3)
nines=l.count(9)

print(f'Nine times: {nines}\nThree pos: {three}\nPairs: {p}')
