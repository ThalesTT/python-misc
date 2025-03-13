# https://pt.wikipedia.org/wiki/Cadastro_de_Pessoas_Físicas

import sys

cpf: str = '073.328.190-74'
# cpf: str = "111.111.111-11"

lista_primeiro_digito = range(10, 1, -1)
lista_segundo_digito = range(11, 1, -1)

# Limpando o cpf de caracteres indesejados


def limpar_cpf(cpf: str):
    cpf_limpo = ""
    for char in cpf:
        if char in '.-':
            continue
        else:
            cpf_limpo += char
    return cpf_limpo


cpf_limpo = limpar_cpf(cpf)
sequenciais = cpf_limpo[0]*len(cpf_limpo)

# evitando o cpf de todos numeros iguais  ex:111.111.111-11
if sequenciais == cpf_limpo:
    print("Cpf inválido")
    sys.exit()

# separando os 9 números dos dígitos
*cpf_sem_digito, primeiro_digito, segundo_digito = cpf_limpo

# logica que defini o digito


def definir_digito(valor: int) -> int:
    valor = (valor*10) % 11
    digito = 0 if valor > 9 else valor
    return digito

# calculo dos números anteriores ao digito


def conta_digitos(cpf: str, lista_range: range) -> int:
    soma = 0
    for i, numero in enumerate(cpf_sem_digito):
        # print(numero, lista_range[i])
        soma += int(numero) * lista_range[i]

    digito = definir_digito(soma)
    return digito


# calculando primeiro digito
digito_um = conta_digitos(cpf_sem_digito, lista_primeiro_digito)

# adicionando primeiro digito ao cpf para calculo do segundo
cpf_um_digito = cpf_sem_digito.append(str(digito_um))

# calculando segundo digito
digito_dois = conta_digitos(cpf_um_digito, lista_segundo_digito)

# adicionando segundo digito ao cpf
cpf_calculado = cpf_sem_digito.append(str(digito_dois))
# unindo cpf em uma string
cpf_calculado = "".join(cpf_sem_digito)
# print(cpf_calculado)

# comparando o cpf calculado com o informado
if cpf_calculado == cpf_limpo:
    print("CPF válido")
else:
    print("CPF inválido")
