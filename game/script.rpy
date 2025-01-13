define supchelkip = Character("Supchelkip")
define narrator = Character("Y/N")

default sup_hello = "characters/supchelkip/sup_hello.png"

label start:
    scene bg room
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
    
    return
