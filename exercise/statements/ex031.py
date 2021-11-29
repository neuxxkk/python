from pre import cls 
cls()

n=float(input('Distance: '))

p=n*0.45 if n>200 else n*0.50    
print(f'Tickets are ${p:.2f}')