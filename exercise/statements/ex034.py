from pre import cls
cls()

n=float(input('Payment: $'))

if n<=1250:
    a=n*0.15
    p=n+a
    print(f'Aumento: ${p:.2f}')
else:
    a=n*0.10
    p=n+a
    print(f'Aumento: ${p:.2f}')