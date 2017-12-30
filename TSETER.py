
from tkinter import *

####################################
# customize these functions
####################################

def init(data, width = 500, height = 500):
    # load data.xyz as appropriate
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
    pass
    
def playTwoPlayer(canvas, data):
    if data.playerOneMove == True:
        str = "One"
    if data.playerOneMove == False:
        str = "Two"
        print("this should print lol")
    
    canvas.create_text(250, 50, text = "Player %s Move" % str,
         font = "Arial 30 bold")
    canvas.create_text(data.width//4, 250, text = "Rock", 
    font = "Arial 25")
    canvas.create_rectangle(data.width//4-50, 235, data.width//4+50, 265)
    canvas.create_text(data.width*2//4, 250, text = "Paper", 
    font = "Arial 25")
    canvas.create_rectangle(data.width*2//4-50, 235, data.width*2//4+50, 265)
    canvas.create_text(data.width*3//4, 250, text = "Scissor",
        font = "Arial 25")
    canvas.create_rectangle(data.width*3//4-50, 235, data.width*3//4+50, 265)

        
def gameOverScreen(canvas, data):
    canvas
    canvas.create_text(150, 400, text = "Player One Score: %d" % data.oneScore)
    canvas.create_text(300, 400, text = "Player Two Score: %d" % data.twoScore)
    
    if data.playerOneChoice == "rock":
        if data.playerTwoChoice == "rock":
        	data.playerTwoChoice = ""
        	data.playerOneChoice = ""
        elif data.playerTwoChoice == "paper":
            canvas.create_text(250, 250, text = "Player One Wins!")
            data.oneScore += 1
            data.playerOneChoice = ""
            data.playerTwoChoice = ""
        else:
            canvas.create_text(250, 250, text = "Player Two Wins!")
            data.twoScore += 1
            data.playerOneChoice = ""
            data.playerTwoChoice = ""
    if data.playerOneChoice == "paper":
        if data.playerTwoChoice == "rock":
        	canvas.create_text(250, 250, text = "Player One Wins!")
        	data.oneScore += 1
        	data.playerOneChoice = ""
        	data.playerTwoChoice = ""
        elif data.playerTwoChoice == "paper":
            canvas.create_text(250, 250, text = "It's a draw!")
            data.playerTwoChoice = ""
        else:
            canvas.create_text(250, 250, text = "Player Two Wins!")
            data.twoScore += 1
            data.playerOneChoice = ""
            data.playerTwoChoice = ""
    if data.playerOneChoice == "scissor":
        if data.playerTwoChoice == "rock":
        	canvas.create_text(250, 250, text = "Player Two Wins!")
        	data.twoScore += 1
        	data.playerOneChoice = ""
        	data.playerTwoChoice = ""
        elif data.playerTwoChoice == "paper":
            canvas.create_text(250, 250, text = "Player Two Wins!")
            data.oneScore += 1
            data.playerTwoChoice = ""
            data.playerOneChoice = ""
        else:
            canvas.create_text(250, 250, text = "It's a draw!")
            data.playerTwoChoice = ""
            data.playerOneChoice = ""
    

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
                (event.y >235 and event.y < 265)):
                    print("HIIIII")
                    data.playerOneChoice = "rock"
                    data.playerOneMove = False
            elif ((event.x > data.width*2//4-50 and event.x < data.width*2//4+50) and
                (event.y >235 and event.y < 265)):
                    data.playerOneChoice = "paper"
                    data.playerOneMove = False
            elif ((event.x > data.width*3//4-50 and event.x < data.width*3//4+50) and
                (event.y >235 and event.y < 265)):
                    data.playerOneChoice = "paper"
                    data.playerOneMove = False
        else:
            if ((event.x > data.width//4-50 and event.x < data.width//4+50) and
                (event.y >235 and event.y < 265)):
                    data.playerTwoChoice = "rock"
                    data.twoPlayer = False
                    data.gameOver = True
            elif ((event.x > data.width*2//4-50 and event.x < data.width*2//4+50) and
                (event.y >235 and event.y < 265)):
                    data.playerTwoChoice = "paper"
                    data.twoPlayer = False
                    data.gameOver = True
            elif ((event.x > data.width*3//4-50 and event.x < data.width*3//4+50) and
                (event.y >235 and event.y < 265)):
                    data.playerTwoChoice = "paper"
                    data.twoPlayer = False
                    data.gameOver = True
                
            
    

def keyPressed(event, data):
    # use event.char and event.keysym
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
    if data.gameOver == True:
        gameOverScreen(canvas, data)

####################################
# use the run function as-is
####################################

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
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)