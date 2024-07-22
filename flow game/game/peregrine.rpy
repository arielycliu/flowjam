transform stretch_to_fill:
    xysize (config.screen_width, config.screen_height)

define peregrine = Character("Peregrine")

label peregrine1:
    $ part2 = 1
    scene
    $ peregrine_bookmark = "peregrine1"
    show screen basics
    show bg knightroom

    "A mortal kneels against a wall in a squire's lodgings, quill set to parchment."

    "Her tongue is sticking slightly out of her mouth, and she hums a simple line of plainsong under her breath."

    "..."

label peregrine11:
    scene
    $ peregrine_bookmark = "peregrine11"
    show screen basics
    show bg knightroom

    "I don't think she's going to notice me."

    "Overcoming my hesitation, I walk up and gently tap her on the shoulder."

label peregrine12:
    scene
    $ peregrine_bookmark = "peregrine12"
    show screen basics
    show bg knightroom

    show peregrine mad
    "She whirls around with a swiftness that can only be born through combat."

    "She slams me against the wall, blade in hand."

    "Even knowing I cannot be killed, I feel a pinprick of fear."

label peregrine13:
    scene
    $ peregrine_bookmark = "peregrine13"
    show screen basics
    show bg knightroom

    show peregrine mad
    "Can mortals hurt us?"

    "Shouldn't Elias have mentioned this?"

    "Maybe they did? They did mention quite a lot of details."

label peregrine14:
    scene
    $ peregrine_bookmark = "peregrine14"
    show screen basics
    show bg knightroom

    show peregrine mad
    mc "Peregrine-!"

    show peregrine shocked
    peregrine "Who are you? How did you get in here?"

    peregrine "How do you know my name?"

    mc "I-"

label peregrine15:
    scene
    $ peregrine_bookmark = "peregrine15"
    show screen basics
    show bg knightroom

    show peregrine shocked
    mc "You called for me!"

    peregrine "What?"

label peregrine16:
    scene
    $ peregrine_bookmark = "peregrine16"
    show screen basics
    show bg knightroom

    show peregrine neutral
    mc "You wanted help with writing something, yes?"

    mc "That's what I'm here for."

    mc "I'm a minor god."

    show peregrine shocked
    peregrine "A what?"

    "What would a person like this understand?"

label peregrine17:
    scene
    $ peregrine_bookmark = "peregrine17"
    show screen basics
    show bg knightroom
    show peregrine neutral
    mc "I'm- I'm like a patron saint."

    mc "Of writing! A patron saint of writing."
    
    mc "Now, please unhand me."

    show peregrine neutral
    "She lets go, and backs up."

label peregrine18:
    scene
    $ peregrine_bookmark = "peregrine18"
    show screen basics
    show bg knightroom
    show peregrine distracted
    peregrine "I'm sorry. That was rude of me."

    show peregrine confused
    peregrine "It's not every day you're visited by a... minor god."

    show peregrine talking
    peregrine "But I'm in desperate straits, my lord."

    mc "Please don't call me that."

label peregrine19:
    scene
    $ peregrine_bookmark = "peregrine19"
    show screen basics
    show bg knightroom

    show peregrine neutral
    peregrine "Alright, my... god"

    show peregrine neutral
    peregrine "If that is what you are, I'll take what help I can get."

    mc "Of course. What seems to be the problem?"

label peregrine191:
    scene
    $ peregrine_bookmark = "peregrine191"
    show screen basics
    show bg knightroom

    show peregrine neutral
    peregrine "I'm a squire, my lord. I've been one for years, and I've always dreamt of being a knight."

    mc "Not another 'my lord'. Please."

    show peregrine smile
    peregrine "All right, all right." 
    
    peregrine "Anyway, I'm apprenticing under one of the king's own and everything."

    show peregrine mad
    peregrine "I was disqualified, on account of my upbringing"

label peregrine192:
    scene
    $ peregrine_bookmark = "peregrine192"
    show screen basics
    show bg knightroom

    show peregrine tired
    peregrine "I just have to write this last letter appealing the decision."

    show peregrine shocked
    peregrine "I may not be from a wealthy family, but that's no reason to disqualify me from the position."
    
    show peregrine mad
    peregrine "So I'm appealing to the order! If they'll just let me in, I can prove how strong I am."

    show peregrine talking
    peregrine "Surely, I can convince them that they're being a bit old-fashioned, going on about good breeding and all that."

    # MENU - TIMES ARE CHANGING FROM NOSTRO

