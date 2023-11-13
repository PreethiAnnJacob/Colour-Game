# Author: Preethi Ann Jacob
# 13th November 2023

# Program for a game where we have to write the colour of the text written. The text will always be the name of a colour other than its original font colour.

import tkinter # tkinter module - standard Python Interface to Tk GUI toolkit
import random

# Given a list of possible colours. Initially Score = 0. Time Left is 30 seconds
colours = ["Red", "Green", "Blue", "Black", "White", "Yellow", "Brown", "Orange", "Pink"]
score = 0
timeLeft = 30

# function to start the game
def startGame(event):
	if timeLeft == 30:
		countDownTimer() # To start the countdown timer
	chooseNextColour() # Run the function to choose the next colour

# function to choose and display the next colour
def chooseNextColour():
	# Using the global keyword in local function to modify the global variable value
	global score
	global timeLeft
	# If a game is currently in play
	if timeLeft>0: 
		typeHere.focus_set() # Make the text entry box active
		# If Colour matches correctly, increment score
		if typeHere.get().lower() == colours[1].lower(): 
			score+=1 
		typeHere.delete(0,tkinter.END) #clear the text entry box # To delete all text, we have to specify the first and last index as parameters
		random.shuffle(colours)
		colourLabel.config( fg = str(colours[1]), text = str(colours[0])) # fg= foreground colour. So we set font colour and the text to different colours
		scoreLabel.config( text = "Score: " + str(score))

# function for CountDown Timer
def countDownTimer():
	global timeLeft
	# if the game is currently in play, decrement the timer by one
	if timeLeft>0:
		timeLeft-=1
		timeLabel.config(text = "Time left: " + str(timeLeft))
		timeLabel.after(1000, countDownTimer) # Call the countDownTimer after 1 second

# Creating a GUI window. Set title, size, icon to that window.
root = tkinter.Tk() 
root.title("COLOUR GAME")
root.geometry("375x200") 
root.iconbitmap(r"F:\I am trying to get better\13.11.2023 Colour Game - Python\icon.ico")
# root.wm_iconbitmap(r"F:\I am trying to get better\13.11.2023 Colour Game - Python\icon.ico")

# Add labels for 1. Instructions 2. Show score 3. Show time left 4. Show colour
instructionsLabel = tkinter.Label(root, text = "Type in the font colour of the words! Not the text :D", font = ("Helvetica",12))
scoreLabel = tkinter.Label(root, text = "Press enter to start!", font = ("Helvetica",12))
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeLeft), font = ("Helvetica",12))
colourLabel = tkinter.Label(root, font = ("Helvetica", 60))

# Add text entry box for typing 
typeHere = tkinter.Entry(root)

# Tkinter packs all the widgets one after the other in the window
instructionsLabel.pack()
scoreLabel.pack()
timeLabel.pack()
colourLabel.pack()
typeHere.pack()

# Make the text entry box active 
typeHere.focus_set()

# When Enter key is pressed, run the startGame function
root.bind('<Return>', startGame)

root.mainloop() # Start the GUI