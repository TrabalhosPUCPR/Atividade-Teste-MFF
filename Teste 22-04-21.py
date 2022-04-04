esc = int(input('Digite o numero da questao '))
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

"""

QUESTAO 1

Uma determinada colônia de bactérias dobra sua população a cada 15h. 
Observando colônias como esta os cientistas levantaram a formula indicada neste enunciado como sendo modelo desta colônia. 
Nesta formula t representa o número de horas que se passaram desde que o experimento começou. 
Considerando que a colônia sempre começa com apenas 100 bactérias quantas horas são necessárias para que a colônia tenha aproximadamente 300 bactérias? 
Marque a alternativa correta. *

"""
if esc == 1:

    # P = 100*2**(tempo/15)
    #300/100 = sqrt(2**t)
    #(300/100)**15= 2**t
    #log2((300/100)**15) = t

    tempo = np.log2((300/100)**15)

    print(tempo)
    print('alternativa 2')

"""

QUESTAO 2

A medida da acidez de um líquido é chamada de pH deste líquido. 
Esta medida é baseada na quantidade de íons de hidrogênio (H+) que existem neste líquido específico. 
A formula para encontrar o pH de um líquido é apresentada neste enunciado e utiliza um logaritmo em base 10. 
Nesta equação, H representa a concentração de íons de hidrogênio e é medido em moles por litro (mol/L). 
Líquidos com pH baixo são mais ácidos que os líquidos com pH alto. 
A água é neutra e seu pH é 7. Se o suco de limão tem um pH = 1,7 qual a concentração de íons de hidrogênio (em mol/L)? 
Considere eventuais arredondamentos até a segunda casa decimal. *

"""

if esc == 2:
    #ph = -log H
    #10**-ph = H

    hidro = 10**(-1.7)

    print(hidro)
    print('alternativa 4')

"""

QUESTAO 3 

Para o cálculo do limite apresentado na equação a seguir, quando usamos a biblioteca sympy, 
importada como sp, com a linguagem de programação Python, 
precisamos utilizar um comando específico. Entre as opções a seguir. 
Indique aquela que contém o comando correto para este cálculo. *

"""

if esc == 3:
    x = sp.Symbol('x')

    print(sp.limit(((1+(1/x))**(3*x)),x , sp.oo))
    print('alternativa 1')

"""

QUESTAO 4

Considerando a equação apresentada neste enunciado, o uso da biblioteca Sympy e da linguagem Python. 
Podemos afirmar que: *

"""

if esc == 4:
    #X->0lim(1+2x)**1/x
    print('QUESTAO foi anuladada, alternativa: este limite tende a 1')

"""

QUESTAO 5

Considerando a equação apresentada nesta questão, 
o uso da linguagem de programação Python, as bibliotecas Numpy e Matplotlib. 
Qual das opções a seguir representa o gráfico desta função de forma correta? 
Marque a alternativa correta. *

"""

if esc == 5:
    x = np.arange(-3, -1, 0.1)

    def Funcao():
        return (x + 2)/(x + 3)

    plt.grid(color='gray', linestyle='-.', linewidth=0.5)

    plt.xlabel('y')
    plt.ylabel('x')

    plt.plot(x, Funcao())
    plt.show()
    print('opcao 1')
    
"""

QUESTAO 6

Usando o Python, Calcule o limite da função apresentada neste enunciado e, 
marque a resposta correta entre as opções a seguir: *

"""

if esc == 6:
    x = sp.Symbol('x')

    funcao = (x**3)/((x+1)**2)
    lim = sp.limit(funcao, x, 1)
    sp.plot(funcao, line_color="red")
    print('Tende a menos infinito, alternativa 4')

