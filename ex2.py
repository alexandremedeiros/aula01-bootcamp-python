'''
Programa que solicita:
1 - Nome do usuário
2 - Valor do salário mensal
3 - Valor do bônus que recebeu

O programa deve imprimir o bônus recebido
Fórmula do bônus: 1000 + salário * bônus
'''
BONUS = 1000

nome = input("Digite seu nome: ")
salario_recebido = float(input("Informe seu salário: "))
bonus_recebido =  float(input("Informe o bônus recebido: "))
valor_bonus = (BONUS + salario_recebido) * bonus_recebido

print(f"O usuário {nome} possui o bonus de {valor_bonus}")