"""
Docstring for Agenda.main

Projeto simples desenvolvido em Python objetivo de atualizar um sistema antigo desenvolvido em PHP. O foco é o aprendizado no trabalho com arquivo, 
controle de fluxo e organização de código, sem uso de banco de dados ou programação orientada a objetos.Este projeto faz parte de um processo de consolidação de fundamentos antes do estudo de Python com salvamento em arquivo.

O projeto visa atualizar para o python um projeto antigo de agenda telefônica chamado "Agenda.php".
"""

  
#Programa Principal

from operacoes import *

arq = ('dados.txt')
open(arq,'a').close()

while True:
    titulo('Menu Principal')
    opcao = menu(['Cadastrar','Listar Todos','Pesquisar','Editar','Excluir','Excluir Tudo','Sair'])
    if opcao == 1:
        cadastrar(arq)
    elif opcao == 2:
        listar(arq)
    elif opcao == 3:
        pesquisar(arq)
    elif opcao == 4:
        editar(arq)
    elif opcao == 5:
        excluir(arq)
    elif opcao == 6:
        limpar_tudo(arq)
    elif opcao == 7:
        print('Saindo do Programa!')
        break