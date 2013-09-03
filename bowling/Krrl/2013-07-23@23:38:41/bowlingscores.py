import sys

def strike(currentgame,currentindex):
    framescore = 10
    secondball = currentgame[currentindex+1]
    thirdball = currentgame[currentindex+2]
    if secondball == 'X' and thirdball == 'X':
        framescore += 20
        return framescore
    elif secondball == 'X' and thirdball != 'X':
        framescore += 10
        framescore += int(thirdball)
        return framescore
    elif secondball != 'X' and thirdball == '/':
        framescore += 10
        return framescore
    else:
        framescore += int(secondball)
        framescore += int(thirdball)
        return framescore

def spare(currentgame,currentindex):
    framescore = 10
    secondball = currentgame[currentindex+2]
    if secondball == 'X':
        framescore += 10
        return framescore
    else:
        framescore += int(secondball)
        return framescore
    
def scoring (game):
    frame = 1
    i = 0
    totalscore = 0
    while i < len(game):
        while frame <= 10:
            if game[i] == 'X':
                totalscore += strike(game,i)
                frame += 1
                i += 1
            elif game[i+1] == '/':
                totalscore += spare(game,i)
                frame += 1
                i += 2
            else:
                totalscore += int(game[i])
                totalscore += int(game[i+1])
                i += 2
                frame += 1
        break
    return totalscore

    
    
f = open(sys.argv[1])

text = f.read()

text = text.split('\n')
while text[-1] == "":
    del text[-1]

listOfGames = []

for item in text:
    listOfGames.append(item.replace(" ", ""))

for game in listOfGames:
    print (scoring(game))
    