label peregrine1_menu:
    scene
    $ peregrine_bookmark = "peregrine192"
    show screen basics
    show bg knightroom

    show peregrine tired
    peregrine "Honestly, I'm not sure I even should."
    $ wrong_answer_label = "peregrine1_wrong"
    $ right_answer_label = "peregrine1_right"
    $ right_answer = "Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better."
    show screen notebook_menu
    "What should I say?"
    
label peregrine1_wrong: 
    $ ink = ink - 5
    $ check_ink()
    show peregrine confused
    peregrine "What are you saying?"
    jump peregrine1_menu

label peregrine1_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ check_ink()
    $ notebook_items.remove("Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better.")
    show peregrine talking
    peregrine "Exactly! Thank you!"

    jump peregrine2

label peregrine2:
    $ part2 = 2
    scene
    $ peregrine_bookmark = "peregrine2"
    show screen basics
    show bg knightroom

    show peregrine smile
    peregrine "That's just the right way to put it."

    $ notebook_items.add("We have to believe that things can get better.")
    peregrine "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}We have to believe that things can get better.{/b}{/size}{/font}"

    show peregrine mad
    peregrine "We can't just value lineage here."

    peregrine "That's what got the old king killed."

    mc "Naturally."

label peregrine21:
    scene
    $ peregrine_bookmark = "peregrine21"
    show screen basics
    show bg knightroom

    show peregrine neutral
    peregrine "Really, it's like no one learns from their mistakes around here."

    show peregrine mad
    $ notebook_items.add("And I've worked really, really hard to be in this position.")
    peregrine "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}And I've worked really, really hard to be in this position.{/b}{/size}{/font}"

    show peregrine distracted
    peregrine "I left my little brother in the fields for this, after all! And the knights' wages would make sure my family never goes hungry."

    show peregrine smile
    peregrine "And if I can prove my mother wrong about my becoming a knight, that'd just be a little bonus perk for me."

label peregrine2_menu:
    scene
    $ peregrine_bookmark = "peregrine21"
    show screen basics
    show bg knightroom

    show peregrine neutral
    peregrine "I just need to convince them that I'm the right man for the job."
    $ wrong_answer_label = "peregrine2_wrong"
    $ right_answer_label = "peregrine2_right"
    $ right_answer = "You already know you've got the best product in town. You just need your buyers to believe that."
    show screen notebook_menu
    "What should I say?"
    
label peregrine2_wrong: 
    $ ink = ink - 5
    $ check_ink()
    show peregrine confused
    peregrine "What are you saying?"
    jump peregrine2_menu

label peregrine2_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ check_ink()
    $ notebook_items.remove("You already know you've got the best product in town. You just need your buyers to believe that.")
    show peregrine smile
    peregrine "Exactly again!"
    jump peregrine3

label peregrine3:
    $ part2 = 3
    scene
    $ peregrine_bookmark = "peregrine3"
    show screen basics
    show bg knightroom

    show peregrine smile
    peregrine "Maybe you do have powers."

    peregrine "You understand me so well."

    show peregrine tired
    "She jots some notes down on corner of her parchment."

label peregrine31:
    scene
    $ peregrine_bookmark = "peregrine31"
    show screen basics
    show bg knightroom

    show peregrine distracted
    peregrine "Well, most of my thinking."

    peregrine "There's just another tiny issue that I'm worried about."

    mc "The way you put that, it doesn't sound tiny at all."

    show peregrine neutral
    peregrine "Maybe not."

label peregrine32:
    scene
    $ peregrine_bookmark = "peregrine32"
    show screen basics
    show bg knightroom

    show peregrine tired
    peregrine "So, the thing is..."
    
    show peregrine neutral
    peregrine "I'm a girl."

    mc "Yes."

    mc "I can tell."

label peregrine33:
    scene
    $ peregrine_bookmark = "peregrine33"
    show screen basics
    show bg knightroom

    show peregrine mad
    peregrine "What?"

    "She looks down at her garb."

    show peregrine neutral
    peregrine "Oh!"

    show peregrine smile
    peregrine "Okay, I know that's probably obvious to you right now."

