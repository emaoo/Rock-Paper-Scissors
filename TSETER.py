#Eileen Mao 
#CMU 2021
#GWC
#tkinter mainloop 15112

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
    data.timerCount = 0 

def startingScreen(canvas, data):
    ultimateFill = ""
    if data.timerCount < 5:
        ultimateFill = "#1F271B"
    else:
        ultimateFill = "#F4442E"
    canvas.create_rectangle(-50, -50, 550, 550, fill = "#19647E")
    canvas.create_rectangle(10, 10, 495, 495, fill = "#F4D35E")
    canvas.create_text(250, 50, fill = "#1F271B",
                        text = "THE", font = "Chalkboard 28 bold")
    canvas.create_text(250, 100, fill = ultimateFill,
                        text = "ULTIMATE", font = "Chalkboard 50 bold")
    canvas.create_text(250, 150, fill = "#1F271B",
                        text = "ROCK, PAPER, SCISSORS GAME", font = "Chalkboard 28 bold")
    canvas.create_rectangle(100, 225, 400, 275, fill = "#28AFB0", width = 3)
    canvas.create_text(250, 250,
                        text = "One Player Mode", font = "Chalkboard 28 bold")
    canvas.create_rectangle(100, 325, 400, 375, fill = "#EE964B", width = 3)
    canvas.create_text(250, 350,
                        text = "Two Player Mode", font = "Chalkboard 28 bold")
    
