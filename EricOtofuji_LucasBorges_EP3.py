# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:55:20 2015

@author: Eric & Lucas
"""
print("Bem-vindo ao controle de dieta! Manter uma vida saudável é muito importante, e vamos te ajudar a chegar em seus objetivos. Vamos lá?\n")
#oal = open("alimentos.csv","r", encoding="utf-8") #oal é o arquivo alimentos.csv aberto e apenas isso
#alim = oal.readlines() #alim é variável que contém as linhas de informação de alimentos.csv
ous = open("usuario.csv","r", encoding="utf-8") #ous é o arquivo usuario.csv aberto e apenas isso
ous.readline() #linejumper
datauser = ous.readline().split(",") #datauser são os dados básicos do usuário como nome, mas ainda não organizados.
nome = datauser[0]
idade = int(datauser[1])
peso = int(datauser[2])
sexo = datauser[3]
altura = float(datauser[4])
"""
CÓDIGO INVÁLIDO USADO ANTERIORMENTE E DESCARTADO
CONTINUA AQUI PARA EVENTUAL CONSULTA
def fatorconvert(x):
    if x=="mínimo":
        return 0
    elif x=="baixo":
        return 1
    elif x=="médio":
        return 2
    elif x=="alto":
        return 3
    elif x=="muito ativo":
        return 4
fator = fatorconvert(datauser[5])
print(fator)
"""
fator = datauser[5]
"""
As variáveis nas linhas 15-20 são exatamente o que seus nomes sugerem: os dados do usuário oriundos do arquivo usuario.csv
"""
row = ous.readlines()
ous.readline() #linejumper
cal = 0 # quantidade de caloria

"""
CÓDIGO INVÁLIDO USADO ANTERIORMENTE E DESCARTADO
CONTINUA AQUI PARA EVENTUAL CONSULTA
datas1 = [] # Lista com as datas em que foram ingeridos os alimentos
datas = []
for i in range(1,len(row)):
    alimentos = row[i].split(",")    
    datas1.insert(0,alimentos[0]) # insere uma data na lista
    datas1.sort(key=lambda x: x.split("/")[::-1]) # Organiza as datas em ordem crescente
for i in datas1:
    if i not in datas:
       datas.insert(0,i)
       datas.sort(key=lambda x: x.split("/")[::-1]) # Organiza as datas em ordem crescente
x = 0
while x <= len(datas):
    for datas[x] in row:
        print(row[2])
    x+=1
"""

import csv
with open("alimentos.csv", mode="r") as calref:
    reader=csv.reader(calref)
    calref={rows[0]:rows[2] for rows in reader}
    """calref é dicionário com valores de referência do alimentos.csv"""
with open("alimentos.csv", mode="r") as protref:
    reader=csv.reader(protref)
    protref={rows[0]:rows[3] for rows in reader}
    """protref é o dicionário com valores de referência do alimentos.csv"""
with open("alimentos.csv", mode="r") as carbref:
    reader=csv.reader(carbref)
    carbref={rows[0]:rows[4] for rows in reader}
    """carbref é o dicionário com os valores de referência do alimentos.csv"""
with open("alimentos.csv", mode="r") as gordref:
    reader=csv.reader(gordref)
    gordref={rows[0]:rows[5] for rows in reader}
    """gordref é o dicionário com com os valores de referência do alimentos.csv"""
with open("alimentos.csv", mode="r") as quant:
    reader=csv.reader(quant)
    quant={rows[0]:rows[1] for rows in reader}
    """quant é o dicionário com as quantidades em gramas dos alimentos em alimentos.csv"""
calq={x:float(calref[x])/float(quant[x]) for x in calref}

print(calq["ACELGA"])