label peregrine34:
    scene
    $ peregrine_bookmark = "peregrine34"
    show screen basics
    show bg knightroom

    show peregrine talking
    peregrine "But I swear, I've been passing for a boy quite well!"

    peregrine "I've bound my chest and trained up my strength and lowered my voice and even worked on my movements so they look more boy-like."

    peregrine "I took Peregrine for a boy's name and everything."

    peregrine "It's been very hard work, I'll have you know."

label peregrine35:
    scene
    $ peregrine_bookmark = "peregrine35"
    show screen basics
    show bg knightroom

    show peregrine smile
    $ notebook_items.add("But if I keep pretending, I'm only going to be living someone else's life for the rest of mine.")
    peregrine "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}But if I keep pretending, I'm only going to be living someone else's life for the rest of mine.{/b}{/size}{/font} Peregrine Rolfe, very average boy knight apprentice."
 
    peregrine "Actually, I like the name all right. I think I'll keep that."

    show peregrine talking
    peregrine "But there's just no way I can go on like this!"

    show peregrine shocked
    peregrine "I'm exhausted, and I'm not even living in the knights' castle yet."

label peregrine36:
    scene
    $ peregrine_bookmark = "peregrine36"
    show screen basics
    show bg knightroom

    show peregrine mad
    peregrine "I need them to let me join the king's order, but I only want to do that honestly."

    show peregrine distracted
    peregrine "Otherwise, if they don't let me, I really don't know what I'll do with my life."

    show peregrine tired
    peregrine "And if I keep having to lie, I don't know what I'll do either."

label peregrine3_menu:
    scene
    $ peregrine_bookmark = "peregrine36"
    show screen basics
    show bg knightroom

    show peregrine distracted
    peregrine "Without the knighthood... what will I have?"
    $ wrong_answer_label = "peregrine3_wrong"
    $ right_answer_label = "peregrine3_right"
    $ right_answer = "And I've worked really, really hard to be in this position."
    show screen notebook_menu
    "What should I say?"

label peregrine3_wrong: 
    $ ink = ink - 5
    $ check_ink()
    show peregrine confused
    peregrine "What are you saying?"
    jump peregrine3_menu

label peregrine3_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ check_ink()
    $ notebook_items.remove("And I've worked really, really hard to be in this position.")
    show peregrine smile
    peregrine "Okay, okay, no need to throw my own words back at me!"
    jump peregrine4

label peregrine4:
    $ part2 = 4
    scene
    $ peregrine_bookmark = "peregrine4"
    show screen basics
    show bg knightroom

    show peregrine talking
    peregrine "Although I appreciate the encouragement."

    mc "You've had the determination to make it this far, against your mother's wishes and against all odds."

    mc "I'm sure that strength will take you far, Peregrine. Knighthood or not."

    show peregrine distracted
    peregrine "I sure hope so."

label peregrine41:
    scene
    $ peregrine_bookmark = "peregrine41"
    show screen basics
    show bg knightroom

    show peregrine smile
    peregrine "Huh, I guess I know what to write after all."

    show peregrine talking
    peregrine "Thanks for the help."

    show peregrine distracted
    peregrine "Although now that I think about it, I'm not quite sure if you helped write all that much."

    show peregrine smile
    peregrine "But hey, like I said - I'll take all the help I can get."

label peregrine42:
    scene
    $ peregrine_bookmark = "peregrine42"
    show screen basics
    show bg knightroom

    show peregrine neutral
    peregrine "I'll have to ask you to leave now, though. I need to focus on writing this letter."

    peregrine "Or if you want to stay, that's okay too."

    show peregrine smile
    peregrine "But thank you, seriously!"

    $ peregrine_bookmark = "peregrine43"
    jump call_timelineUI

label peregrine43:
    scene
    show screen basics
    show bg knightroom

    while True:
        show peregrine distracted
        "Peregrine puts her hair into her mouth, realizes what she's doing, and takes it back out."

        show peregrine smile
        "Peregrine gazes out of the window longingly."

        show peregrine confused
        "Peregrine scratches in a word or two, and squints at them to make sure they are spelled right."