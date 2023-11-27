class Fighter:
    def __init__(self, fighter_name, health, damagePerAttack):
        self.name = fighter_name
        self.health = health
        self.damagePerAttack = damagePerAttack # кількість шкоди, яку бієць завдає під час атаки
        
    def is_alive(self):
        return self.health >= 0  
    
    def attack(self, opponent):
        opponent.health -= self.damagePerAttack

 
class Fight:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2    

    def get_winner(self):
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            self.fighter1.attack(self.fighter2)
            self.fighter2.attack(self.fighter1)
            if not self.fighter2.is_alive():
                return self.fighter1.name

            if not self.fighter1.is_alive():
                return self.fighter2.name
            
            if not self.fighter1.is_alive() and not self.fighter2.is_alive():
                return None
       
            
            
fighter1 = Fighter('боєць 1', 70, 40)
fighter2 = Fighter('боєць 2', 90, 50)


fight = Fight(fighter1, fighter2)
winner = fight.get_winner()

if winner is not None:
    print(f"{winner} переміг!")
else:
    print('Нічия')