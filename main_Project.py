import random

#Card class, has value attribute and suit attribute
class Card():
    def __init__(self, val, suit):
        self.__value = val
        self.__suit = suit
    
    def getVal(self):
        return self.__value
    
    def getSuit(self):
        return self.__suit
    
    #If value is one it is an ace, 11 is jack, 12 is queen, 13 is king, just returns string holding name of card
    def __str__(self):
        tempVal = str(self.getVal())
        if tempVal == "1":
            tempVal = "Ace"
        elif tempVal == "11":
            tempVal = "Jack"
        elif tempVal == "12":
            tempVal = "Queen"
        elif tempVal == "13":
            tempVal = "King"
        tempStr = tempVal + " of " + self.getSuit()
        return tempStr

#Array for master deck, has all cards in order
#Goes ace of clubs, 2 of clubs, 3 of clubs,.., ace of hearts, 2 of hearts, 3 of hearts, etc.
defaultDeck = []
for i in range(0, 4):
    tempSuit = ""
    if i == 0:
        tempSuit = "Clubs"
    elif i == 1:
        tempSuit = "Hearts"
    elif i == 2:
        tempSuit = "Spades"
    else:
        tempSuit = "Diamonds"
    for j in range(1, 14):
        tempCard = Card(j, tempSuit)
        defaultDeck.append(tempCard)

#Shoe is an array holding 8 default decks that have been shuffled and appended to shoe array, entire deck is then shuffled
class Shoe():
    def __init__(self):
        self.__cards = []
        for num in range(0, 8):
            tempDeck = defaultDeck
            random.shuffle(tempDeck)
            self.__cards = self.__cards + tempDeck
        random.shuffle(self.__cards)
    
    #returns card value at the end of the deck
    def popShoe(self):
        return self.__cards.pop()

class Player():
    #Drop flag for dropping for 3 zero bets, zero counter for counting bets of zero and initial balance is random
    #number between 500 and 5000, reset function explained below
    def __init__(self):
        self.__dropFlag = False
        self.__zeroCounter = 0
        self.reset()
        self.__balance = random.randint(500, 5000)
    
    #Sets player cards to empty array, score set to zero, flags for stand bust and blackJack set to false, current bet reset
    def reset(self):
        self.__playerCards = []
        self.__score = 0
        self.__standFlag = False
        self.__bustFlag = False
        self.__blackJackFlag = False
        self.__currentBet = 0
    
    #When adding a card, the round is important as to determine what ace value is assumed to be during first round
    def addCard(self, newCard, round):
        self.__playerCards.append(newCard)
        #If round is 2 and above player chooses what ace value is
        if(round > 1):
            if(newCard.getVal() == 1):
                #Simple user input validation
                validInput = False
                while(validInput == False):
                    choice = input("Enter 1 or 11 for value of the ace card: ")
                    if(choice.isnumeric() == True):
                        choice = int(choice)
                        if(choice == 1 or choice == 11):
                            validInput = True
                        else:
                            print("Invalid Input")
                            print("Please enter either 1 or 11")
                    else:
                        print("Invalid Input")
                        print("Please enter either 1 or 11")
                
                if(choice == 1):
                    self.__score += 1
                elif(choice == 11):
                    self.__score += 11
            else:
                #If not an ace value, but is 10, jack, queen or king then 10 is added to score
                if(newCard.getVal() > 9):
                    self.__score += 10
                #otherwise just add the score, should be cards 2-9
                else:
                    self.__score += newCard.getVal()
        else:
            #For round 1, if value is ace assume it is 11, if two aces then one 11 and one is set to 1
            if(newCard.getVal() == 1):
                self.__score += 11
                if(self.__score == 22): #Two aces
                    self.__score -= 10
            #10, jack queen and king are always value of 10
            elif(newCard.getVal() > 9):
                self.__score += 10
            #2-9 cards are added
            else:
                self.__score += newCard.getVal()
    
    #Prints player cards
    def displayCards(self):
        for card in self.__playerCards:
            print(card)
    
    #If player places bet of 0, iterate zeroCounter and check if they are eligible for drop, otherwise just set the currentBet
    def placeBet(self, bet):
        if(bet == 0):
            self.__zeroCounter += 1
            if(self.__zeroCounter == 3):
                self.drop()
        self.__currentBet = bet
    
    #Double down doubles current bet and sets stand Flag to true
    def doubleDown(self):
        self.__currentBet *= 2
        self.stand()
    
    #Losing bet subtracts bet value from balance
    def lostBet(self):
        self.__balance -= self.getBet()
    
    #Regular win gives 2:1 payback, since bet isnt removed from balance until a player loses just add same bet value to balance
    def regularWin(self):
        self.__balance += self.getBet()
    
    #blacjack win gives 3:1 payback, since bet isnt removed from balance until a player loses just add 2x bet value to balance    
    def blackJack(self):
        self.__blackJackFlag = True
        self.__balance += 2*self.getBet()
    
    def getScore(self):
        return self.__score
    
    def hasStand(self):
        return self.__standFlag
    
    def stand(self):
        self.__standFlag = True
    
    def hasBust(self):
        return self.__bustFlag
    
    #If player busts then set the flag to true and call lostBet function
    def busts(self):
        self.__bustFlag = True
        self.lostBet()
    
    def hasBlackJack(self):
        return self.__blackJackFlag
    
    def getBalance(self):
        return self.__balance
    
    def getBet(self):
        return self.__currentBet
    
    def drop(self):
        self.__dropFlag = True
    
    def isDropped(self):
        return self.__dropFlag
    
