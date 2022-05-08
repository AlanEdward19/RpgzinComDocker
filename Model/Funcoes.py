from Model.Jogador import Player
import time
import os
import random


def Conversa (nome:str,mensagem:str):
    print(f"{nome}:{mensagem}")

def RandomInimigo():
    Inimigos = [
    Player("Bandido",22,4,100,0),
    Player("Ladrao Ardiloso",18,12,110,0),
    Player("Carlinhos Vigarista",22,24,200,0),
    Player("Valtinho da 2",222,70,100,0)
                ]
                

    return random.choice(Inimigos)

def SimulacaoCombate(Jogador:Player,Inimigo:Player):
    os.system('cls' if os.name == 'nt' else 'clear')
    i=1
    print(f"\nBatalha entre {Jogador.nome} e {Inimigo.nome} se iniciou!!")

    while Jogador.vida > 0 and Inimigo.vida>0:
        escolha=0
        print(f"\nRound: {i}\n")
        print(f"Turno do: {Jogador.nome}\n")
        escolha=int(input("O que Deseja Fazer?\n[1] Atacar\n[2] Usar Magia\n[3] Se Apresentar\n"))
        if escolha == 1:
            Jogador.Atacar(Inimigo)
        elif escolha == 2:
            Jogador.Magia(Inimigo)
        elif escolha == 3:
            Jogador.Apresentar()
        time.sleep(2.5)
        print(f"\nTurno do: {Inimigo.nome}\n")
        escolha=random.randint(1,2)
        if escolha == 1:
            Inimigo.Atacar(Jogador)
        elif escolha == 2:
            Inimigo.Apresentar()
        i+=1
    if Jogador.vida > 0:
        print(f"{Inimigo.nome} foi derrotado!!\nVitoria de {Jogador.nome} com {Jogador.vida} pontos de vida restante")
    else:
        print(f"{Jogador.nome} foi derrotado!!\nVitoria de {Inimigo.nome} com {Inimigo.vida} pontos de vida restante")

def CriadorPersonagem(Personagem: Player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t\t--Criador de Personagem--\n")

    nome=input("Como se chama?\n")
    idade=int(input("Quantos anos tem?\n"))

    if int(input("Escolha sua Arma:\n[1] Soco\n[2] Espada Longa\n")) == 1:
        dano=15
    else:
        dano=35

    armadura=int(input("Escolha sua Armadura:\n[1] Armadura Leve\n[2] Armadura Media\n[3] Armadura Pesada\n"))
    if armadura == 1:
        vida = 100+15
    elif armadura == 2:
        vida = 100+20
    else:
        vida = 100+25

    Personagem= Player(nome,idade,dano,vida,50)

    print(f"Ficha de {Personagem.nome}:\nVida: {Personagem.vida}\nIdade: {Personagem.idade} anos\nDano: {Personagem.dano}")

    return Personagem