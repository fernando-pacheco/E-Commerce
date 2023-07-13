cpf = input('Insira o seu CPF para validação (sem pontos ou traços): ')
acum1 = 0
acum2 = 0
validacao = []
numeros_cpf = []

if not cpf.isnumeric():
    if len(cpf) == 11:
        print('Insira APENAS números!')
        exit()
    elif len(cpf) == 14:
        print('Insira o CPF sem pontos, ou traços!')
        exit()
    else:
        print('Isso não é um CPF!')
        exit()

else:
    for n in cpf:
        numeros_cpf.append(int(n))
        validacao.append(int(n))

    validacao.pop()
    validacao.pop()
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = numeros_cpf

    for p, r in enumerate(range(10, 1, -1)):
        produto = r * numeros_cpf[p]
        acum1 = acum1 + produto


    for p, r in enumerate(range(11, 1, -1)):
        produto = r * numeros_cpf[p]
        acum2 = acum2 + produto


v1 = 11 - (acum1 % 11)
v2 = 11 - (acum2 % 11)

if v1 > 9:
    validacao.append(0)
else:
    validacao.append(v1)

if v2 > 9:
    validacao.append(0)
else:
    validacao.append(v2)


if validacao == numeros_cpf:
    print()
    print(f'O CPF: {n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{n10}{n11} é válido!')
    if validacao[-3] == 0:
        print('E a origem esse CPF é do Rio Grande do Sul.')
    elif validacao[-3] == 1:
        print('E a origem esse CPF é da região de Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins.')
    elif validacao[-3] == 2:
        print('E a origem esse CPF é da região de Pará, Amazonas, Acre, Amapá, Rondônia e Roraima.')
    elif validacao[-3] == 3:
        print('E a origem esse CPF é da região de Ceará, Maranhão e Piauí.')
    elif validacao[-3] == 4:
        print('E a origem esse CPF é da região de Pernambuco, Rio Grande do Norte, Paraíba e Alagoas.')
    elif validacao[-3] == 5:
        print('E a origem esse CPF é da região de Bahia e Sergipe.')
    elif validacao[-3] == 6:
        print('E a origem esse CPF é da região de Minas Gerais.')
    elif validacao[-3] == 7:
        print('E a origem esse CPF é da região de Rio de Janeiro e Espírito Santo.')
    elif validacao[-3] == 8:
        print('E a origem esse CPF é da região de São Paulo.')
    else:
        print('E a origem desse CPF é da região de Paraná e Santa Catarina.')

else:
    print()
    print(f'O CPF: {n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{n10}{n11} NÃO é válido!')