class Dealer():
    #initializing shoe
    def __init__(self):
        self.reset()
        self.__gameDeck = Shoe()
    
    #initializing dealers cards, score and bust flag
    def reset(self):
        self.__dealerCards = []
        self.__score = 0
        self.__bustFlag = False
    
    #returns a card object from the shoe
    def dealCard(self):
        return self.__gameDeck.popShoe()
    
    #dealer deals himself a card from shoe
    def dealSelf(self):
        newCard = self.dealCard()
        self.__dealerCards.append(newCard)
        #If ace and score is less than 11, 11 added to score otherwise add 1 to score
        if(newCard.getVal() == 1):
            if(self.getScore() < 11):
                self.__score += 11
            else:
                self.__score += 1
        #If card is 10, jack, queen or king add 10 to score, otherwise add 2-9 value cards to score
        else:
            if(newCard.getVal() > 9):
                self.__score += 10
            else:
                self.__score += newCard.getVal()
        
    def getScore(self):
        return self.__score
    
    #Displays dealer cards
    def displayCards(self):
        for card in self.__dealerCards:
            print(card)
            
    def busts(self):
        self.__bustFlag = True
        
    def hasBust(self):
        return self.__bustFlag

if __name__ == '__main__':
    gameDealer = Dealer()
    playerArr = []
    
    #Total number of players is random, can be 1 to 6 players
    randomPlayers = random.randint(1, 6)
    print("There are ", randomPlayers, " players at this table")
    for index in range(0, randomPlayers):
        playerArr.append(Player())
        print("Player ", index+1, " starting balance is: $", playerArr[index].getBalance())
    print()
    
    #Total number of games is random, 10 minimum to 16 maximum games
    totalGames = random.randint(10, 16)
    print("There will be ", totalGames, " games played")
    for currentGame in range(0, totalGames):
        print("---------------------------------------------------------")
        print("Game ", currentGame+1, "\n")
        #Game starts here, implement random amount of games
        
        if(currentGame > 0):
            for index in range(0, randomPlayers):
                print("Player ", index+1, " balance is: $", playerArr[index].getBalance())
            print()
        
        round = 1
        #Starting bets, only players who haven't been dropped from all games can place bets
        for playerIn in range(0, len(playerArr)):
            if(playerArr[playerIn].isDropped() == False):
                #Simple input validation, players can only bet 0 to sit out, or 25 to their balance minus one (no all in bets)
                validInput = False
                while(validInput == False):
                    print("Enter Player", playerIn+1, " bet amount: ")
                    tempBet = input()
                    if(tempBet.isnumeric() == True):
                        tempBet = int(tempBet)
                        if(tempBet == 0 or tempBet >= 25 and tempBet < playerArr[playerIn].getBalance()):
                            validInput = True
                        else:
                            print("Invalid Input")
                            print("Please enter either 0 to sit out for the game or a number between 25 and ", playerArr[playerIn].getBalance())
                    else:
                        print("Invalid Input")
                        print("Please enter either 0 to sit out for the game or a number between 25 and ", playerArr[playerIn].getBalance())
                playerArr[playerIn].placeBet(tempBet)
                print("Player ", playerIn+1, " starting bet: $", tempBet)
                print()
        
        #Displaying players who aren't able to play this game
        for playerIn in range(0, len(playerArr)):
            if(playerArr[playerIn].isDropped() == True and playerArr[playerIn].getBalance() < 50):
                print("Player ", playerIn+1, " dropped from all future games since balance is less than 50")
            elif(playerArr[playerIn].isDropped() == True and playerArr[playerIn].getBet() == 0): 
                print("Player ", playerIn+1, " dropped from all future games due to three bets of zero")
            elif(playerArr[playerIn].getBet() == 0):
                print("Player ", playerIn+1, " not in game since bet is zero")
        print()
        
        #First round, players that didnt bet 0 and players that are not dropped from the game dealt one card, then dealer
        for playerIn in range(0, len(playerArr)):
            if(playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False):  
                playerArr[playerIn].addCard(gameDealer.dealCard(), round)
            
        gameDealer.dealSelf()
        
        #Players dealt second cards
        for playerIn in range(0, len(playerArr)):
            if(playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False):  
                print("Player ", playerIn+1)
                playerArr[playerIn].addCard(gameDealer.dealCard(), round)
                print("Cards: ")
                playerArr[playerIn].displayCards()
                print("Score: ", playerArr[playerIn].getScore())
                print()
                if(playerArr[playerIn].getScore() == 21):
                    playerArr[playerIn].blackJack()
            
        #Dealer deals himself a card and it is displayed
        gameDealer.dealSelf()
        print("Dealer Cards: ")
        gameDealer.displayCards()
        print("Dealer Score: ", gameDealer.getScore(), "\n")
        
        #Player Rounds
        for playerIn in range(0, len(playerArr)):
            round = 2
            #If players bet is zero or they've been dropped for balance less than 50 or they have blackjack, skip their turn in this game
            if(playerArr[playerIn].getBet() == 0 or playerArr[playerIn].isDropped() == True or playerArr[playerIn].hasBlackJack() == True):
                if(playerArr[playerIn].hasBlackJack() == True):
                    print("Player ", playerIn+1, " has BlackJack, turn skipped")
                continue
            else:
                print("Player ", playerIn+1, " turn")
                print("---------------")
            #While player has not stood, bust, or gotten blackjack, continue to play
            while(playerArr[playerIn].hasStand() == False and playerArr[playerIn].hasBust() == False and playerArr[playerIn].hasBlackJack() == False):
                #Only in round two can player double down, split not implemented
                if(round == 2):
                    #Simple user input validation, user can only enter 1, 2 or 3
                    validInput = False
                    while(validInput == False):
                        print("Options Available: 1 Hit 2 Double Down 3 Stand")
                        userChoice = input("Enter option: ")
                        if(userChoice.isnumeric() == True):
                            userChoice = int(userChoice)
                            if(userChoice == 1 or userChoice == 2 or userChoice == 3):
                                validInput = True
                            else:
                                print("Invalid Input")
                                print("Please enter either 1, 2, or 3")
                        else:
                            print("Invalid Input")
                            print("Please enter either 1, 2, or 3")
                    
                    #If player chooses 1, deal a card, add to player, display it as well as players new score
                    if(userChoice == 1):
                        tempCard = gameDealer.dealCard()
                        playerArr[playerIn].addCard(tempCard, round)
                        print("Added Card: ", tempCard, ", Updated Score: ", playerArr[playerIn].getScore())
                    #If player chooses 2 and they do not have enough balance to double down, print output, go to next player round
                    #If player chooses 2 and they have enough balance, doubleDown doubles their bet and sets stand flag true, final card is dealt
                    #and new card is displayed along with updated score
                    elif(userChoice == 2):
                        if(playerArr[playerIn].getBet()*2 > playerArr[playerIn].getBalance()):
                            print("Player does not have enough in balance to double down")
                        else:
                            playerArr[playerIn].doubleDown()
                            tempCard = gameDealer.dealCard()
                            playerArr[playerIn].addCard(tempCard, round)
                            print("Added Card: ", tempCard, ", Updated Score: ", playerArr[playerIn].getScore(), ", Updated Bet: $", playerArr[playerIn].getBet())
                    #If player chooses 3 then the player stands, just sets a flag to true
                    elif(userChoice == 3):
                        playerArr[playerIn].stand()
                else:
                    #Simple user input validation, user can only enter 1 pr 2
                    validInput = False
                    while(validInput == False):
                        print("Options Available: 1 Hit 2 Stand")
                        userChoice = input("Enter option: ")
                        if(userChoice.isnumeric() == True):
                            userChoice = int(userChoice)
                            if(userChoice == 1 or userChoice == 2):
                                validInput = True
                            else:
                                print("Invalid Input")
                                print("Please enter either 1 or 2")
                        else:
                            print("Invalid Input")
                            print("Please enter either 1 or 2")
                    
                    #If player chooses 1, deal a card, add to player, display it as well as players new score
                    if(userChoice == 1):
                        tempCard=gameDealer.dealCard()
                        playerArr[playerIn].addCard(tempCard, round)
                        print("Added Card: ", tempCard, ", Updated Score: ", playerArr[playerIn].getScore())
                    #If player chooses 3 then the player stands, just sets a flag to true
                    elif(userChoice == 2):
                        playerArr[playerIn].stand()
                
                #If player gets blackjack the blackjack flag is set to true, win info displayed later
                if(playerArr[playerIn].getScore() == 21):
                    playerArr[playerIn].blackJack()
                #If player busts during game, prompt displayed, busts decreases balance and sets flag to True, new balance displayed
                elif(playerArr[playerIn].getScore() > 21):
                    playerArr[playerIn].busts()
                    print("Player busts! Updated Balance: $", playerArr[playerIn].getBalance())
                #If player stands, prompt displayed
                elif(playerArr[playerIn].hasStand() == True):
                    print("Player stands, wait for dealer to play")
                print()
                round += 1
        print()
        
        #Dealer deals himself a card until he hits 17 or higher
        while(gameDealer.getScore() < 17):
            gameDealer.dealSelf()
        #Updated cards displayer
        print("Updated Dealer Cards: ")
        gameDealer.displayCards()
        print("Updated Dealer Score: ", gameDealer.getScore())
        #If dealer busts then prompt is displayed and flag is set to true
        if(gameDealer.getScore() > 21):
            print("Dealer busts!")
            gameDealer.busts()
        print()
        
        #If dealer busts then every player that hasnt busted during the game wins
        if(gameDealer.hasBust() == True):
            for playerIn in range(0, len(playerArr)):
                if(playerArr[playerIn].hasBust() == False and playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False):
                    if(playerArr[playerIn].hasBlackJack()):
                        print("Player ", playerIn+1, " wins by Black Jack! Updated Balance: $", playerArr[playerIn].getBalance())
                    else:
                        playerArr[playerIn].regularWin()
                        print("Player ", playerIn+1, " has won! Updated Balance: $", playerArr[playerIn].getBalance())
        #If dealer is between 17 and 21, blackjack winners are displayed, players above score of dealer get regular win (win double the bet)
        #Players with score below dealers lose their bet
        else:
            for playerIn in range(0, len(playerArr)):
                if(playerArr[playerIn].hasBust() == False and playerArr[playerIn].getBet() != 0 and playerArr[playerIn].isDropped() == False):
                    if(playerArr[playerIn].hasBlackJack()):
                        print("Player ", playerIn+1, " wins by Black Jack! Updated Balance: $", playerArr[playerIn].getBalance())
                    elif(playerArr[playerIn].getScore() > gameDealer.getScore()):
                        playerArr[playerIn].regularWin()
                        print("Player ", playerIn+1, " wins! Updated Balance: $", playerArr[playerIn].getBalance())
                    else:
                        playerArr[playerIn].lostBet()
                        print("Player ", playerIn+1, " loses to dealer Updated Balance: $", playerArr[playerIn].getBalance())
        print()
        
        #Check to see if players balance is below 50, if they are then set drop flag to true and prompt
        for playerIn in range(0, len(playerArr)):
            if(playerArr[playerIn].isDropped() == False and playerArr[playerIn].getBalance() < 50):
                print("Player ", playerIn+1, " has been dropped since balance is less than 50")
                playerArr[playerIn].drop()
        print()
        
        #Resetting players and dealer
        for player in playerArr:
            player.reset()
        gameDealer.reset()