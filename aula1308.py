


meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
#print(type(meu_dicionario))


meu_dicionario_2 = dict({1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'})
#print(type(meu_dicionario_2))

#get() Elementos pelo indice
print(meu_dicionario[2])
print(meu_dicionario.get(4))

#len() Tamanho do dicionario
print(len(meu_dicionario))

#adicionando elementos no dicionario
meu_dicionario[5] = 'Joaquina'
print(meu_dicionario)

meu_dicionario.update({6: 'Pedro'})
print(meu_dicionario)

#removendo elementos do dicionario
#pop()
meu_dicionario.pop(2)
del meu_dicionario[1]
print(meu_dicionario)

#visualizando dados
for id, nome in meu_dicionario.items():
    print(str(id) +": "+str(nome))

meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
#print(type(meu_dicionario))
print('1-cadastrar')
print('2-excluir')
print('3- mostrar status')
print('4- mostrar lista de clientes')
escolha= int(input('digite sua escolha:'))

if escolha==1:
    nome=input('digite o nome:')
    rg=float(input('digite o RG:'))
    endereco=input('digite o endereço:')
    bairro=input('digite o bairro:')
    cidade=input('digite a cidade:')
    telefone=int(input('digite o telefone:'))
    email=input('digite o email:')

class Cliente:
    def __init__(self, nome='', RG='', endereco='', bairro='', cidade='', telefone='', email='', ativo=False):
        self.nome = nome
        self.rg = RG
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.ativo = ativo

    def getNOME(self):
       return self.nome

    def setNOME(self,valor):
         self.nome=valor

    def getRG(self):
       return self.nome

    def setRG(self,valor):
       self.RG=valor

    def getendereco(self):
       return self.endereco

    def setendereco(self,valor):
         self.endereco=valor

    def getbairro(self):
       return self.bairro

    def setbairro(self,valor):
       self.bairro=valor

    def getcidade(self):
        return self.cidade
    def setcidade(self,valor):
        self.cidade=valor

    def gettelefone(self):
        return self.telefone

    def settelefone(self, valor):
        self.telefone = valor

    def getemail(self):
        return self.email

    def setemail(self, valor):
        self.email = valor

    def getativo(self):
        return self.ativo

    def setativo(self, valor):
        self.ativo = valor
    def _str_(self):
        return self.nome
    def desativarpessoa(self):
        self.ativo=False

cliente = Cliente()
cliente.nome = input('Informe o nome: ')
cliente.rg = input('Informe o RG: ')
cliente.endereco = input('Informe o endereço: ')
cliente.bairro = input('Informe o bairro: ')
cliente.cidade = input('Informe a cidade: ')
cliente.telefone = input('Informe o telefone: ')
cliente.email = input('Informe o email: ')

print('-----------------------')
print('Nome: ', cliente.nome)
print('RG: ', cliente.rg)
print('endereço: ', cliente.endereco)
print('Bairro: ', cliente.bairro)
print('Cidade: ', cliente.cidade)
print('Telefone: ', cliente.telefone)
print('Email: ', cliente.email)
print('-----------------------')
if escolha==2:
    def excluirCliente():
        print('Informe o ID do livro que você deseja excluir')
        idCliente = int(input())
        for i in range(len(Cliente)):
            if id == cliente[0]:
                del (cliente)
                break

if escolha==3:
    def

        contador = 100
        num = 100
        par = 0
        impar = 0
        while == 100:
            if (par % 2 == 0):
                par = par + 1
            else:
                impar = impar + 1
            print('par', par)
            print('impar,'
            impar)

            n1 = int(input('digite o numero:'))

            if (n1 % 2) == 0:
                print('o numero é par')
            else:
                print('o numero é impar')
                emprestimo = float(input('digite o valor do emprestimo:'))
                parcelas = float(input('digite o numero de parcelas:'))
                salario = float(input('digite o valor do salario:'))
                divisao = emprestimo / parcelas
                if divisao <= (30 / 100 * salario):
                    print('emprestimo aprovado')
                else:
                    print('emprestimo foi negado')
        lista = []
        lista1 = []
        n = 0
        while (n <= 4):
            nome = input('digite o nome:')
            cpf = input('digite o cpf:')
            lista.append(nome)
            lista1.append(cpf)
            n = n + 1
        print('A lista com nomes é:', lista)
        print('A lista com cpf é:', lista1)

        def soma(a, b):
            soma = a + b
            return soma

        def multiplicacao(a, b):
            multiplicacao = a * b
            return multiplicacao

        def divisao(a, b):

            divisao = a / b
            return divisao

        def subtracao(a, b):

            subtracao = a - b
            return subtracao

        n1 = float(input('digite o numero:'))
        n2 = float(input('digite o numero:'))
        print('o resultado é:', soma(n1, n2))
        print('o resultado é:', multiplicacao(n1, n2))
        print('o resultado é:', divisao(n1, n2))
        print('o resultado é:', subtracao(n1, n2))

        n1 = float(input('digite o numero:'))
        n2 = float(input('digite o numero:'))
        n3 = float(input('digite o numero:'))
        n4 = float(input('digite o numero:'))
        n5 = float(input('digite o numero:'))
        n6 = float(input('digite o numero:'))
        n7 = float(input('digite o numero:'))
        n8 = float(input('digite o numero:'))
        n9 = float(input('digite o numero:'))
        n10 = float(input('digite o numero:'))

        x = int(input('informe o limite:'))
        qtd_pov = 1
        qtd_neg = -1
        for n in range(x):
            if n >= 1:
                qtd_pov = qtd_pov + 1
        print('a quantidade de numeros positivos é', qtd_pov)
        if n < -1:
            qtd_neg = qtd_neg - 1
        print('a quantidade de numeros negativos é', qtd_neg)

        class pessoa:
            # construtor
            def _init_(self, nome='', sexo='', idade=0, ativo=False):
                self.nome = nome
                self.sexo = sexo
                self.idade = idade
                self.ativo = ativo

            def _str_(self):
                return self.nome

            def ativarpessoa(self):
                self.ativo = True

            def desativarpessoa(self):
                self.ativo = False

        # instaciando objetos

        pessoa = pessoa()
        pessoa.nome = input('digite o nome:')
        pessoa.sexo = input('digite o sexo:')
        pessoa.idade = input('digite idade:')
        pessoa.ativarpessoa()

        print('o nome da pessoa é', pessoa.nome)
        print('o sexo de {} é {}'.format(pessoa.nome, pessoa.sexo))
        print('a idade de {} é {}'.format(pessoa.nome, pessoa.idade))
        print('o status de é', pessoa.ativo)

        x = int(input('informe o limite:'))
        qtd_int = 1
        for n in range(x):
            if n > 1:
                qtd_int = qtd_int + 1
        print('a quantidade de numeros inteiros é', qtd_int)

        lista = []
        while True:
            n = int(input('Digite o número (9999 para encerrar): '))
            lista.append(n)
            if n == 9999:
                break

        print('O maior número da lista é: ', max(lista))

        def pn(n):
            if n > 0:
                print('Positivo')
            elif n == 0:
                print('Nulo')
            else:
                print('Negativo')

        print('POSITIVO OU NEGATIVO')
        n = int(input('digite um número: '))
        print('Este número é', end=' ')
        pn(n)

        def soma3(a, b, c):
            s = a + b + c
            return s

        print('SOMA DE TRÊS NÚMEROS')
        a = int(input('Primeiro número: '))
        b = int(input('Segundo número: '))
        c = int(input('Terceiro número: '))

        print('Soma = ', soma3(a, b, c))

        def somaImposto(taxaImposto, Custo):
            return (1 + taxaImposto / 100) * Custo

        t = float(input('Digite a taxa de imposto: '))
        c = float(input('Digite o custo: '))
        print('Valor com imposto:', somaImposto(t, c))

        def reverso(n):
            return str(n[::-1])

        n = str(input('Digite um número: ')).strip()
        print(f'Reverso: {reverso(n)}')

        class idade:
            def _init_(self, idade=0):
                self.idade = idade

            def _str_(self):
                return self.idade

        idade = int(input('digite a idade:'))
        if idade >= 18:
            print('você é maior de idade')
        else:
            print('você é menor de idade')
            return mysql.conector.connect(host=host, user=usuario, password=senha, database=banco)
        meu_dicionario = {1: 'Fabio', 2: 'Maria', 3: 'João', 4: 'José'}
        # print(type(meu_dicionario))
        # adicionando elementos no dicionario
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

                def setNome(self, valor):
                    self._nome = valor

                def getRg(self):
                    return self._rg

                def setRg(self, valor):
                    self._rg = valor

                def getEndereco(self):
                    return self._endereco

                def setEndereco(self, valor):
                    self._endereco = valor

                def getBairro(self):
                    return self._bairro

                def setBairro(self, valor):
                    self._bairro = valor

                def getCidade(self):
                    return self._cidade

                def setCidade(self, valor):
                    self._cidade = valor

                def getTelefone(self):
                    return self._telefone

                def setTelefone(self, valor):
                    self._telefone = valor

                def getEmail(self):
                    return self._email

                def setEmail(self, valor):
                    self._email = valor

                def __str__(self):
                    return self.nome

                def desativarPessoa(self):
                    self.ativo = False

        listaDeClientes = {1: 'Fabio', 2: 'Maria', 3: 'João', 4: 'José'}
        nlista = 2

        print('''   [1] Cadastrar 
           [2] Excluir 
           [3] Desativar uma conta
           [4] Mostra lista dos clientes
           [5] Finaliza operação''')

        opcao = input('Qual opção desea realizar: ')
        while opcao != '5':
            if opcao == '4':
                for id, nome in listaDeClientes.items():
                    print(str(id) + ": " + str(nome))
            elif opcao == '2':
                nexcluir = int(input('Digite o número que deseja excluir da lista: '))
                del listaDeClientes[nexcluir]

            elif opcao == '1':
                cliente = Cliente()
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

            elif opcao == '3':
                ldesativar = input('Digite o nome da conta que deseja desativar: ')
                print(ldesativar, ' Está desativado')

            opcao = input('Escolha uma opção: ')


