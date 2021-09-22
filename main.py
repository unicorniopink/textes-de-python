from conexao import criar_conexao,fechar_conexao

def inserir(con,codigo,nome,codigo_endereco,cnpj_cpf,tipo_cliente,telefone):
    cursor = con.cursor()
    sql = "INSERT INTO Profissao (codigo,nome,codigo_endereco,cnpj_cpf,tipo_cliente,telefone) values (%s,%s,%s,%s,%s,%s)"
    valores = (codigo,nome,codigo_endereco,cnpj_cpf,tipo_cliente,telefone)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def deletar(con,codigo):
    cursor = con.cursor()
    sql = "Delete from clientte where codigo = {}".format(codigo)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar(con):
    cursor = con.cursor()
    sql = "Select * from codigo"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
     print(valores_lidos)
         for linha in valores_lidos:
     print("Nome: ",linha[0])
     print("Telefone: ",linha[1])
    cursor.close()

def main():
    con = criar_conexao("127.0.0.1", "root", "", "livraria")
    deletar(con,codigo)
    listar(con)
    fechar_conexao(con)

    main()

listaDeClientes = {1:''}
nlista=0
listadeCompra= {1:''}
nlista1=0
nlista1=nlista1 +1
listadaeditora={1:''}
nlista2=0
listadeEndereco={1:''}
nlista3=0
listadeLivro={1:''}
nlista4=0



print('''    [1] Cliente
    [2] Compra
    [3] Editora
    [4] Endereço
    [5] Livro
    [6] Deletar
    [7] listar
    [8] Sair
    ''')

opcao = input('Escolha uma opção: ')

while opcao != 0:
   if opcao == "1":
    codigo = input("Digite o codigo: ")
    nome = input("Digite seu nome: ")
    codigo_endereco = input("Digite o codigo endereço: ")
    cnpj_cpf = input("Digite o cnpj ou cpf: ")
    tipo_cliente = input("Digite o tipo de cliente: ")
    telefone = input("Digite o telefone: ")
    nlista = nlista + 1
    listaDeClientes[nlista] = listaDeClientes
    break


   if opcao=='2':
    codigo= input('Digite o codigo:')
    isbn=input('Digite o isbn:')
    data_compra=input('Digite a data da compra:')
    nlista1=nlista1 +1
    listadeCompra[nlista1] = listadeCompra
    break

   if opcao=='3':
    codigo= input('Digite o codigo:')
    nome_gerente= input('Digite o nome do gerente:')
    codigo_endereco= input('Digite o endereço:')
    telefone_editora= input('Digite o telefone da editora:')
    nlista2 = nlista2 + 1
    listadaeditora[nlista2] = listadaeditora
    break

   if opcao=='4':
    codigo= input('Digite o codigo:')
    cep= input('Digite o endereço:')
    complemento= input('Digite o complemento:')
    bairro= input('Digite o bairro:')
    numero= input('Digite o numero:')
    cidade=input('Digite a cidade:')
    nlista3= nlista3 + 1
    listadeEndereco[nlista3] = listadeEndereco
    break

   if opcao=='5':
     isbn= input('Digite o isbn:')
     autor= input('Digite o autor:')
     assunto= input('Digite o assunto:')
     qtd_estoque= input('Digite a quantidade de estoque:')
     codigo_editora= input('Digite o código da editora:')
     nlista4 = nlista4+1
     listadeLivro[nlista4]= listadeLivro
     break

if opcao=='6':
    print= input('Qual lista deseja excluir: listaDeClientes[1], listadeCompra[2] ,listadeEndereco[3], listadeLivro[4]')
if print=='1':
   print=input('Digite o numero da lista que que excluir:')
del listaDeClientes[print]
if print=='2':
   print=input('Digite o numero da lista que que excluir:')
del listadeCompra[print]
if print=='3':
   print=input('Digite o numero da lista que que excluir:')
del listadeEndereco[print]
if print=='4':
   print=input('Digite o numero da lista que que excluir:')
del listadeLivro[print]

if opcao=='7':
    print = input('Listar:')
if print== '1':
    print('ListaDeClientes',listaDeClientes)
if print=='2':
    print('ListadeCompra',listadeCompra)
if print=='3':
    print('Listadaeditora',listadaeditora)
if print=='4':
    print('ListadeEndereco',listadeEndereco)
if print=='5':
   print('ListadeLivro',listadeLivro)
    break

if opcao=='8':
    print('opção finalizada')
     break

    print= input('Escolha uma opção: ')
#Teste de função
import unittest


def fun(x):
   return x+1

class mytest(unittest.TestCase):
   def test(self):
       self.assertEqual(fun(3),4)

if __name__== '__main__':
    unittest.main()







