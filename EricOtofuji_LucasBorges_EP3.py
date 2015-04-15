# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:55:20 2015

@author: Eric & Lucas
"""

print("Bem-vindo ao controle de dieta! Manter uma vida saudável é muito importante, e vamos te ajudar a chegar em seus objetivos. Vamos lá?")
oal = open("alimentos.csv") #oal é o arquivo alimentos.csv aberto e apenas isso
alim = oal.readlines #alim é variável que contém as linhas de informação de alimentos.csv
#print(alim)
ous = open("usuario.csv") #ous é o arquivo usuario.csv aberto e apenas isso
datauser = ous.readline(2) #datauser são os dados básicos do usuário como nome, mas ainda não organizados.
