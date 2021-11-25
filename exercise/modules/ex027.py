from pre import cls
cls()

n=input('Name: ').title()

f=n.split()[0]
l=n.split()[len(n.split())-1]

print(n)
print(f.title())
print(l.title())


