# This is an algorithm for the Maze on ReeBorgs world
# Go to the link, past this code an observe Reeborg escape the maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json



def turn_right():
    # there is no built in turn_right so I made one
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    # there is no built in turn_right so I made one
    turn_left()
    turn_left()
    

while front_is_clear() == True:
    move() #Keep moving until he hits a wall to start the maze
turn_left()
# This prevents Reeborg getting stuck in an infinite loop when he spawns in with no walls near him

while at_goal() == False:
   
    if right_is_clear() == True:
        turn_right()
        move() # this is make sure we are always hugging a wall to the right
    elif front_is_clear() == True:
        move() #if there is no wall on the right then we keep moving forward
    else:
        turn_left() # We always hug the wall to the right, or keep moving forward. Turning left is the last thing we do