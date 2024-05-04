# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# Exercicios calcular a area de hexagono

import math
print("Programa que calcula area de hexagono")


lado = float(input("Digite o comprimento de um lado do hexagono: "))
area =  (3*math.sqrt(3)*lado ** 2)/2

print("Area de um hexagono é : ", area)