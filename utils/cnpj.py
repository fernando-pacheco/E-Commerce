def replace(x):
    x = x.replace('.', '')
    x = x.replace('/', '')
    x = x.replace('-', '')
    return x


def digito(novo_digito, i): 
    acum = 0
    for index in novo_digito:
        acum += i * int(index)
        i -= 1
        if i == 1:
            i = 9
    digit = 11 - (acum % 11)
    if digit > 9:
        digit = 0
        return digit
    return digit


def seq(valor_cnpj):
    sequencia = valor_cnpj[0] * len(valor_cnpj)
    if sequencia == valor_cnpj:
        return '01010101010101'
    return valor_cnpj


def valid(valor_cnpj):
    cnpj = replace(valor_cnpj)
    cnpj = seq(cnpj)
    n_cnpj = cnpj[:-2]
    d1 = digito(n_cnpj, 5)
    n_cnpj += str(d1)
    d2 = digito(n_cnpj, 6)
    n_cnpj += str(d2)
    return n_cnpj
