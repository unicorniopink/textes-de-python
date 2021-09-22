meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
#print(type(meu_dicionario))
#adicionando elementos no dicionario
meu_dicionario[5] = 'Cristiano'
print(meu_dicionario)

class Cliente:
    def __init__(self, nome='', rg='', endereco='', bairro='', cidade='', telefone='', email='', ativo=False):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.ativo = ativo

        def getNome(self):
            return self._nome

        def setNome(self,valor):
            self._nome = valor

        def getRg(self):
            return self._rg

        def setRg(self,valor):
            self._rg= valor

        def getEndereco(self):
            return self._endereco

        def setEndereco(self,valor):
            self._endereco = valor

        def getBairro(self):
            return self._bairro

        def setBairro(self,valor):
            self._bairro = valor

        def getCidade(self):
            return self._cidade

        def setCidade(self,valor):
            self._cidade = valor

        def getTelefone(self):
            return self._telefone

        def setTelefone(self,valor):
            self._telefone = valor

        def getEmail(self):
            return self._email

        def setEmail(self, valor):
            self._email = valor

        def __str__(self):
            return self.nome

        def desativarPessoa(self):
            self.ativo = False

listaDeClientes ={1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
nlista= 2

print('''   [1] Cadastrar 
   [2] Excluir 
   [3] Desativar uma conta
   [4] Mostra lista dos clientes
   [5] Finaliza operação''')


opcao= input('Qual opção desea realizar: ')
while opcao!= '5':
    if opcao=='4':
        for id, nome in listaDeClientes.items():
            print(str(id) + ": " + str(nome))
    elif opcao == '2':
        nexcluir= int(input('Digite o número que deseja excluir da lista: '))
        del listaDeClientes[nexcluir]

    elif opcao=='1':
        cliente =Cliente()
        cliente.setNome = input('Digite o nome: ')
        cliente.setRg = input('Digite o RG: ')
        cliente.setEndereco = input('Digite o endereço: ')
        cliente.setBairro = input('Digite o bairro: ')
        cliente.setCidade = input('Digite a cidade: ')
        cliente.setTelefone = input('Digite o telefone: ')
        cliente.setEmail = input('Digite o email: ')

        print('-----------------------')
        print('Nome: ', cliente.nome)
        print('RG: ', cliente.rg)
        print('endereço: ', cliente.endereco)
        print('Bairro: ', cliente.bairro)
        print('Cidade: ', cliente.cidade)
        print('Telefone: ', cliente.telefone)
        print('Email: ', cliente.email)
        print('-----------------------')

        nlista = nlista + 1
        listaDeClientes[nlista] = cliente.getNome

    elif opcao=='3':
        ldesativar= input('Digite o nome da conta que deseja desativar: ')
        print(ldesativar, ' Está desativado')


    opcao = input('Escolha uma opção: ')



