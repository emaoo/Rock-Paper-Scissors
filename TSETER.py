
from tkinter import *
import random

def init(data, width = 500, height = 500):
  
    data.width = width
    data.height = height
    data.startingScreen = True
    data.onePlayer = False
    data.twoPlayer = False
    data.oneScore = 0
    data.twoScore = 0
    data.playerOneMove = True
    data.playerOneChoice = ""
    data.playerTwoChoice = ""
    data.gameOver = False
    data.gameOverText = ""
    data.gameOverTextDisplay = False
    data.dictionaryAI = {"rock": 1, "paper": 1, "scissor": 1}
    data.yourChoice = ""
    data.AIGameOver = False
    data.AIChoice = ""
    data.highScore = dict()
    data.yourScore = 0
    data.AIGameOverTextDisplay = False
    data.AIScore= 0

def startingScreen(canvas, data):
    canvas.create_text(250, 50,
                        text = "THE ULTIMATE", font = "Arial 30 bold")
    canvas.create_text(250, 100,
                        text = "ROCK, PAPER, SCISSORS GAME", font = "Arial 30 bold")
    canvas.create_rectangle(100, 225, 400, 275, fill = "yellow")
    canvas.create_text(250, 250,
                        text = "One Player Mode", font = "Arial 30 bold")
    canvas.create_rectangle(100, 325, 400, 375, fill = "green")
    canvas.create_text(250, 350,
                        text = "Two Player Mode", font = "Arial 30 bold")
    
