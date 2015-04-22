# -*- coding: utf-8 -*-
"""
Arquivo mestre do programa de controle de dieta
EP3 - Design de Software - 2015 - Insper, instituto de ensino e pesquisa
Devs: Eric Otofuji & Lucas Borges
"""
print("Bem-vindo ao controle de dieta! Manter uma vida saudável é muito importante, e vamos te ajudar a chegar em seus objetivos. Vamos lá?\n") #um texto de boas vindas fofélico
ous = open("usuario.csv","r", encoding="utf-8") #ous é o arquivo usuario.csv aberto e apenas isso - depois de aberto não vai servir para muita coisa, então não é algo a se preocupar muito.
leitura=open("usuario.csv","r", encoding="utf-8").readlines() # Abre o arquivo com os dados do usuário
ous.readline() #linejumper
datauser = ous.readline().split(",") #datauser são os dados básicos do usuário como nome, mas ainda não organizados. Esta linha também separa a linha em índices em uma lista separada por vírgulas. 
nome = datauser[0] #variável "nome" é o índice zero (primeira coluna) de usuario.csv. Em suma, é o nome do dito-cujo.
idade = int(datauser[1]) #variável "idade" éo índice 1 (segunda coluna) de usuario.csv. Em suma, é a idade do cidadão.
peso = int(datauser[2]) #variável "peso" é o índice 2 (terceira coluna) de usuario.csv. Em suma, é o peso da criatura.
sexo = datauser[3] #variável "sexo" é o índice 3 (quarta coluna) de usuario.csv. Em suma, é o sexo da pessoa.
altura = float(datauser[4]) #variável "altura" é o índice 4 (quinta coluna) de usuario.csv. Em suma, é a altura do indivíduo.
fator = datauser[5].upper() ##variável "fator" é o índice 5 (sexta coluna) de usuario.csv. Em suma, é o fator de atividade física (o quanto se exercita) do usuário.
ous.readline() #linejumper
row = ous.readlines() #lê todas as linhas do alimentos.csv daí pra baixo.
cal = 0 #variável com quantidade de caloria em kcal
prot = 0 #variável com quantidade de proteínas
carb = 0 #variável com a quantidade de carboidratos
gord = 0 #variável com a quantidade de gorduras
import csv #importa a biblioteca csv, que será muito útil para as funções que usaremos para criar os dicionários com o banco de dados das informações nutricionais usando somente três linhas.
import matplotlib.pyplot as plt
with open("alimentos.csv", mode="r") as calref: #aqui estamos abrindo alimentos.csv para extrairmos os valores em dicionário de calorias e para tanto criamos a variável calref (referência de calorias)
    reader=csv.reader(calref) #aqui usamos a função reader da biblioteca csv para ler o arquivo csv como csv e fazer o Python entender isso
    calref={rows[0]:rows[2] for rows in reader} #aqui criamos dicionário calref do csv lido usando a coluna [0] como chaves e a coluna [2] como valores, que é a coluna que tem valores de calorias que é o que queremos aqui.
with open("alimentos.csv", mode="r") as protref: #análogo às três linhas acima usando protref pois agora é a referência de proteínas
    reader=csv.reader(protref)
    protref={rows[0]:rows[3] for rows in reader}
with open("alimentos.csv", mode="r") as carbref: #análogo ao calref mas agora com carbref (referência de carboidratos).
    reader=csv.reader(carbref)
    carbref={rows[0]:rows[4] for rows in reader}
with open("alimentos.csv", mode="r") as gordref: #análogo ao calref mas agora com gordreg (referência de gorduras).
    reader=csv.reader(gordref)
    gordref={rows[0]:rows[5] for rows in reader}

def CalculaNívelbasal(peso,altura,idade): # Calcula a Taxa de Metabolismo Basal(TMB)                        
    """ 
    >>> round(CalculaNívelbasal(65,1.75,20),2) # Round seleciona quantas casas depois da virgula você quer exibir
    1685.36
    """    
    if sexo == "M": # No caso de sexo masculino
        TMB= 88.36+(13.4*peso)+(4.8*altura*100)-(5.7*idade)
    elif sexo == "F": # No caso de sexo feminino
        TMB= 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)    
    return TMB

def CalculaNecessidadeCal(): # Calcula a Necessidade calórica diária (kcal)    
    """ 
    >>> round(CalculaNecessidadeCal(),2) # Round seleciona quantas casas depois da virgula você quer exibir
    3120.86
    """ 
    if fator == "MÍNIMO":  # No caso de fator MÍNIMO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.2
    elif fator == "BAIXO":    # No caso de fator BAIXO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.375
    elif fator == "MÉDIO":    # No caso de fator MÉDIO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.55
    elif fator == "ALTO":    # No caso de fator ALTO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.725
    else:    # No caso de fator MUITO ALTO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.9        
    return TaxaCal  
print(CalculaNecessidadeCal())
    
