from pre import cls
cls()

n=input('Full name: ')

spaces=n.count(' ')
length=len(n)-spaces
upper=n.upper()
lower=n.lower()
f=n.split()[0]
flen=len(f)
name=n.title()

print(f'{name}:')
print(f'Length: {length}')
print(f'In upper case: {upper}')
print(f'In lower case: {lower}')
print(f'First name {f.title()} length: {flen}')