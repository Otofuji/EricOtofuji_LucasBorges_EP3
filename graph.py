# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:46:44 2015

@author: Eric
"""

import matplotlib.pyplot as plt

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

