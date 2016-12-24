import os
#os.chdir('C:/Workspace/Python/Group Projects/Hand Reader')
os.chdir("wherever-you-have-stored-the-'cards.py'-file")
import cards

print("Hi there! Tell what cards you hold, and I'll tell you if you have any hands or not....")
myHand = cards.hand()
cardList = []
for i in range(0, 5):
    cardList.append(input("Enter the cardname : "))

myHand.addCard(cardList)
print("You have {0}.".format(cards.whichHand(myHand)))
