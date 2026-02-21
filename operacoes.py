def titulo(texto_titulo):
    """
    Docstring for titulo
    
    :param texto_titulo: Recebe o título e gera um pequeno menu centralizado.
    """
    a = len(texto_titulo)+10
    print('-'*a)
    print(texto_titulo.capitalize().center(a))
    print('-'*a)

def menu(menu_opcoes):
    """
    Docstring for menu
    
    :param menu_opcoes: Recebe uma lista de opções e transforma em menu retornando um input de
    """
    for c, dados in enumerate(menu_opcoes):
        print (f'{c+1} - {dados}')
    print('Digite a sua opção: ', end = '')
    return int(input())

def codigo(arq):
    #abertura e conversão dos dados do arquivo em lista
    from ast import literal_eval
    a = open(arq,'rt')
    temp = []
    for registros in a:
        dados = registros.strip()
        if not dados:
            continue
        else:
            registros = literal_eval(dados)
            temp.append(registros)
    a.close()
    #---------------------------------------------------
    c = 1
    codigos = []
    for registros in temp:
        if not registros:
            return (c)
        else:
            codigos.append(registros['Codigo'])
    while c in codigos:
        c+=1
    return (c)      
     
def cadastrar(arq):
    """
    Docstring for cadastrar
    
    :param arq: Abre o arquivo texto para possibilitar o cadastro da agenda
    """
    titulo('Cadastrar Registros')
    dados_cadastro = {}
    while True:
        a = open(arq,'at')
        dados_cadastro['Codigo'] = codigo(arq)
        dados_cadastro['Nome'] = input('Digite o Nome: ').lower().title().strip()
        dados_cadastro['Telefone'] = input('Digite o telefone: ')
        print(dados_cadastro)
        a.write(f'{dados_cadastro} \n')
        dados_cadastro.clear()
        opt = input ('Deseja cadastrar outro registro? [S/N] ')
        if opt in 'Nn':
            break
    a.close()
    return

def listar(arq):
    from ast import literal_eval
    titulo('Listagem Geral de Telefones')
    a = open(arq,'rt')
    for dados in a:
        dados = dados.strip()
        if not dados:
            continue
        else:
            registro = literal_eval(dados)
            print(f'Código: [{registro['Codigo']}] | Nome: {registro['Nome']} | Telefone: {registro['Telefone']}')
    a.close()
    print('Digite uma Tecla para Continuar')
    input()
    return

def pesquisar(arq):
    from ast import literal_eval
    titulo('Pesquisar Registros')
    a = open(arq,'rt')
    temp = []
    for registro in a:
        dados = registro.strip()
        if not dados:
            continue
        else:
            registro = literal_eval(dados)
            temp.append(registro)
    a.close()
    nome = input('Digite o nome: ').lower().title().strip()
    encontrado = False
    for dados in temp:
        if dados['Nome'] == nome:
            print('Identificado o seguinte registro com os dados digitados:')
            print(f'Código: [{dados['Codigo']}] | Nome: {dados['Nome']} | Telefone: {dados['Telefone']}')
            encontrado = True
    if not encontrado:
        print('Registro não encontrado')
    print('Digite uma Tecla para Continuar')
    input()

def editar(arq):
    from ast import literal_eval
    a = open(arq,'rt')
    temp = []
    for registro in a:
        dados = registro.strip()
        if not dados:
            continue
        else:
            registro = literal_eval(dados)
            temp.append(registro)
    a.close()
    codigo = int(input('Digite o código que deseja alterar: '))
    encontrado = False
    for dados in temp:
        if dados['Codigo'] == codigo:
                opt = input(f'Os dados alterados serão: {dados}, continuar? [S/N]: ')
                if opt in 'Ss':
                    dados['Nome'] = input('Digite o Novo Nome: ').capitalize().strip()
                    dados['Telefone'] = input('Digite o Novo telefone: ')
                    encontrado = True
                if opt in 'Nn':
                    print('Operação Cancelada pelo Usuário!')
                    print('Digite uma tecla para retornar ao menu.')
                    input()
                    return
    
    if encontrado:
        a = open(arq,'wt+')
        for dados in temp:
            a.write(f'{dados} \n')
        a.close()
        print('Dados Inseridos Corretamente!')
        input()
   
    if not encontrado:
        print('Registro não encontrado!')
        print('Digite uma tecla para retornar ao menu.')
        input()

def excluir(arq):
    from ast import literal_eval
    a = open(arq,'rt')
    temp = []
    for registros in a:
        dados = registros.strip()
        if not dados:
            continue
        else:
            dados = literal_eval(registros)
            temp.append(dados)
    a.close()
    codigo = int(input('Digite o código que deseja excluir: '))
    encontrado = False
    for dados in temp:
        if dados['Codigo'] == codigo:
            opt = input(f'Identificado o registro {dados} deseja excluir? [S/N]: ')
            if opt in 'Ss':
                temp.remove(dados)
                encontrado = True
            elif opt in 'Nn':
                print('Operação cancelada pelo usuário!')
                print('Digite uma tecla para retornar ao menu.')
                return
    
    if encontrado:
        a = open(arq,'wt')
        for registros in temp:
            a.write(f'{registros} \n')
        a.close()
        print('Registro Excluído com Sucesso!')
        print('Pressione uma tecla para retornar ao menu.')
        input()
        return
    else:
        print('Registro Não Encontrado')
        print('Pressione uma tecla para retornar ao menu.')
        input()
        return

def limpar_tudo(arq):
    opt = input('Tem certeza que deseja limpar todo o arquivo? [S/N]: ')
    if opt in 'Ss':
        a = open(arq,'wt+')
        a.close()
        print('Limpeza efetuada com sucesso :-D')
        print('Pressione uma tecla para retornar ao menu.')
        input()
    else:
        return()