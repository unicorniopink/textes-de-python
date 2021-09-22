def subtracao(a,b):
    subtracao=a-b
    return subtracao
n1=float(input('digite o numero:'))
n2=float(input('digite o numero:'))
n3=float(input('digite o numero:'))
n4=float(input('digite o numero:'))
n5=float(input('digite o numero:'))
n6=float(input('digite o numero:'))
n7=float(input('digite o numero:'))
n8=float(input('digite o numero:'))
n9=float(input('digite o numero:'))
n10=float(input('digite o numero:'))
print('o resultado é:',subtracao,n1/2)
print('o resultado é:',subtracao,n2/2)
print('o resultado é:',subtracao,n3/2)
print('o resultado é:',subtracao,n4/2)
print('o resultado é:',subtracao,n5/2)
print('o resultado é:',subtracao,n6/2)
print('o resultado é:',subtracao,n7/2)
print('o resultado é:',subtracao,n8/2)
print('o resultado é:',subtracao,n9/2)
print('o resultado é:',subtracao,n10/2)



soma=0
for c in range(1,501,2):
    if c % 3 == 0:
     soma= soma + c
print('a soma de todos os número é {}'.format(soma))




n=int(input('digite um número:'))
c=n
f=1
print('calculando {}!  '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c>1 else'=',end='')
    f= f * c
    c-=1
print(' {} '.format(f))

maior= n1
n1 = 0
cont = 0
while n1 != 9999:
    n1 = int(input('digite um número: [digite 9999 para parar] '))
    if n1 !=9999:
     cont =+1
print('o valor dos números citados são: {}'.format(cont))