def playOnePlayer(canvas, data):
    if data.onePlayer == True:
        canvas.create_text(250, 50, text = "Your Move")
        canvas.create_text(data.width//4, 300, text = "Rock", 
        font = "Arial 25")
        canvas.create_rectangle(data.width//4-50, 285, data.width//4+50, 325)
        canvas.create_text(data.width*2//4, 300, text = "Paper", 
        font = "Arial 25")
        canvas.create_rectangle(data.width*2//4-50, 285, data.width*2//4+50, 325)
        canvas.create_text(data.width*3//4, 300, text = "Scissor",
            font = "Arial 25")
        canvas.create_rectangle(data.width*3//4-50, 285, data.width*3//4+50, 325)
        
    
def playTwoPlayer(canvas, data):
    if data.playerOneMove == True:
        str = "One"
    if data.playerOneMove == False:
        str = "Two"
        
    
        canvas.create_text(250, 50, text = "Your Move")
        canvas.create_text(data.width//4, 300, text = "Rock", 
        font = "Arial 25")
        canvas.create_rectangle(data.width//4-50, 285, data.width//4+50, 325)
        canvas.create_text(data.width*2//4, 300, text = "Paper", 
        font = "Arial 25")
        canvas.create_rectangle(data.width*2//4-50, 285, data.width*2//4+50, 325)
        canvas.create_text(data.width*3//4, 300, text = "Scissor",
            font = "Arial 25")
        canvas.create_rectangle(data.width*3//4-50, 285, data.width*3//4+50, 325)

        
def gameOverScreenWords(canvas, data): 
    if data.gameOverTextDisplay == True:
   
        canvas.create_text(data.width//2, data.height//3,text=data.gameOverText)
        canvas.create_text(100, 400, text = "Player One Score = %d" % data.oneScore)
        canvas.create_text(300, 400, text = "Player Two Score = %d" % data.twoScore)
        canvas.create_text(250, 250, text = "back to home")
        canvas.create_rectangle(220, 220, 270, 270)
    
def AIGameOverScreenWords(canvas, data):
    if data.AIGameOverTextDisplay == True:

        canvas.create_text(data.width//2, data.height//3,text=data.gameOverText)
        canvas.create_text(100, 400, text = "Your Score = %d" % data.yourScore)
        canvas.create_text(300, 400, text = "AI Score = %d" % data.AIScore)
        canvas.create_text(250, 250, text = "back to home")
        canvas.create_rectangle(220, 220, 270, 270)

        
    
def gameOverScreen(canvas, data):
    if data.gameOver == True:
        data.gameOverTextDisplay = True
        canvas.create_text(150, 400, text = "Player One Score: %d" % data.oneScore)
        canvas.create_text(300, 400, text = "Player Two Score: %d" % data.twoScore)
        
        if data.playerOneChoice == "rock":
            if data.playerTwoChoice == "rock":
                data.gameOverText = "It's a draw!"
            elif data.playerTwoChoice == "paper":
                data.gameOverText =  "Player One Wins!"
                data.oneScore += 1
                
            else:
                data.gameOverText = "Player Two Wins!"
                data.twoScore += 1
                
        if data.playerOneChoice == "paper":
            if data.playerTwoChoice == "rock":
                data.gameOverText =  "Player One Wins!"
                data.oneScore += 1
                
            elif data.playerTwoChoice == "paper":
                data.gameOverText =  "It's a draw!"
                
            else:
                data.gameOverText =  "Player Two Wins!"
                data.twoScore += 1
                
        if data.playerOneChoice == "scissor":
            if data.playerTwoChoice == "rock":
                data.gameOverText =  "Player Two Wins!"
                data.twoScore += 1
                
            elif data.playerTwoChoice == "paper":
                data.gameOverText =  "Player Two Wins!"
                data.oneScore += 1
                
            else:
                data.gameOverText =  "It's a draw!"
    data.gameOver = False

def AIGameOver(canvas, data):
    if data.AIGameOver == True:
        data.AIGameOverTextDisplay = True
        
        
        if data.yourChoice == "rock":
            if data.AIChoice == "rock":
                data.gameOverText = "It's a draw!"
            elif data.AIChoice == "paper":
                data.gameOverText =  "AI Wins!"
                data.AIScore += 1
                
            else:
                data.gameOverText = "You Win!"
                data.yourScore += 1
                
        if data.yourChoice == "paper":
            if data.AIChoice == "rock":
                data.gameOverText =  "You Win!"
                data.yourScore += 1
                
            elif data.AIChoice == "paper":
                data.gameOverText =  "It's a draw!"
                
            else:
                data.gameOverText =  "AI Wins!"
                data.AIScore += 1
                
        if data.yourChoice == "scissor":
            if data.AIChoice == "rock":
                data.gameOverText =  "AI Wins!"
                data.AIScore += 1
                
            elif data.AIChoice == "paper":
                data.gameOverText =  "You Win!"
                data.yourScore += 1
                
            else:
                data.gameOverText =  "It's a draw!"
    data.AIGameOver = False
    
    
        
    

def mousePressed(event, data):
    if event.x > 100 and event.x < 400:
        if event.y > 225 and event.y <275:
            data.onePlayer = True
            data.startingScreen = False
        if event.y > 325 and event.y <375:
            data.twoPlayer = True
            data.startingScreen = False
    if data.twoPlayer == True:
        if data.playerOneMove == True:
            if ((event.x > data.width//4-50 and event.x < data.width//4+50) and
                (event.y >285 and event.y < 325)):
                    print("HIIIII")
                    data.playerOneChoice = "rock"
                    data.playerOneMove = False

            elif ((event.x > data.width*2//4-50 and event.x < data.width*2//4+50) and
                (event.y >285 and event.y < 325)):
                    data.playerOneChoice = "paper"
                    data.playerOneMove = False
            elif ((event.x > data.width*3//4-50 and event.x < data.width*3//4+50) and
                (event.y >285 and event.y < 325)):
                    data.playerOneChoice = "scissor"
                    data.playerOneMove = False
        else:
            if ((event.x > data.width//4-50 and event.x < data.width//4+50) and
                (event.y >285 and event.y < 325)):
                    data.playerTwoChoice = "rock"
                    data.twoPlayer = False
                    data.gameOver = True
            elif ((event.x > data.width*2//4-50 and event.x < data.width*2//4+50) and
                (event.y >285 and event.y < 325)):
                    data.playerTwoChoice = "paper"
                    data.twoPlayer = False
                    data.gameOver = True
            elif ((event.x > data.width*3//4-50 and event.x < data.width*3//4+50) and
                (event.y >285 and event.y < 325)):
                    data.playerTwoChoice = "scissor"
                    data.twoPlayer = False
                    data.gameOver = True
    if data.gameOverTextDisplay == True:
        if event.x > 220 and event.x < 270:
            if event.y > 220 and event.y <270:
                data.startingScreen = True
                data.gameOverTextDisplay = False
                data.gameOver = False
                data.playerOneMove = ""
                data.playerTwoMove = ""
                data.playerOneMove = True
    if data.onePlayer == True:
            if ((event.x > data.width//4-50 and event.x < data.width//4+50) and
                (event.y >285 and event.y < 325)):
                    print("HIIIII")
                    data.yourChoice = "rock"
                    data.dictionaryAI["paper"] += 1
                    data.AIGameOver = True
                    data.onePlayer = False
            elif ((event.x > data.width*2//4-50 and event.x < data.width*2//4+50) and
                (event.y >285 and event.y < 325)):
                    data.yourChoice = "paper"
                    data.dictionaryAI["scissor"] += 1
                    data.AIGameOver = True
                    data.onePlayer = False
            elif ((event.x > data.width*3//4-50 and event.x < data.width*3//4+50) and
                (event.y >285 and event.y < 325)):
                    data.yourChoice = "scissor"
                    data.dictionaryAI["rock"] +=1
                    data.AIGameOver = True
                    data.onePlayer = False
            data.AIChoice = (random.choice([x for x in data.dictionaryAI for y in range(data.dictionaryAI[x])]))
            print("ai choice = ", data.AIChoice)
            
    if data.AIGameOverTextDisplay == True:
        if event.x > 220 and event.x < 270:
            if event.y > 220 and event.y <270:
                data.startingScreen = True
                data.AIGameOverTextDisplay = False
                data.AIGameOver = False
                data.AIChoice = ""
                data.yourChoice = ""
                data.onePlayer = False
                
    

def keyPressed(event, data):
   
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.startingScreen == True:
        startingScreen(canvas, data)
    if data.onePlayer == True:
        playOnePlayer(canvas, data)
    if data.twoPlayer == True:
        playTwoPlayer(canvas, data)
    gameOverScreen(canvas, data)
    gameOverScreenWords(canvas, data)
    AIGameOver(canvas, data)
    AIGameOverScreenWords(canvas, data)
    print(data.dictionaryAI)


def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)

        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
 
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 
    init(data)

    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    
    root.mainloop()  
    print("bye!")

run(500, 500)
