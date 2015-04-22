# -*- coding: utf-8 -*-
"""
Arquivo mestre do programa de controle de dieta
EP3 - Design de Software - 2015 - Insper, instituto de ensino e pesquisa
Devs: Eric Otofuji & Lucas Borges
"""
print("Bem-vindo ao controle de dieta! Manter uma vida saudável é muito importante, e vamos te ajudar a chegar em seus objetivos. Vamos lá?\n") #um texto de boas vindas fofélico
ous = open("usuario.csv","r", encoding="utf-8") #ous é o arquivo usuario.csv aberto e apenas isso - depois de aberto não vai servir para muita coisa, então não é algo a se preocupar muito.
ous.readline() #linejumper
datauser = ous.readline().split(",") #datauser são os dados básicos do usuário como nome, mas ainda não organizados. Esta linha também separa a linha em índices em uma lista separada por vírgulas. 
nome = datauser[0] #variável "nome" é o índice zero (primeira coluna) de usuario.csv. Em suma, é o nome do dito-cujo.
idade = int(datauser[1]) #variável "idade" éo índice 1 (segunda coluna) de usuario.csv. Em suma, é a idade do cidadão.
peso = int(datauser[2]) #variável "peso" é o índice 2 (terceira coluna) de usuario.csv. Em suma, é o peso da criatura.
sexo = datauser[3] #variável "sexo" é o índice 3 (quarta coluna) de usuario.csv. Em suma, é o sexo da pessoa.
altura = float(datauser[4]) #variável "altura" é o índice 4 (quinta coluna) de usuario.csv. Em suma, é a altura do indivíduo.
fator = datauser[5] ##variável "fator" é o índice 5 (sexta coluna) de usuario.csv. Em suma, é o fator de atividade física (o quanto se exercita) do usuário.
ous.readline() #linejumper
row = ous.readlines() #lê todas as linhas do alimentos.csv daí pra baixo.
cal = 0 #variável com quantidade de caloria em kcal
prot = 0 #variável com quantidade de proteínas
carb = 0 #variável com a quantidade de carboidratos
gord = 0 #variável com a quantidade de gorduras
import csv #importa a biblioteca csv, que será muito útil para as funções que usaremos para criar os dicionários com o banco de dados das informações nutricionais usando somente três linhas.
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
from FuncoesUsuario.py import * #importa módulos de funções do usuário
from graph.py import * #importa módulos de gráficos
