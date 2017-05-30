# For floating point divisions
from __future__ import division

# For math and numerical functions
import numpy as np
import math

# For plotting
import matplotlib.pyplot as plt


class Dice(object):
    '''Class for simulating N-sided dice'''

    def __init__(self, sides):
        '''Initialize die with N sides'''
        self.sides = sides
        self.value = 0

    def roll(self):
        '''Roll the die'''
        import random as rand
        self.value = rand.randint(1, self.sides)


class Comparator(object):
    '''Compare two dice with one another'''
    def __init__(self):
        self.attackResult  = 0
        self.defenceResult = 0

    def compareDice(self, attacker, defender):
        '''Compare two dice with one another'''

        # 0 = winner, -1 = loser, loses one unit
        if attacker.value > defender.value:
            self.attackResult  = 0
            self.defenceResult = -1
        elif attacker.value == defender.value:
            self.attackResult  = -1
            self.defenceResult = 0 
        elif attacker.value < defender.value:
            self.attackResult  = -1
            self.defenceResult = 0 
        else:
            print("Something went wrong")



class Battle(object):
    '''Class providing functions to simulate Risk battles'''
    def __init__(self):
        self.attackResult  = 0
        self.defenceResult = 0
        self.battleResult  = -1

    def rollRound(self, attackingArmies, defendingArmies):
        '''Roll one round of a battle, i.e. one throw of dice'''
        # print(["attacking Armies", attackingArmies])
        # attackingArmies = number of dice attacker has on country
        # attackUnits = number of dice that are rolled in this round
        if attackingArmies > 3:
            attackUnits = 3
        elif attackingArmies == 3:
            attackUnits = 2
        elif attackingArmies == 2:
            attackUnits = 1
        else:
            raise problemRollingRounds("Number of attacking units could not be determined")

        # defendingArmies = number of dice defender has on country
        # defenceUnits = number of dice that are rolled in this round
        if defendingArmies > 2:
            defenceUnits = 2
        else:
            defenceUnits = defendingArmies

        # print(["attack Units", attackUnits])
        
        # Create array with the number of dice each player has
        attackDice  = range(0, attackUnits)
        defenceDice = range(0, defenceUnits)

        # Roll those dice
        for i in xrange(0, attackUnits):
            attackDice[i] = Dice(6)
            attackDice[i].roll()
        for i in xrange(0, defenceUnits):
            defenceDice[i] = Dice(6)
            defenceDice[i].roll()

        # To determine the winner, sort the dice in descending order and compare
        attackDice.sort(key=lambda dice: dice.value, reverse=True)
        defenceDice.sort(key=lambda dice: dice.value, reverse=True)

        compare=Comparator()

        attackLosses  = 0
        defenceLosses = 0

        # Compare the dice and determine number of losses on each side
        if attackUnits >= defenceUnits:
            for i in xrange(0, defenceUnits):
                compare.compareDice(attackDice[i], defenceDice[i])
                attackLosses  = attackLosses  + compare.attackResult
                defenceLosses = defenceLosses + compare.defenceResult
        else:
            for i in xrange(0, attackUnits):
                compare.compareDice(attackDice[i], defenceDice[i])
                attackLosses  = attackLosses  + compare.attackResult
                defenceLosses = defenceLosses + compare.defenceResult

        # Return how much each player loses
        return [attackLosses, defenceLosses]
    
    def rollBattle(self, attackingArmies, defendingArmies):
        '''Roll multiple rounds for one battle - country 1 v country 2'''
        # print("initial setup")
        # print("attack")
        # print(attackingArmies)
        # print("defence")
        # print(defendingArmies)
        i = 1

        # Roll unit attacker has no units left, or defender loses
        while(attackingArmies > 1 and defendingArmies >0):
            # print(["------round", i])

            # Roll the round
            [attackLosses, defenceLosses] = \
                self.rollRound(attackingArmies, defendingArmies)
            attackingArmies = attackingArmies + attackLosses
            defendingArmies = defendingArmies + defenceLosses

            # print("attack")
            # print(attackingArmies)
            # print("defence")
            # print(defendingArmies)

            i=i+1
        return [attackingArmies, defendingArmies]


def fightWar(attackTroops, defenceTroops):
    '''Function to simulate attack of several countries in a row with one stack'''
    '''Input: attackTroops = Number of units attacker has on starting country'''
    '''       defenceTroops = array with number of units defender has on each country'''

    battleNumber = 0

    # Maximum number of battles to be fought = number of countries attacked
    totalBattles = len(defenceTroops)
    
    # print("battles to fight")
    # print(totalBattles)
    
    # Fight as long as attacker has troops left, and until last country is attacked
    while(attackTroops > 0 and battleNumber < totalBattles):
        # print("battle number--------------")
        # print(battleNumber)
    
        battle = Battle()
        battleOutcome = battle.rollBattle(attackTroops,
                defenceTroops[battleNumber])
    
        attackTroops = battleOutcome[0]
    
        if attackTroops > 1 and battleNumber == totalBattles-1:
            # print("attacker won with following remaining")
            attackTroops = attackTroops 
            # print(attackTroops)
            return  attackTroops
        elif attackTroops < 2:
            # print("defender won with following armies")
            # print(battleOutcome[1])
            return -battleOutcome[1]

        if attackTroops > 1 and battleNumber < totalBattles-1:
            attackTroops = attackTroops - 1
    
        battleNumber = battleNumber + 1


# Change this variable for the number of shots to be made
monteCarloTrials  = 1000

monteCarloResults = np.zeros(monteCarloTrials)

# Change this variable for the number of armies on your starting territory
attackingArmies = 15
# Change this array for the number of defending armies on enemy territories
defendingArmies = [1,10,1]


# Run the MC simulation
totalWins = 0
for i in xrange(0, monteCarloTrials):
    monteCarloResults[i] = fightWar(attackingArmies, defendingArmies)
    # print("---------------------trial----------------")
    # print(i)
    if monteCarloResults[i] > 0.:
        totalWins = totalWins + 1
    elif math.isnan(totalWins):
        # print("Error! Following variables")
        # print(monteCarloResults[i])
        break 

chanceOfWinning = totalWins / monteCarloTrials * 100

print("chance of winning in percent")
print(chanceOfWinning)


# Show all results, if you want
# for i in xrange(0, monteCarloTrials):
#     print(i, monteCarloResults[i])

# Compute mean number of remaining armies
print("mean")
print(np.mean(monteCarloResults))

# Plot results
#plt.hist(monteCarloResults)#, bins=10, normed=True)
#plt.title("Number of remaining attacking armies")
#plt.xlabel("Value")
#plt.ylabel("Frequency")
#plt.show()





