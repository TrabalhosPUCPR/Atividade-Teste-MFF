#1) Escreva um Algoritmo que imprima todos os números inteiros de 0 a 50. 
#2) Escreva um Algoritmo que imprima todos os números inteiros de 100 a 1 (em ordem decrescente). 
#3) Escreva um Algoritmo que imprima todos os números inteiros de 100 a 200. 
#4) Escreva um Algoritmo que imprima os 100 primeiros números ímpares.
#5) Escreva um Algoritmo que receba dez números do usuário e imprima a metade de cada número. 
#6) Escreva um Algoritmo que imprima os número de 1 à 100, menos os múltiplos de 5.
#7) Escreva um algoritmo que leia e imprima 10 números fornecidos pelo usuário. No entanto, se o usuário entrar com o número 6, 
#interrompa o processo e Finalize a execução.
#8) Criar um Algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto 
#e seu somatório. Suponha que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor é menor que o 
#segundo, teste essa condição.

import numpy as np

escolha = int(input("Escolha a atividade (1-8):"))
if(escolha>8 or escolha<1):
    exit("Atividade não existe")
else:
    if(escolha==1):
        numeroum = np.arange(0, 51, 1)
        for x in numeroum:
            print(x)

    if(escolha==2):
        numeroum = np.arange(1, 101, 1)
        numeroum = np.flip(numeroum)
        for x in numeroum:
            print(x)

    if(escolha==3):
        numeroum = np.arange(100, 201, 1)
        for x in numeroum:
            print(x)

    if(escolha==4):
        numeroum = np.arange(0, 101, 1)
        for x in numeroum:
            if((x%2)!= 0): #se dividir por 2 não restar zero, printa X
                print(x)

    if(escolha==5):
        contador = 0
        numeros = 0
        while contador < 10:
            teste = int(input("Digite um numero diferente de zero: "))
            if (teste == 0):
                print("ERRO!!! Numero é igual a zero")
            else:   
                teste = teste / 2 
                numeros = np.append(numeros, teste) #coloca o numero digitado, dividido pela metade no vetor numeros
                contador += 1
        numeros = np.delete(numeros, [0]) #eu não sabia como declarar um array, então o primeiro termo era igual a 0
        print("A metade dos numeros digitados é, respectivamente:",numeros)
            
    if(escolha==6):
        numeroum = np.arange(0, 101, 1)
        for x in numeroum:
            if((x%5)!= 0):
                print(x)

    if(escolha==7):
        contador = 0
        numeros = 0
        while contador < 10:
            teste = int(input("Digite um numero inteiro, caso 6, o programa parará: "))
            if (teste == 6):
                print("loop encerrado")
                exit
            else:    
                numeros = np.append(numeros, teste)
                contador += 1
        numeros = np.delete(numeros, [0])
        print("Os números digitados são, respectivamente:",numeros)

    if(escolha==8):
        numerosoma = 0
        numeroum = int(input("digite o inicio do intervalo: "))
        numerodois = int(input("digite o final do intervalo: "))
        while(numeroum > numerodois):
            numeroum = int(input("digite o inicio do intervalo corretamente: "))
            numerodois = int(input("digite o final do intervalo corretamente: "))
        numeros = np.arange(numeroum, numerodois, 1)
        for x in numeros:
            if(x%2 == 0):
                print(x)
                numerosoma += x
        print("A soma final ficou",numerosoma)
    exit()
#'''