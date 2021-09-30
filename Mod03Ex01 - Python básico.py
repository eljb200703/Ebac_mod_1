#!/usr/bin/env python
# coding: utf-8

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[1]:


sexo = 'F'
beta_hcg = 5

# seu código vem abaixo desta linha
if sexo == 'M':
    print("indivíduo do sexo masculino")
elif sexo == 'F' and  beta_hcg >= 5:
    print("Positivo")
elif sexo == 'F' and  beta_hcg < 5:
    print("Negativo")    


# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[52]:


dic_renomeacao = {'name':'nome', 'age':'idade', 'income':'renda'}
dic_renomeacao['age']


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[106]:


N = 20
M = 3

#Seu código
if N % M == 0:   
    print(('O número %d é divisível por' % N) + (' %d' % M))
if N % M != 0:   
    print(('O número %d é não é divisível por' % N) + (' %d' % M))


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[7]:


N = 4

# seu código abaixo

primos = []

for x in range(1, N+1):
    if N % x == 0:
        primos.append(x)
    
if len(primos) == 2:
    print('O número %d é primo' % N)

else:
    print('O número %d não é primo' % N)    


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[1]:


N = 101

# seu código aqui

primos = []

for x in range(1, N+1):
    if N % x == 0:
        primos.append(x)
    
if len(primos) == 2:
    print('O número %d é primo' % N)

else:
    print('O número %d não é primo' % N)    


# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[31]:


imc_ideal = 19
imc_ideal

#Pelo que entendi, minha tarefa é encontrar a média entre os valores de imc mínimo e máximo. Se entendi errado então peço 
#que explique melhorque o devo fazer.


min = 18.5
max = 24.9

imc_ponto_medio = ((min+max)/2)
imc_ponto_medio


# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[35]:


altura = 1.70

# Seu código

peso_ideal = imc_ponto_medio * altura ** 2
print(f'O peso ideal para altura {altura:.2f} e IMC {imc_ponto_medio:.2f} é {peso_ideal:.2f}kg')


# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[59]:


lista_alturas = [1.95, 2.05, 1.70, 1.65]

lista_peso_ideal = []

# seu código


for alturas in lista_alturas:
    peso_ideal = imc_ponto_medio * alturas ** 2
    lista_peso_ideal.append(peso_ideal)
lista_peso_ideal


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[74]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]

imc = []

# seu código
altura = []
peso = []
for a in altura_peso:
    altura.append(a[0])
for b in altura_peso:
    peso.append(b[1])

#fiquei travado aqui na hora de calcular a altura com o peso.


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[9]:


altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

# seu código

altura_peso

