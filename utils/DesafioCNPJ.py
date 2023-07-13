from utils.cnpj import valid, replace  
valor_cnpj = input('Insira o CNPJ para validação: ')
n_cnpj = valid(valor_cnpj)

if n_cnpj == replace(valor_cnpj):
    print(f'O CNPJ {valor_cnpj} é válido!')

else:
    print(f'O CNPJ {valor_cnpj} é inválido!')
