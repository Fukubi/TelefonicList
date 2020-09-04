import database
import utils


# contato = [('Teste', 'Rua 0', '9090909090', 'email@email.com')]
# novocontato(contato)
print('-'*60)
print(f'{"AGENDA TELEFÔNICA":^60}')
while True:
    print('-' * 60)
    try:
        opcao = int(input('''SELECIONE UMA DAS SEGUINTES OPÇÕES:
[1] - LISTAR CONTATOS
[2] - LISTAR CONTATOS PELO NOME
[3] - LISTAR CONTATOS PELO ID
[4] - NOVO CONTATO
[5] - ATUALIZAR CONTATO
[6] - REMOVER CONTATO
[7] - SAIR
> '''))
    except ValueError:
            print('A opção precisa ser um número inteiro!')
    else:
        if opcao == 7:
            break
        if opcao == 1:
            utils.formatarListagem(database.listarcontatos())
        if opcao == 2:
            nomeListar = (input('Digite o nome do contato: '), )
            utils.formatarListagem(database.listarcontatospelonome(nomeListar))
        if opcao == 3:
            try:
                id = (int(input('Digite o ID do contato: ')), )
            except ValueError:
                print('O ID precisa ser um número inteiro!')
            else:
                utils.formatarListagem(database.listarcontatospeloid(id))
        if opcao == 4:
            print('-' * 60)
            print(f'{"NOVO CONTATO":^60}')
            print('-' * 60)
            nome = input('Digite o nome do novo contato: ')
            while nome == '':
                print('É necessário informar um nome para o contato!')
                nome = input('Digite o nome do novo contato: ')
            numero = input('Digite o número do novo contato: ')
            while numero == '':
                print('É necessário informar um número para o contato!')
                numero = input('Digite o número do novo contato: ')
            endereco = input('Digite o endereco do novo contato: ')
            email = input('digite o email do novo contato: ')
            contato = [(nome, endereco, numero, email)]
            database.novocontato(contato)
            print('NOVO CONTATO ADICIONADO COM SUCESSO!')
        if opcao == 5:
            print('-' * 60)
            idContato = (int(input('Digite o ID do contato: ')), )
            contatoAlterar = database.listarcontatospeloid(idContato)
            print('-' * 60)
            utils.formatarListagem(contatoAlterar)
            print('-' * 60)
            try:
                escolhaAlterar = int(input('''SELECIONE O QUE VOCÊ DESEJA ALTERAR
[1] - NOME
[2] - TELEFONE
[3] - ENDEREÇO
[4] - EMAIL
[5] - CANCELAR
> '''))
            except ValueError:
                print('A escolha da alteração precisa ser um inteiro!')
            else:
                if escolhaAlterar == 5:
                    print('CANCELANDO A ALTERAÇÃO')
                if escolhaAlterar == 1:
                    print('-' * 60)
                    nomeAlterar = input('Digite o novo nome para o contato: ')
                    alterando = (nomeAlterar, contatoAlterar[2], contatoAlterar[3], contatoAlterar[4], idContato[0])
                    database.alterarcontato(alterando)
                if escolhaAlterar == 2:
                    print('-' * 60)
                    telefoneAlterar = input('Digite o nomo número de telefone do contato: ').strip()
                    alterando = (contatoAlterar[1], contatoAlterar[2], telefoneAlterar, contatoAlterar[4], idContato[0])
                    database.alterarcontato(alterando)
                if escolhaAlterar == 3:
                    print('-' * 60)
                    enderecoAlterar = input('Digite o novo endereço para o contato: ').strip()
                    alterando = (contatoAlterar[1], enderecoAlterar, contatoAlterar[3], contatoAlterar[4], idContato[0])
                    database.alterarcontato(alterando)
                if escolhaAlterar == 4:
                    print('-' * 60)
                    emailAlterar = input('Digite o novo email para o contato: ').strip()
                    alterando = (contatoAlterar[1], contatoAlterar[2], contatoAlterar[3], emailAlterar, idContato[0])
                    database.alterarcontato(alterando)
        if opcao == 6:
            idRemover = (int(input('Digite o ID do contato que deseja remover: ')), )
            database.removercontato(idRemover)
