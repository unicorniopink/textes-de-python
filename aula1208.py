sexo= input('digite o sexo:')
feminino=0
masculino=0
while sexo != 'x':
    if sexo == 'feminino':
        feminino = feminino+1
    elif sexo == 'masculino':
        masculino = masculino+1
    else:
        print('numero invalido ')
    sexo=input('digite o sexo')
print('a quantidade de pessoas do sexo femininoé:',feminino)
print('a quantidade de pessoas do sexo masculino é',masculino)

x=int(input('digite o número:'))
x=int(input('digite o número:'))

p= +1
n= -1

for n in range(x):
   if p+1:
     p= +1
print('a quantidade de numeros positivos é',p)
if n-1:
     n=-1
print('a quantidade de numeros negativos é',n)
 class Cliente:
    def _init_(self, nome='', RG='', endereco='',bairro='',cidade='',telefone='',email='',ativo=False):
        self.nome = nome
        self.RG = RG
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.ativo=ativo
cliente=dados()
cliente.nome=input('digite o nome:')
cliente.RG=input('digite o RG:')
cliente.endereco=input('digite o endereço:')
cliente.bairro=input('digite o bairro:')
cliente.cidade=input('digite a cidade:')
cliente.telefone=input('digite o telefone:')
cliente.email=input('digite o email:')
