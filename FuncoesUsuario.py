# -*- coding: utf-8 -*-
"""
Arquivo de módulos do programa
EP3 - Design de Software - 2015 - Insper, instituto de ensino e pesquisa
Devs: Eric Otofuji & Lucas Borges
"""


leitura=open("usuario.csv","r", encoding="utf-8").readlines() # Abre o arquivo com os dados do usuário

""" Dados do Usuário"""
datauser = leitura[1].split(",")
nome = datauser[0] # Lê e retorna o nome do Usuário
idade = int(datauser[1]) # Lê e retorna a idade(anos) do Usuário
peso = float(datauser[2]) # Lê e retorna o peso(kg) do Usuário
sexo = datauser[3].upper().strip() # Lê e retorna o sexo(M ou F) do Usuário
altura = float(datauser[4]) # Lê e retorna a altura(m) do Usuário
fator = datauser[5].upper().strip() # Lê e retorna o fator do Usuário

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

def CalculaNecessidadeCal(fator): # Calcula a Necessidade calórica diária (kcal)    
    """ 
    >>> round(CalculaNecessidadeCal(fator),2) # Round seleciona quantas casas depois da virgula você quer exibir
    2833.42
    """
    if fator == "MÍNIMO":  # No caso de fator MÍNIMO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.2
    if fator == "BAIXO":    # No caso de fator BAIXO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.375
    if fator == "MÉDIO":    # No caso de fator MÉDIO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.55
    if fator == "ALTO":    # No caso de fator ALTO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.725
    if fator == "MUITO ALTO":    # No caso de fator MUITO ALTO
        TaxaCal = CalculaNívelbasal(peso,altura,idade)*1.9        
    return TaxaCal 

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
SemanaGramas={}
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
        SemanaCarboidratos[data] = carbref[comida]*gramas
        for data in SemanaCarboidratos:
            if data in SemanaCarboidratos:
                SemanaCarboidratos[data]+=carbref[comida]*gramas
            else:
                 SemanaCarboidratos[data]+=carbref[comida]*gramas
    return SemanaCarboidratos

def usuariocaloriascsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        SemanaCalorias[data]=calref[comida]*gramas
        for data in SemanaCalorias:
            if data in SemanaCalorias:
                SemanaCalorias[data]+= calref[comida]*gramas
            else:
                SemanaCalorias[data]=calref[comida]*gramas
    return SemanaCalorias

def usuarioproteinascsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        SemanaProteinas[data]=protref[comida]*gramas
        for data in SemanaProteinas:
            if data in SemanaProteinas:
                SemanaProteinas[data]+=protref[comida]*gramas
            else:
                SemanaProteinas[data]=protref[comida]*gramas  
    return SemanaProteinas

def usuariofatcsv():
    for linha in leitura[3:]:
        datauser = linha.strip().split(',')
        gramas=float(datauser[2])
        comida=datauser[1]
        data=datauser[0]
        SemanaGorduras[data]=gordref[comida]*gramas
        for data in SemanaGorduras:
            if data in SemanaGorduras:
                SemanaGorduras[data]+=gordref[comida]*gramas
            else:
                SemanaGorduras[data]=gordref[comida]*gramas  
    return SemanaGorduras 

    
if __name__ =='__main__':	
    import doctest
    doctest.testmod(verbose=True)