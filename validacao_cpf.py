# Bibliotecas
import sys

# Cálculo CPF
# Seja um CPF 698.412.140-xy
# Dígito x:
# 1. Deve-se multiplicar os 9 primeiros dígitos por uma contagem regressiva que começa em 10
# 2. No exemplo acima: 6*10 9*9 8*8 4*7 1*6 2*5 1*4 4*3 0*2
# 3. Em seguida soma-se o resultado obtido no passo 2: 60 + 81 + 64 + 28 + 6 + 10 + 4 + 12 + 0 = 265
# 4. Multiplica-se o resultado do passo 3 por 10: 265*10 = 2650
# 5. Calcula-se o resto da divisão do resultado do passo 4 por 11: 2650 % 11 = 10
# 6. Se o resultado do passo 5 for maior que 9, x = 0
# 7. Se o resultado do passo 5 for menor ou igual a 9, x = resultado passo 5
# 8. No exemplo presente x = 0 porque o resultado do passo 5 foi igual a 10

# Dígito y:
# 1. Deve-se multiplicar os 10 primeiros dígitos por uma contagem regressiva que começa em 11
# 2. No exemplo acima: 6*11 9*10 8*9 4*8 1*7 2*6 1*5 4*4 0*3 0*2
# 3-7. Mesma lógica usada para calcular o dígito x

# Funções

# Função que remove os pontos e o traço do cpf
def limpar_cpf(cpf):
    cpf_limpo = cpf.replace(".","").replace("-","")
    return cpf_limpo

# Função para calcular os dois últimos digitos do CPF
def calcular_digito(cpf_limpo,num_digitos):
    if num_digitos == 9:
        i = 10
    elif num_digitos == 10:
        i = 11
    
    # Loop para calcular a soma das multiplicações
    soma_multiplicacoes = 0
    for valor in cpf_limpo:
        soma_multiplicacoes += int(valor)*i
        i -= 1
        if i < 2:
            break

    # Multiplicando o resultado anterior por 10
    soma_multiplicacoes_vezes10 = soma_multiplicacoes*10

    # Resto da divisão do resultado anterior por 11
    resto_divisao11 = soma_multiplicacoes_vezes10 % 11

    # Primeiro digito do CPF
    digito = 0 if resto_divisao11 > 9 else resto_divisao11

    return digito

# Início do software

# Solicitando o CPF do usuário
cpf = input("Informe o CPF: ")

# Limpando o CPF
cpf_limpo = limpar_cpf(cpf)
cpf_nao_valido = 11*cpf_limpo[0]
print(f'CPF informado: {cpf_limpo}')

# Verificando os digitos do CPF
if (len(cpf_limpo) == 11) and (cpf_limpo != cpf_nao_valido):
    
    try:
        # Calculando os dois últimos dígitos do CPF
        primeiro_digito = calcular_digito(cpf_limpo,9)
        segundo_digito = calcular_digito(cpf_limpo,10)

    except ValueError:
        print("O CPF deve conter apenas números ou estar no formato xxx.xxx.xxx-xx")
        sys.exit()
    
    # Transformando de inteiro para string
    primeiro_digito = str(primeiro_digito)
    segundo_digito = str(segundo_digito)

    # Validando CPF
    if (cpf_limpo[9] == primeiro_digito) and (cpf_limpo[10] == segundo_digito):
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO!")
    
elif cpf_limpo == cpf_nao_valido:
    print("O CPF não pode ser uma sequência de um único número.")

else:
    print("O CPF deve conter 11 digitos.")
