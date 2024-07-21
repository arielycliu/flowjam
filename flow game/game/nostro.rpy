define nostro = Character("Nostro")

label nostro1:
    show screen timelineButton
    show screen notebook_display_toggle
    show screen inkbar
    scene bg castle

    "A cold stone room, lit by wall-mounted candles. Flickering coals sit in the untended fireplace."

    "A mortal sits before me at a writing desk, tapping his fingers."

    "He looks up."
    
    nostro "[name]! The esteemed Inksmith themselves! Well, what a sight for sore eyes."

    nostro "Please, please, do make yourself comfortable. My castle has of late been wanting in company. Perhaps all that I need to resolve this quandry is to have a visitor to brighten its halls."

    nostro "I am quite flustered to admit a guest such as yourself to my home when it is in such a sorry state, but I have had to let all the servants go. Their keep simply costs me too much."

    nostro "I cannot remember when I have seen the place this dilapidated. Perhaps never."

    nostro "It behooves my management."

    $ notebook_items.append("Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better.")
    nostro "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better.{/b}{/size}{/font}"

    mc "I see."

    nostro "Yes, yes. I suspect a new owner shall inhabit this place soon enough."

    nostro "Oh, my apologies. We are here to write, are we not?"

    nostro "I have not had company for so long, [name]. You must forgive me for rambling on."

    nostro "The point is: I have, of late, conceived of a concept for a novel I am quite passionate about."

    nostro "A story of star-crossed lovers - a perfectly normal boy and a cannibal girl, who loves him but desires to consume him whole."

    nostro "The story is unique, however, by way of its audience. I hope to write for children in the teen ages, who perhaps believe in their love but are not yet so world-weary."

    nostro "This is my manuscript. I had this meeting scene completely planned out, but I'm afraid it has all gone a tad wrong."

    mc "That idea seems... a bit ahead of its time."

    nostro "Oh, believe me, I understand that it may right well be."

    nostro "But I've an odd feeling that the idea itself will be revolutionary in a hundred years or so."

    nostro "Ah, not that I will be around to see it succeed by that point. Like other mortals, that is not within my lifespan, of course."

    nostro "But it is a nice thought, is it not?"

    nostro "The essential bit of the story, you see, lacks an artistic touch to bring it to life. The meeting of the main lovers."

    nostro "They meet in a university, and the boy falls in love at first sight, while the girl struggles to tamp down her flesh-eating tendencies."

    nostro "Whenever I hope to write the way that he describes her, the words seem to fail me completely. I can neither make head nor tail of it."

    mc "I know the feeling."

    nostro "I knew you would."

    nostro "'If only I could call on [name],' I thought to myself, 'the conundrum could certainly be addressed.'"

label nostro1_menu:
    nostro "So, er, would you perchance have any ideas?"
    define wrong_answer_label = "nostro1_wrong"
    define right_answer_label = "nostro1_right"
    define right_answer = "Her ocean-blue eyes and snow-white hair captured my attention. When she smiled, she was the only person in the room to me."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label nostro1_wrong: 
    $ ink = ink - 5

    nostro "Er, sorry, but I am not really certain how that phrase is helpful in this scenario."
    nostro "Maybe, try again?"

    jump nostro1_menu

label nostro1_right: 
    hide screen notebook_menu
    $ ink = ink - 5

    nostro "Oh, but that is brilliant!"
    jump nostro2

label nostro2:

    nostro "It carries just the right touch of sentimentality for the scene. Of course, the specific adjectives must be transposed, but that conveys just what I would like it to."

    nostro "Oh, I almost feel motivated to uncork one of my vintages. It sounds foolish, but you would be shocked by how long I have been pondering this singular scene."

    nostro "In fact, perhaps an offering would be appropriate. I have troubled you to come visit me, have I not?"

    nostro "I am sure a deity like you can appreciate a good wine."

    mc "Perhaps. I've never had wine, actually."

    mc "But I'm not here for any sort of reward, Nostro. It's very kind of you, but really not necessary."

    nostro "What?"

    nostro "That is simply unacceptable!"

    $ notebook_items.append("a god who has never had wine is like a king who has never seen gold!")
    nostro "Why, {font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}a god who has never had wine is like a king who has never seen gold!{/b}{/size}{/font}"

    nostro "That simply will not do."

    "Nostro whisks two glasses from a nearby cabinet, then two wine bottles. He slides a glass toward me. Uncorking both, he pours with practiced dexterity."
    
    "Such hospitality. Are mortals all so kind?"

    "When I pick up my glass, he clinks his against mine. The liquid inside swirls, the crimson drink in his cup far more opaque. I bring the glass to my lips."

    "It's surprisingly sweet."

    nostro "It is delicious, is it not?"

    "Then, a tingling spreads across my tongue. My face puckers."

    nostro "But it holds an unexpected acidity."

    mc "Yes-"
    
    " - I begin to cough - "
    
    "- it's quite something."

    nostro "Inksmith, you must forgive me for not warning you."

    nostro "Sometimes, I find the unexpected to be the most pleasing."

    nostro "[name], since you are here already - may I ask you another favour?"

    nostro "I do hope I am not taking up too much of your time."

    "Good thing that's not a concern at all."
    
    mc "Oh, do go on."

    nostro "You see, there is yet another plot point I worry about the composition of."

    nostro "At the most climactic moment of the narrative, I hope for an antagonistic cannibal to hunt the boy. However, with the way my manuscript has developed, he has already crept into hiding."

    nostro "He is quite protected while in hiding, but I require that he ventures outside so that he may be captured, and only then can the novel progress."

