#Knight Name Generator - www.101computing.net/name-knight-generator
import random


# The purpose of this program is to generate a random choice
# for two players, their name, coat of arms, personality traits,
# and home details

def knightNameGenerator():
  #Initialise list of possible first names and nicknames
  firstnames = ["Lancelot","Charles","Henry","William","James","Richard","Edward"]
  nicknames = ["Brave","Horrific","Courageous","Terrific","Fair","Conqueror","Victorious","Glorious","Invicible"]
  
  #Randomely pick one first name and one nickname
  firstname = random.choice(firstnames)
  nickname =  random.choice(nicknames)
  
  #Use String concatenation to generate and return the full name
  return firstname + " The " + nickname 
# from this point onward is my code:
# define a function to generate coat of arms symbol for player:
def generateCoatOfArms():
    colours = ["Red", "Golden", "Blue", "Purple", "White", "Silver"]
    animals = ["Lion", "Dragon", "Unicorn", "Horse", "Tiger"]

    colour = random.choice(colours)
    colour2 = random.choice(colours)
    animal = random.choice(animals)

    return colour + " and " + colour2 + " " + animal

def generateFavWeapon():
  weapons = ["Iron Mace", "Goldlen Flail", "Silver Axe", "Wooden Shield", "Bow and Arrow", "Dagger",]
  FavWeapon = random.choice(weapons)

  return FavWeapon

def KnightPersonalityTraits():
  KnightPersonalityTraits = ["Loyal", "Combative", "Strong", "Fearless", "Worthy", "Mighty", "Courageous", "Curious", "Dangerous", "Greedy"]
  PersonaTrait1 = random.choice(KnightPersonalityTraits)
  PersonaTrait2 = random.choice(KnightPersonalityTraits)

  return PersonaTrait1 + " and " +  PersonaTrait2

def generateKnightHome():
  LotTrait = ["Haunted", "Hidden", "Barricaded", "Dusty", "Fortefied", "Spacious", "Dark", "Safe", "Warm"]
  Home = ["Cottage", "Castle", "Shack", "Lair", "Cave", "Tower", "Mansion"]

  KnightLotTrait = random.choice(LotTrait)
  KnightHome = random.choice(Home)
  
  return KnightLotTrait + " " + KnightHome

#Main code to test our function
player1 = knightNameGenerator()
print("Player 1: Your name is: " + player1)
player1COA = generateCoatOfArms()
print("Player 1: Your Coat of Arms is a " + player1COA)
player1Weapon = generateFavWeapon()
print("Player 1: Your chosen weapon is a " + player1Weapon)
PersonalityTypeP1 = KnightPersonalityTraits()
print("Player 1: You are " + PersonalityTypeP1)
KnightHome1 = generateKnightHome()
print("Player 1: You live in a " + KnightHome1)


player2 = knightNameGenerator()
print("Player 2: Your name is: " + player2)
player2COA = generateCoatOfArms()
print("Player 2: Your Coat of Arms is a " + player2COA)
PersonalityTypeP2 = KnightPersonalityTraits()
print("Player 2: You are " + PersonalityTypeP2)
KnightHome2 = generateKnightHome()
print("Player 2: You live in a " + KnightHome2)


