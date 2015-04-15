# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:55:20 2015

@author: Eric & Lucas
"""

print("Bem-vindo ao controle de dieta! Manter uma vida saudável é muito importante, e vamos te ajudar a chegar em seus objetivos. Vamos lá?")
oal = open("alimentos.csv","r", encoding="utf-8") #oal é o arquivo alimentos.csv aberto e apenas isso
alim = oal.readlines() #alim é variável que contém as linhas de informação de alimentos.csv
#print(alim)
ous = open("usuario.csv","r", encoding="utf-8") #ous é o arquivo usuario.csv aberto e apenas isso
ous.readline() #linejumper
datauser = ous.readline().split(",") #datauser são os dados básicos do usuário como nome, mas ainda não organizados.
nome = datauser[0]
idade = datauser[1]
peso = datauser[2]
sexo = datauser[3]
altura = datauser[4]
fator = datauser[5]
"""
As variáveis nas linhas 15-20 são exatamente o que seus nomes sugerem: os dados do usuário oriundos do arquivo usuario.csv.
"""
ous.readline() #linejumper
cal == 0
while not ous.readline()=="":
    ous.readline()
    
    for i in (numeros)