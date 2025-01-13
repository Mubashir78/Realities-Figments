# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define supchelkip = Character("Supchelkip")
define narrator = Character("Y/N")
default sup_hello = "characters/supchelkip/sup_hello.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sup_hello with dissolve

    supchelkip "Hiya!"

    hide sup_hello with dissolve

    narrator "The Player wakes up on a damp, cold floor."
    narrator "Their memory is fuzzy."
    narrator "They don't know anything about what's going on."
    narrator "They look around their surroundings."
    
    menu:
        "Look in front":
            narrator "You look in front of you which leads outside."
        
        "Look left":
            narrator "You look through your left."
            narrator "Somehow it seems familiar."
            
        "Look right":
            narrator "You look to your right hearing a bunch of tech sounds."
        


    # This ends the game.

    return
