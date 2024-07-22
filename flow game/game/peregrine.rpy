transform stretch_to_fill:
    xysize (config.screen_width, config.screen_height)

define peregrine = Character("Peregrine")

label peregrine1:
    scene bg commonroom at stretch_to_fill zorder 0
    "A mortal kneels against a wall in a squire's lodgings, quill set to parchment."

    "Her tongue is sticking slightly out of her mouth, and she hums a simple line of plainsong under her breath."

    "..."

    "I don't think she's going to notice me."

    "Overcoming my hesitation, I walk up and gently tap her on the shoulder."

    show peregrine mad
    "She whirls around with a swiftness that can only be born through combat."

    "She slams me against the wall, blade in hand."

    "Even knowing I cannot be killed, I feel a pinprick of fear."

    "Can mortals hurt us?"

    "Shouldn't Elias have mentioned this?"

    "Maybe they did? They did mention quite a lot of details."

    mc "Peregrine-!"

    show peregrine shocked
    peregrine "Who are you? How did you get in here?"

    peregrine "How do you know my name?"

    mc "I-"

    mc "You called for me!"

    peregrine "What?"

    show peregrine mad
    mc "You wanted help with writing something, yes?"

    mc "That's what I'm here for."

    mc "I'm a minor god."

    peregrine "A what?"

    "What would a person like this understand?"

    mc "I'm- I'm like a patron saint."

    mc "Of writing! A patron saint of writing."
    
    mc "Now, please unhand me."

    show peregrine neutral
    "She lets go, and backs up."

    peregrine "I'm sorry. That was rude of me."

    show peregrine confused
    peregrine "It's not every day you're visited by a... minor god."

    peregrine "But I'm in desperate straits, my lord."

    mc "Please don't call me that."
    
    show peregrine neutral
    peregrine "If that is what you are, I'll take what help I can get."

    "That's all I wanted."

    mc "Of course. What seems to be the problem?"

    peregrine "I'm a squire, my lord. I've been one for years, and I've always dreamt of being a knight."

    mc "Not another 'my lord'. Please."

    peregrine "All right, all right." 
    
    peregrine "Anyway, I'm apprenticing under one of the king's own and everything."

    peregrine "I just have to write this last letter."

    show peregrine distracted
    peregrine "I may not be from a wealthy family, but that's no reason to disqualify me from the position."
    
    peregrine "So I'm appealing to the order! If they'll just let me in, I can prove how strong I am."

    peregrine "Surely, I can convince them that they're being a bit old-fashioned, going on about good breeding and all that."

    # MENU - TIMES ARE CHANGING FROM NOSTRO

label peregrine1_menu:
    show peregrine bored
    peregrine "Honestly, I'm not sure I even should."
    define wrong_answer_label = "peregrine1_wrong"
    define right_answer_label = "peregrine1_right"
    define right_answer = "Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label peregrine1_wrong: 
    $ ink = ink - 5
    show peregrine confused
    peregrine "What are you saying?"
    jump peregrine1_menu

label peregrine1_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    show peregrine talking
    peregrine "Exactly! Thank you!"

    jump peregrine2

label peregrine2:
    show peregrine smile
    peregrine "That's just the right way to put it."

    show peregrine mad
    peregrine "We can't just value lineage here."

    peregrine "That's what got the old king killed."

    mc "Naturally."

    show peregrin neutral
    peregrine "Really, it's like no one learns from their mistakes around here."

    $ notebook_items.append("And I've worked really, really hard to be in this position.")
    peregrine "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}And I've worked really, really hard to be in this position.{/b}{/size}{/font}"

    peregrine "I left my little brother in the fields for this, after all! And the knights' wages would make sure my family never goes hungry."

    show peregrine smile
    peregrine "And if I can prove my mother wrong about my becoming a knight, that'd just be a little bonus perk for me."

