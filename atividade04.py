menu = {}
menu['1']="cadastrar."
menu['2']="Delete ."
menu['3']="listar"
menu['4']="sair"
  while True:
  options=menu.keys()
  options.sort()
    for entry in options:
      print entry, menu[entry]

    selecao=input("selecione:")
    if selecao =='1':
      print "cadastar"
    Elif selecao == '2':
      print "deletar"
Elif selection == '3':
    print "listar"
    Elif selection == '4':
      break
    else:
    print ('Opção desconhecida selecionada!')

class Cliente:
def __init__(self, nome='', cnpj_cpf='', codigo_endereco='', telefone='' ):
        self.nome = nome
        self.cnpj_cpf = cnpj_cpf
        self.codigo_endereco = codigo_endereco
        self.telefone = telefone


def getNome(self):
        return self._nome

def setNome(self, valor):
        self._nome = valor

def getEndereco(self):
        return self._codigo_endereco

def setEndereco(self, valor):
        self._codigo_endereco = valor

def getTelefone(self):
        return self._telefone

def setTelefone(self, valor):
        self._telefone = valor
        from conexao import criar_conexao, fechar_conexao

        def insere_usuario(con, matricula, nome, titulacao):
            cursor = con.cursor()
            sql = "INSERT INTO professor (matricula, nome,titulacao) values (%s, %s, %s)"
            valores = (matricula, nome, titulacao)
            cursor.execute(sql, valores)
            cursor.close()
            con.commit()

        def select_todos_usuarios(con):
            cursor = con.cursor()
            sql = "SELECT matricula,nome,titulacao FROM professor"
            cursor.execute(sql)
            cursor.close()

        def main():
            con = criar_conexao("localhost", "root", "", "controleacademico")
            insere_usuario(con, "23122323", "thaissa", "graduação")
            select_todos_usuarios(con)

            fechar_conexao(con)

            main()



