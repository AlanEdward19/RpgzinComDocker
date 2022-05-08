class Personagem:
    def __init__(self,nome, idade, dano,vida,mana):
        self.nome = nome
        self.idade = idade
        self.dano = dano
        self.vida = vida
        self.mana = mana

    def DiminuirVida(self,quantidade,atacante):
        if(self.vida > 0):
             self.vida-=quantidade
             print(f'{atacante} causou Dano de {quantidade} em {self.nome}!!\n{self.nome} Vida Atual: {self.vida}')
        else:
            print(f'{self.nome} Morreu!')

    def Apresentar(self):
        print(f'\nMe chamo {self.nome}')

class Player(Personagem):
    def __init__(self, nome, idade, dano, vida, mana):
        super().__init__(nome, idade, dano, vida, mana)

    def Atacar(self,Alvo:Personagem):
        Alvo.DiminuirVida(self.dano,self.nome)

    def Magia(self,Alvo:Personagem):
        if self.mana > 10:
            escolha=int(input("Qual Magia Deseja Usar?\n[1] Bola de Fogo\n[2] Raio de Gelo\n"))
            if escolha == 1:
                Alvo.DiminuirVida(10,self.nome)
                self.mana-=10
            if escolha == 2:
                Alvo.DiminuirVida(15,self.nome)
                self.mana-=15
                
            print(f"Mana Restante: {self.mana}\n")
        else:
            print("Sem Mana Suficiente!!\nAtacando com arma")
            self.Atacar(Alvo)