label nostro2_menu:
    nostro "I could always rewrite the preceding scenes, but I really would rather not if it can be avoided."
    define wrong_answer_label = "nostro2_wrong"
    define right_answer_label = "nostro2_right"
    define right_answer = "lying can always solve problems. Or make things better. Or if not better, more interesting."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label nostro2_wrong: 
    $ ink = ink - 5

    nostro "Er, sorry, but I am not really certain how that phrase is helpful in this scenario."
    jump nostro2_menu

label nostro2_right: 
    hide screen notebook_menu
    $ ink = ink - 5

    nostro "Oh, I suppose that will do."
    jump nostro3

label nostro3:
    nostro "Now that I consider it, it does fit into the trapper's motives."

    nostro "Oh, yes, splendid! It really is all falling into place!"

    nostro "I can see that you are a god for a reason, Inksmith."

    nostro "That's all of the notable obstacles to completing this piece addressed, then. And at long last, I can spy the end of my journey."

    nostro "Well, I claim that it has been long, but I suppose greater authors than I have languished much longer on their writing. I can only aspire to one day be inducted into their ranks."

    mc "There is no need to be so humble. A long time to a mortal may be a blink to us."

    nostro "Oh, you would be surprised, [name]."

    show nostro knowing
    $ notebook_items.append("We mortals can live very long. If not in life, then in spirit.")
    nostro "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}We mortals can live very long. If not in life, then in spirit.{/b}{/size}{/font} And I intend to lead a very long life indeed." 

    nostro "There is such a great deal left to accomplish. I feel as though I am filled to the brim with ideas to share with the world at large."

    nostro "It is difficult to imagine passing away before I have done so."

    $ notebook_items.append("at least I will go to my own death knowing that I have not let my dreams slip idly by.")
    nostro "And in the unlikely case of failure - {font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}at least I will go to my own death knowing that I have not let my dreams slip idly by.{/b}{/size}{/font}"

    mc "Of course. Your ambition is respectable, honestly."

    nostro "..."

    nostro "In truth, I am afraid. I am certainly an unorthodox writer, with unorthodox tastes. You said so yourself, upon hearing my plans for the narrative."

    nostro "My prose is hardly elegant, and as much as one may speak proudly about creation for its own sake, the practice of artistry too strange to be accepted is a lonely path."

    nostro "Ah, perhaps, [name], I must ask you to tell me honestly, although it frightens me to imagine what you may say."

label nostro3_menu:
    nostro "Do you believe my manuscript stands a chance?"
    define wrong_answer_label = "nostro3_wrong"
    define right_answer_label = "nostro3_right"
    define right_answer = ""
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label nostro3_wrong: 
    $ ink = ink - 5

    nostro "Er, sorry, but I am not really certain how that phrase is helpful in this scenario."
    jump nostro3_menu

label nostro3_right: 
    hide screen notebook_menu
    $ ink = ink - 5

    nostro "Ah. I understand."
    jump nostro3andahalf

label nostro3andahalf:
    nostro "You cannot imagine how much it means to me to hear you say so, [name]. I do not know what sort of relationship you have had with your worshippers, but I hold your opinion in the highest esteem."

    nostro "That is all that I needed your support with, but know that your instruction has been indescribably helpful."

    nostro "I will let you go for now, then. I am certain that you have wealths of followers who do still require that same instruction."

    nostro "Do not take that to mean that I have dismissed you from my presence, of course. Please, feel free to sit here as long as you wish. My home is yours, Inksmith."

    hide nostro

label nostro4:
    # so that from now on, every time you jump back to Nostro, he's writing
    while True:
        "Nostro is writing with fervour - his pen scratches so quickly it threatens to shred the paper."

        "Nostro is tapping his fingers, deep in thought. An ink smudge stains his fingertips."

        "Nostro takes a sip from his blood-red wine glass."





    