from Model.Jogador import Player
from Model import Funcoes
import time
import os
import random

#Começo
def Comeco():
    print("Em uma bela noite, todos do reino estão comemorando em uma taverna!!\n")
    time.sleep(4)
    print("Derrepente a porta da taverna se abre e Alguem se aproxima\nEsta pessoa anda em direção ao taverneiro que lhe diz:\n")
    time.sleep(4)
    Funcoes.Conversa("Taverneiro","Voce..")
    time.sleep(4.5)
    Funcoes.Conversa("Taverneiro","Quem e voce?\n")
    time.sleep(3.5)

Jogador=Player("1",0,0,0,0)

Comeco()
Jogador=Funcoes.CriadorPersonagem(Jogador)

if input("Pronto para começar sua Jornada Aventureiro?\n[S/N]").upper() == "S":
     os.system('cls' if os.name == 'nt' else 'clear')
     Inimigo=Funcoes.RandomInimigo()
     Funcoes.SimulacaoCombate(Jogador,Inimigo)
else:
    Jogador=Funcoes.CriadorPersonagem(Jogador)