def playOnePlayer(canvas, data):
    if data.onePlayer == True:
        canvas.create_rectangle(-50, -50, 550, 550, fill = "#F4D35E")
        canvas.create_rectangle(10, 10, 495, 495, fill = "#28AFB0")
        canvas.create_rectangle(data.width//4-50, 280, data.width//4+50, 320, fill = "#EE964B", width = 3)
        canvas.create_rectangle(data.width*2//4-50, 280, data.width*2//4+50, 320, fill = "#EE964B", width = 3)
        canvas.create_rectangle(data.width*3//4-50, 280, data.width*3//4+50, 320, fill = "#EE964B", width = 3)
        canvas.create_text(250, 100, fill = "#1F271B", text = "Your Move", font = "Chalkboard 40 bold")
        canvas.create_text(data.width//4, 300, text = "Rock", 
        font = "Chalkboard 25")
        
        canvas.create_text(data.width*2//4, 300, text = "Paper", 
        font = "Chalkboard 25")
        
        canvas.create_text(data.width*3//4, 300, text = "Scissor",
            font = "Chalkboard 25")
        
        
    
def playTwoPlayer(canvas, data):
    canvas.create_rectangle(-50, -50, 550, 550, fill = "#28AFB0")
    canvas.create_rectangle(10, 10, 495, 495, fill = "#EE964B")
    canvas.create_oval(228, 125, 300, 126, width = 6)
    canvas.create_rectangle(data.width//4-50, 280, data.width//4+50, 320, fill = "#19647E", width = 3)
    canvas.create_rectangle(data.width*2//4-50, 280, data.width*2//4+50, 320, fill = "#19647E", width = 3)
    canvas.create_rectangle(data.width*3//4-50, 280, data.width*3//4+50, 320, fill = "#19647E", width = 3)
    if data.playerOneMove == True:
        str = "One"
    if data.playerOneMove == False:
        str = "Two"

    canvas.create_text(250, 100, text = "Player %s Move" % str,
         font = "Chalkboard 40 bold")
    canvas.create_text(data.width//4, 300, text = "Rock", fill = "#F9F8F8",
    font = "Chalkboard 25")
    
    canvas.create_text(data.width*2//4, 300, text = "Paper", fill = "#F9F8F8",
    font = "Chalkboard 25")

    canvas.create_text(data.width*3//4, 300, text = "Scissor", fill = "#F9F8F8",
        font = "Chalkboard 25")
    

        
def gameOverScreenWords(canvas, data): 
    if data.gameOverTextDisplay == True:
        canvas.create_rectangle(10, 10, 495, 495, fill = "#1F271B")
        canvas.create_rectangle(175, 220, 320, 280, fill = "#462255")
        canvas.create_rectangle(175, 290, 320, 350, fill = "#568259")
        canvas.create_text(data.width//2, data.height//3,fill = "#FE4A49",text=data.gameOverText, 
        font = "Chalkboard 30 bold")
        
        canvas.create_text(130, 400, fill = "#FFEE93", text = "Player One Score = %d" % data.oneScore, font = "Chalkboard 20 bold")
        canvas.create_text(370, 400, fill = "#ADF7B6", text = "Player Two Score = %d" % data.twoScore , font = "Chalkboard 20 bold")
        canvas.create_text(250, 250, fill = "#FCF5C7", text = "Play Again", 
        font = "Chalkboard 25 bold")
        canvas.create_text(250, 320, fill = "#FCF5C7", text = "Home", 
        font = "Chalkboard 30 bold")
        canvas.create_text(data.width//2+10, 100, fill = "#F4D35E", 
        text = "Player one played %s & Player two played %s " % (data.playerOneChoice, data.playerTwoChoice), font = "Chalkboard 18 bold", )
        
    
def AIGameOverScreenWords(canvas, data):
    if data.AIGameOverTextDisplay == True:
        
        canvas.create_rectangle(10, 10, 495, 495, fill = "#1F271B")
        canvas.create_rectangle(175, 220, 320, 280, fill = "#462255")
        canvas.create_rectangle(175, 290, 320, 350, fill = "#2A324B")
        canvas.create_text(data.width//2, data.height//3,fill = "#FE4A49", text=data.gameOverText, font = "Chalkboard 30 bold")
        canvas.create_text(data.width//2, 100, fill = "#F4D35E", 
        text = "You played %s & AI played %s " % (data.yourChoice, data.AIChoice), font = "Chalkboard 20 bold", )
       
        canvas.create_text(150, 400, fill = "#FFC09F", text = "Your Score = %d" % data.yourScore, 
        font = "Chalkboard 20 bold")
        canvas.create_text(350, 400, fill = "#A0CED9", text = "AI Score = %d" % data.AIScore, 
        font = "Chalkboard 20 bold")
        canvas.create_text(250, 250, fill = "#FCF5C7", text = "Play Again", 
        font = "Chalkboard 25 bold")
        canvas.create_text(250, 320, fill = "#FCF5C7", text = "Home", 
        font = "Chalkboard 30 bold")


        
    
def gameOverScreen(canvas, data):
    if data.gameOver == True:
        data.gameOverTextDisplay = True
        canvas.create_text(150, 400, text = "Player One Score: %d" % data.oneScore)
        canvas.create_text(300, 400, text = "Player Two Score: %d" % data.twoScore)
        
        if data.playerOneChoice == "rock":
            if data.playerTwoChoice == "rock":
                data.gameOverText = "It's a draw!"
            elif data.playerTwoChoice == "paper":
                data.gameOverText =  "Player Two Wins!"
                data.twoScore += 1
                
            else:
                data.gameOverText = "Player One Wins!"
                data.oneScore += 1
                
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
                data.gameOverText =  "Player One Wins!"
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
        if event.x >175 and event.x < 320:
            if event.y > 290 and event.y < 350:
                data.startingScreen = True
                data.gameOverTextDisplay = False
                data.gameOver = False
                data.playerOneMove = ""
                data.playerTwoMove = ""
                data.playerOneMove = True
                data.onePlayer = False
                
                data.oneScore = 0
                data.twoScore = 0
                data.twoPlayer = False
        if event.x > 175 and event.x < 320:
            if event.y > 220 and event.y <280:
                data.startingScreen = False
                data.gameOverTextDisplay = False
                data.gameOver = False
                data.playerOneMove = ""
                data.playerTwoMove = ""
                data.playerOneMove = True
                data.twoPlayer = True
                data.onePlayer = False
    if data.onePlayer == True:
            if ((event.x > data.width//4-50 and event.x < data.width//4+50) and
                (event.y >285 and event.y < 325)):
          
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
       
    if data.AIGameOverTextDisplay == True:
        if event.x >175 and event.x < 320:
            if event.y > 290 and event.y < 350:
                data.startingScreen = True
                data.AIGameOverTextDisplay = False
                data.AIGameOver = False
                data.AIChoice = ""
                data.yourChoice = ""
                data.onePlayer = False
                data.AIScore = 0
                data.yourScore = 0
                data.twoPlayer = False
        if event.x > 175 and event.x < 320:
            if event.y > 220 and event.y <280:
                data.startingScreen = False
                data.AIGameOverTextDisplay = False
                data.AIGameOver = False
                data.AIChoice = ""
                data.yourChoice = ""
                data.onePlayer = True
                data.twoPlayer = False
                
                
    

def keyPressed(event, data):
   
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    data.timerCount += 1
    if data.timerCount > 10:
        data.timerCount = 0
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
    print("Game Over!")

run(500, 500)
