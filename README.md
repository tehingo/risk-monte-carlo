# risk-monte-carlo
Monte Carlo simulation for the popular boardgame RISK

## Introduction
This is a very simple Python script that aims to determine the probability of winning a sequence of battles in Risk. The script implements a Monte Carlo simulation.

## Usage
1. Make sure Python is installed on your computer. You also need to have numpy installed (http://www.numpy.org/)
2. Open the file Risk.py in any text editor
3. Edit a few variables: 
  1. Line 185 for the number of Monte Carlo runs you want to make. 1000 is typically enough
  2. Line 190 for the number of units on the country you attack from
  3. Line 192 for the number of units on each fo the territories you want to attack
4. Execute the script, e.g. by typing in a terminal "python Risk.py"
5. Make an informed decision for your next turn based on the output!

## Random acknowledgements
The script was inspired by the "RISK® Dice-Thrower and Probability Calculator". It essentially does the same as that script, but runs it repeatedly to come up with a probability of winning for a sequence of attacks.
http://recreationalmath.com/Risk/

My use case for this is to get better at risk, which I enjoy playing over at WarGear. Join the community, it's a great way to play Risk online!
http://www.wargear.net

## Is this cheating?
General consensus is: no!
http://www.wargear.net/forum/showthread/4672/Monte_Carlo_Analysis

The script cannot tell you what to do. It can only give you a better feeling for whether you should do an attack, or not.

## Has this script been validated?
Yes! 

I compared the output to this table, but feel free to verify it for yourself:
http://blog.markturansky.com/wp-content/uploads/2008/03/risk_chanceofwinning.png

## Disclaimer
This script was literally programmed in one evening, where I was messing around with classes and gave up toward the end. 
Since it worked, I didn't care to clean things up.

Take it or leave it!
