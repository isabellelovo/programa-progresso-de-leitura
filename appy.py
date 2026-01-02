print('-'*5, 'Sistema de Controle: Progresso de Leitura', '-'*5)
print('\nInforme:')

livro = input('*- Nome do Livro: ')
pags_total = int(input('*- Total de páginas: '))
pags_lidas = 0

while True:
    print('\n', '-'*3, 'Digite uma Opção', '-'*3)
    print('1 - Registrar leitura \n2 - Visualizar progresso \n3 - Sair do sistema')
    escolha = int(input('> '))

    print('\n', '-'*10, '\n')

    match escolha:
        case 1:
            entrada = int(input('Quantidade de páginas lidas: '))
            if (pags_lidas + entrada) <= pags_total:
                pags_lidas += entrada
            else:
                print('Erro! Número de páginas acima do limite.')

        case 2:
            percentual_lido = float((pags_lidas/pags_total) * 100)
            pags_restantes = pags_total - pags_lidas

            print(f'*- Você leu {percentual_lido:.2f}% de {livro}!')
            print(f'*- Faltam {pags_restantes} páginas!')

        case 3:
            break

print('Saindo...')
