from Turn-taking import turn_taking
from Dice_throw import dice_throw

def startFight(fighter, target):
    list_of_turn = []
    list_of_turn.append(turn_taking(fighter, target))

    fighter_throw = fighter.attack
    target_throw = target.attack

    fighter_dice = dice_throw(fighter_throw)
    target_dice = dice_throw(target_throw)

    for i in list_of_turn:
        if [i] == "mob":
        [i].fighter_dice




#Attack:
#Göra: Spelare/Monster ska kunna attackera motpart, vid träff göra skada
#Hur: Funktion som tar emot attackerare och mål. Returnera träff/miss.
#Drar av health vid träff.
#Om monster dör, tar bort från rumslista och turordningslista.
#Riddare blockar alltid första attacken vid träff mot den i varje strid.
#Tjuv gör dubbel skada 25% av tiden