label peregrine2_menu:
    show peregrine neutral
    peregrine "I just need to convince them that I'm the right man for the job."
    define wrong_answer_label = "peregrine2_wrong"
    define right_answer_label = "peregrine2_right"
    define right_answer = "You already know you've got the best product in town. You just need your buyers to believe that."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label peregrine2_wrong: 
    $ ink = ink - 5
    show peregrine confused
    peregrine "What are you saying?"
    jump peregrine2_menu

label peregrine2_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    show peregrine smile
    peregrine "Exactly again!"
    jump peregrine3

label peregrine3:
    peregrine "Maybe you do have powers."

    peregrine "You understand me so well."

    "She jots some notes down on corner of her parchment."

    show peregrine distracted
    peregrine "Well, most of my thinking."

    peregrine "There's just another tiny issue that I'm worried about."

    mc "The way you put that, it doesn't sound tiny at all."

    peregrine "Maybe not."

    show peregrine tired
    peregrine "So, the thing is..."
    
    show peregrine neutral
    peregrine "I'm a girl."

    mc "Yes."

    mc "I can tell."

    show peregrine mad
    peregrine "What?"

    "She looks down at her garb."

    show peregrine neutral
    peregrine "Oh!"

    peregrine "Okay, I know that's probably obvious to you right now."

    show peregrine talking
    peregrine "But I swear, I've been passing for a boy quite well!"

    peregrine "I've bound my chest and trained up my strength and lowered my voice and even worked on my movements so they look more boy-like."

    peregrine "I took Peregrine for a boy's name and everything."

    peregrine "It's been very hard work, I'll have you know."

    show peregrine neutral
    $ notebook_items.append("But if I keep pretending, I'm only going to be living someone else's life for the rest of mine.")
    peregrine "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}But if I keep pretending, I'm only going to be living someone else's life for the rest of mine.{/b}{/size}{/font} Peregrine Rolfe, very average boy knight apprentice."
 
    peregrine "Actually, I like the name all right. I think I'll keep that."

    peregrine "But there's just no way I can go on like this!"

    peregrine "I'm exhausted, and I'm not even living in the knights' castle yet."

    peregrine "I need them to let me join the king's order, but I only want to do that honestly."

    show peregrine distracted
    peregrine "Otherwise, if they don't let me, I really don't know what I'll do with my life."

    peregrine "And if I keep having to lie, I don't know what I'll do either."


label peregrine3_menu:
    peregrine "Without the knighthood... what will I have?"
    define wrong_answer_label = "peregrine3_wrong"
    define right_answer_label = "peregrine3_right"
    define right_answer = "And I've worked really, really hard to be in this position."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label peregrine3_wrong: 
    $ ink = ink - 5
    show peregrine confused
    peregrine "What are you saying?"
    jump peregrine3_menu

label peregrine3_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    show peregrine smile
    peregrine "Okay, okay, no need to throw my own words back at me!"
    jump peregrine3andahalf

label peregrine3andahalf:
    peregrine "Although I appreciate the encouragement."

    mc "You've had the determination to make it this far, against your mother's wishes and against all odds."

    mc "I'm sure that strength will take you far, Peregrine. Knighthood or not."

    peregrine "I sure hope so."

    show peregrine distracted
    peregrine "Huh, I guess I know what to write after all."

    show peregrine smile
    peregrine "Thanks for the help."

    show peregrine talking
    peregrine "Although now that I think about it, I'm not quite sure if you helped write all that much."

    peregrine "But hey, like I said - I'll take all the help I can get."

    show peregrine neutral
    peregrine "I'll have to ask you to leave now, though. I need to focus on writing this letter."

    peregrine "Or if you want to stay, that's okay too."

    peregrine "But thank you, seriously!"

label peregrine4:
    while True:
        "Peregrine puts her hair into her mouth, realizes what she's doing, and takes it back out."

        "Peregrine gazes out of the window longingly."

        "Peregrine scratches in a word or two, and squints at them to make sure they are spelled right."