def CalculaIMC(peso,altura): # Calcula o Índice de Massa Corporal (IMC)   
    """ 
    >>> round(CalculaIMC(50,1.5),2) # Round seleciona quantas casas depois da virgula você quer exibir
    22.22
    """        
    IMC= (peso)/(altura)**2  
    return IMC   

def TipoIMC(peso,altura): # Define qual é o seu tipo de IMC
    """ 
    >>> round(TipoIMC(80,1.8),2) # Round seleciona quantas casas depois da virgula você quer exibir
    Você está no peso ideal
    2
    """    
    if CalculaIMC(peso,altura)<18.5: # Caso esteja abaixo do peso
        print("Você está abaixo do peso")
        return 1
    elif 18.5<=CalculaIMC(peso,altura)<25: # Caso esteja no peso ideal
        print("Você está no peso ideal")
        return 2
    elif 25<=CalculaIMC(peso,altura)<30: # Caso esteja um pouco acima do peso
        print("Você está um pouco acima do peso")
        return 3
    else:
        print("Você está muito acima do peso") # Caso esteja muito acima do peso
        return 4
         
""" Dicionários com a quantidade de cada alimento ingeridos"""    
SemanaCalorias={}
SemanaProteinas={}
SemanaCarboidratos={}
SemanaGorduras={}

def usuariocarboidratoscsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        if data in SemanaCarboidratos:
            SemanaCarboidratos[data]+=float(carbref[comida])*gramas/100
        else:
            SemanaCarboidratos[data]=float(carbref[comida])*gramas/100
    return SemanaCarboidratos

def usuariocaloriascsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        if data in SemanaCalorias:
                SemanaCalorias[data]+= float(calref[comida])*gramas/100
        else:
                SemanaCalorias[data]=float(calref[comida])*gramas/100
    return SemanaCalorias

def usuarioproteinascsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        if data in SemanaProteinas:
                SemanaProteinas[data]+=float(protref[comida])*gramas/100
        else:
                SemanaProteinas[data]=float(protref[comida])*gramas/100  
    return SemanaProteinas

def usuariofatcsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        if data in SemanaGorduras:
                SemanaGorduras[data]+=float(gordref[comida])*gramas/100
        else:
                SemanaGorduras[data]=float(gordref[comida])*gramas/100  
    return SemanaGorduras 
    
#if __name__ =='__main__':	
    #import doctest
    #doctest.testmod(verbose=True)    

def graphcal(cal,datas):
    plt.plot(cal,datas)
    plt.title("Seu consumo calórico")
    plt.xlabel("Calorias ingeridas (kcal)")
    plt.ylabel("Dias")
    plt.show()
    
def graphprot(prot,datas):
    plt.plot(prot,datas)
    plt.title("Seu consumo de proteínas")
    plt.xlabel("Proteínas ingeridas")
    plt.ylabel("Dias")
    plt.show()
    
def graphcarb(carb,datas):
    plt.plot(carb,datas)
    plt.title("Seu consumo de carboidratos")
    plt.xlabel("Carboidratos ingeridos")
    plt.ylabel("Dias")
    plt.show()
    
def graphgord(gord,datas):
    plt.plot(gord,datas)
    plt.title("Seu consumo de gorduras")
    plt.xlabel("Gorduras ingeridas")
    plt.ylabel("Dias")
    plt.show()

usuariocaloriascsv()
plt.title("Consumo de Calorias\n Teste",color="b")
plt.bar(range(len(SemanaCalorias)), SemanaCalorias.values(), align='center')
plt.xticks(range(len(SemanaCalorias)), list(SemanaCalorias.keys()))
plt.show()

usuariocarboidratoscsv()
plt.title("Consumo de Carboidratos",color="black")
plt.bar(range(len(SemanaCarboidratos)), SemanaCarboidratos.values(), align='center',color="black")
plt.xticks(range(len(SemanaCarboidratos)), list(SemanaCarboidratos.keys()))
plt.show()

usuarioproteinascsv()
plt.title("Consumo de Proteínas (g)",color="red")
plt.bar(range(len(SemanaCarboidratos)), SemanaCarboidratos.values(), align='center',color="red")
plt.xticks(range(len(SemanaCarboidratos)), list(SemanaCarboidratos.keys()))
plt.show()

usuariofatcsv()
plt.title("Consumo de Gorduras (g)", color = "yellow")
plt.bar(range(len(SemanaGorduras)), SemanaGorduras.values(), align='center',color="yellow")
plt.xticks(range(len(SemanaGorduras)), list(SemanaGorduras.keys()))
plt.show()

print(usuariocarboidratoscsv())
print(usuariocaloriascsv())
print(usuarioproteinascsv())
print(usuariofatcsv())
#==============================================================================
# NivelBasal = CalculaNívelbasal(peso,altura,idade)
# NecessidadeCal = CalculaNecessidadeCal(fator)
# IMC = CalculaIMC(peso,altura)
# TIMC = TipoIMC(peso,altura)
#==============================================================================