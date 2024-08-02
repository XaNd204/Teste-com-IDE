###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Um Lanche Antes da Aula
# Nome: Alexandre Fernandes de Souza
# RA: 201698
###################################################

# Leitura da entrada

T = int(input())
L1 = int(input())
L2 = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())

# Comparação entre as opções e impressão da saída

if (P1 + T + P2 > 45) and (P3 + T <= 45):
    print(False)
if (P3 + T > 45) and (P1 + T + P3 <= 45):
    print(True)
if (P1 + T + P2 <= 45) and (P3 + T <= 45) and (L1 + 12 == L2 + 6):
    print(True)
if (P1 + T + P2 <= 45) and (P3 + T <= 45) and (L1 + 12 > L2 + 6):
    print(False)
if (P1 + T + P2 <= 45) and (P3 + T <= 45) and (L1 + 12 < L2 + 6):
    print(True)
if (P1 + T + P2 > 45) and (P3 + T > 45) and (P3 + T < P1 + T + P2):
    print(False)
if (P1 + T + P2 > 45) and (P3 + T > 45) and (P3 + T > P1 + T + P2):
    print(True)
if (P1 + T + P2 > 45) and (P3 + T > 45) and (P1 + T + P2 == P3 + T):
    print(True)
if (P1 + T + P2 <= 45) and (P3 + T > 45):
    print(True)
