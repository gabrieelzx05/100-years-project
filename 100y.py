from ast import Continue
import time
import sys

print(f"Olá, gostaria de saber quantos anos faltam para você completar 100 anos? ")

resposta = input("Digite a resposta, por favor: ")

if resposta.lower() == "sim":
 print(f"Gostaria que nos apresentassemos, pode me chamar de Wall-e! como eu deveria te chamar? ")

else: 
 print(f"Obrigado pela participação! O programa será encerrado.")
 time.sleep(2)
 sys.exit()

nome = input("Digite seu nome: ") 
print(f"Adorei o seu nome, agora poderia me informar a sua idade por favor? ")
idade = int(input("Digite sua idade: "))

anos_restantes = 100 - idade

print(f"Muito obridado, {nome}. Faltam {anos_restantes} anos até você completar 100 anos! Se precisar de algo a mais é só falar, foi um prazer e volte sempre!!")