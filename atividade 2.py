#Entreda de dados
ano1=int(input('digite o ano atual:'))
ano2=int(input('digite o ano de nascimento:'))
sub= ano1-ano2
if sub >= 16:
     print('você pode votar!')
elif sub < 16:
     print('você não pode votar!')
     