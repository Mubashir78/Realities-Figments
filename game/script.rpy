define supchelkip = Character("Supchelkip", color="#FF318A")
define narrator = Character("Narrator", color="#A3A3A3")
define nar = Character("Nar")
define mudkip = Character("Mudkip", color="#4859F5")
define mc = Character("Y/N", color="#FF7531")

default sup_hello = "characters/supchelkip/sup_hello.png"
define bg_forest =  "backgrounds/forest_path.png"
default wrong_name = True

label start:
    scene forest_path with fade
    
    while wrong_name:
        $ player_name = renpy.input("Enter the Player's name.", length=32).strip()
    
        narrator "You will play as [player_name]. Is that correct?"
    
        menu:
            "Yes, its correct.":
                $ wrong_name = False

            "No, let me change it.":
                pass
            
    narrator "[player_name] wakes up on a damp, cold floor."
    narrator "Your memory is fuzzy."
    narrator "You don't know anything about what's going on."
    
    menu:
        narrator "You look around your surroundings."

        "Look in front":
            narrator "You look in front of you which leads outside."
        
        "Look left":
            scene bg_house with Dissolve(0.5)
            narrator "You look through your left."
            narrator "Somehow it seems familiar."
            
            # scene change with Dissolve(0.5)
            
            narrator "You find someone standing in front of you."
            nar "Hey [player_name]! Over here!"
            
            narrator "Interesting. They know your name."
            narrator "With confused looks, you approach the person."
            
            mc "Huh!? How do you know my name??"
            nar "Oh that? Haha, everyone knows who you are in this world."
            
            
        "Look right":
            scene bg_crane with Dissolve(0.5)
            narrator "You look to your right hearing a bunch of tech sounds."
    
    return
