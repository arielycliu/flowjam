define nostro = Character("Nostro")

label nostro1:
    $ part3 = 1
    scene
    $ nostro_bookmark = "nostro1"
    show screen basics
    show bg castle

    "A warm wood built room, lit by wall-mounted candles. Flickering coals sit in the untended fireplace."

    "A mortal sits before me at a writing desk, tapping his fingers."

    "He looks up."

label nostro11:
    scene
    $ nostro_bookmark = "nostro11"
    show screen basics
    show bg castle

    show nostro knowing
    nostro "[name]! The esteemed Inksmith themselves! Well, what a sight for sore eyes."

    show nostro veryhappy
    nostro "Please, please, do make yourself comfortable. My castle has of late been wanting in company. Perhaps all that I need to resolve this quandry is to have a visitor to brighten its halls."

    show nostro smile
    nostro "I am quite flustered to admit a guest such as yourself to my home when it is in such a sorry state, but I have had to let all the servants go. Their keep simply costs me too much."

    show nostro neutral
    nostro "I cannot remember when I have seen the place this dilapidated. Perhaps never."

label nostro12:
    scene
    $ nostro_bookmark = "nostro12"
    show screen basics
    show bg castle

    show nostro angry
    nostro "It behooves my management."

    $ notebook_items.add("Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better.")
    nostro "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better.{/b}{/size}{/font}"

    mc "I see."

    show nostro sigh
    nostro "Yes, yes. I suspect a new owner shall inhabit this place soon enough."

label nostro13:
    scene
    $ nostro_bookmark = "nostro13"
    show screen basics
    show bg castle

    show nostro happy
    nostro "Oh, my apologies. We are here to write, are we not?"

    nostro "I have not had company for so long, [name]. You must forgive me for rambling on."

    show nostro sigh
    nostro "The point is: I have, of late, conceived of a concept for a novel I am quite passionate about."

    show nostro happy
    nostro "A story of star-crossed lovers - a perfectly normal boy and a cannibal girl, who loves him but desires to consume him whole."

label nostro14:
    scene
    $ nostro_bookmark = "nostro14"
    show screen basics
    show bg castle

    show nostro neutral
    nostro "The story is unique, however, by way of its audience. I hope to write for children in the teen ages, who perhaps believe in their love but are not yet so world-weary."

    show nostro worried
    nostro "This is my manuscript. I had this meeting scene completely planned out, but I'm afraid it has all gone a tad wrong."

    mc "That idea seems... a bit ahead of its time."

    show nostro smile
    nostro "Oh, believe me, I understand that it may right well be."

    nostro "But I've an odd feeling that the idea itself will be revolutionary in a hundred years or so."

label nostro15:
    scene
    $ nostro_bookmark = "nostro15"
    show screen basics
    show bg castle

    show nostro sigh
    nostro "Ah, not that I will be around to see it succeed by that point. Like other mortals, that is not within my lifespan, of course."

    show nostro smile
    nostro "But it is a nice thought, is it not?"

    show nostro worried
    nostro "The essential bit of the story, you see, lacks an artistic touch to bring it to life. The meeting of the main lovers."

    nostro "They meet in a university, and the boy falls in love at first sight, while the girl struggles to tamp down her flesh-eating tendencies."

label nostro16:
    scene
    $ nostro_bookmark = "nostro16"
    show screen basics
    show bg castle

    show nostro angry
    nostro "Whenever I hope to write the way that he describes her, the words seem to fail me completely. I can neither make head nor tail of it."

    mc "I know the feeling."

    show nostro knowing
    nostro "I knew you would."

    nostro "'If only I could call on [name],' I thought to myself, 'the conundrum could certainly be addressed.'"

label nostro1_menu:
    scene
    $ nostro_bookmark = "nostro1_menu"
    show screen basics
    show bg castle

    show nostro worried
    nostro "So, er, would you perchance have any ideas?"
    $ wrong_answer_label = "nostro1_wrong"
    $ right_answer_label = "nostro1_right"
    $ right_answer = "Her ocean-blue eyes and snow-white hair captured my attention. When she smiled, she was the only person in the room to me."
    show screen notebook_menu
    "What should I say?"
    
label nostro1_wrong: 
    $ ink = ink - 5

    show nostro worried
    nostro "Er, sorry, but I am not really certain how that phrase is helpful in this scenario."
    jump nostro1_menu

label nostro1_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ notebook_items.remove("Her ocean-blue eyes and snow-white hair captured my attention. When she smiled, she was the only person in the room to me.")

    show nostro happy
    nostro "Oh, but that is brilliant!"
    jump nostro2

label nostro2:
    $ part3 = 2
    scene
    $ nostro_bookmark = "nostro2"
    show screen basics
    show bg castle

    show nostro knowing
    nostro "It carries just the right touch of sentimentality for the scene. Of course, the specific adjectives must be transposed, but that conveys just what I would like it to."

    show nostro veryhappy
    nostro "Oh, I almost feel motivated to uncork one of my vintages. It sounds foolish, but you would be shocked by how long I have been pondering this singular scene."

    show nostro worried
    nostro "In fact, perhaps an offering would be appropriate. I have troubled you to come visit me, have I not?"

    show nostro knowing
    nostro "I am sure a deity like you can appreciate a good wine."

label nostro21:
    scene
    $ nostro_bookmark = "nostro21"
    show screen basics
    show bg castle

    show nostro knowing
    mc "Perhaps. I've never had wine, actually."

    mc "But I'm not here for any sort of reward, Nostro. It's very kind of you, but really not necessary."

    show nostro worried
    nostro "What?"

    show nostro angry
    nostro "That is simply unacceptable!"

label nostro22:
    scene
    $ nostro_bookmark = "nostro22"
    show screen basics
    show bg castle

    show nostro sigh
    $ notebook_items.add("a god who has never had wine is like a king who has never seen gold!")
    nostro "Why, {font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}a god who has never had wine is like a king who has never seen gold!{/b}{/size}{/font}"

    nostro "That simply will not do."

    show nostro knowing
    "Nostro whisks two glasses from a nearby cabinet, then two wine bottles. He slides a glass toward me. Uncorking both, he pours with practiced dexterity."
    
    "Such hospitality. Are mortals all so kind?"

label nostro23:
    scene
    $ nostro_bookmark = "nostro23"
    show screen basics
    show bg castle

    show nostro knowing
    "When I pick up my glass, he clinks his against mine. The liquid inside swirls, the crimson drink in his cup far more opaque. I bring the glass to my lips."

    "It's surprisingly sweet."

    show nostro happy
    nostro "It is delicious, is it not?"

    "Then, a tingling spreads across my tongue. My face puckers."

label nostro24:
    scene
    $ nostro_bookmark = "nostro24"
    show screen basics
    show bg castle

    show nostro veryhappy
    nostro "But it holds an unexpected acidity."

    mc "Yes-"
    
    " - I begin to cough - "
    
    "- it's quite something."

label nostro25:
    scene
    $ nostro_bookmark = "nostro25"
    show screen basics
    show bg castle

    show nostro happy
    nostro "Inksmith, you must forgive me for not warning you."

    show nostro veryhappy
    $ notebook_items.add("Sometimes, I find the unexpected to be the most pleasing.")
    nostro "{font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}Sometimes, I find the unexpected to be the most pleasing.{font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}"

    show nostro worried
    nostro "[name], since you are here already - may I ask you another favour?"

label nostro26:
    scene
    $ nostro_bookmark = "nostro26"
    show screen basics
    show bg castle

    show nostro worried
    nostro "I do hope I am not taking up too much of your time."

    "Good thing that's not a concern at all."
    
    mc "Oh, do go on."

label nostro27:
    scene
    $ nostro_bookmark = "nostro27"
    show screen basics
    show bg castle

    show nostro sigh
    nostro "You see, there is yet another plot point I worry about the composition of."

    show nostro worried
    nostro "At the most climactic moment of the narrative, I hope for an antagonistic cannibal to hunt the boy. However, with the way my manuscript has developed, he has already crept into hiding."

    show nostro neutral
    nostro "He is quite protected while in hiding, but I require that he ventures outside so that he may be captured, and only then can the novel progress."

label nostro2_menu:
    scene
    $ nostro_bookmark = "nostro2_menu"
    show screen basics
    show bg castle

    show nostro worried
    nostro "I could always rewrite the preceding scenes, but I really would rather not if it can be avoided."
    $ wrong_answer_label = "nostro2_wrong"
    $ right_answer_label = "nostro2_right"
    $ right_answer = "lying can always solve problems. Or make things better. Or if not better, more interesting."
    show screen notebook_menu
    "What should I say?"

label nostro2_wrong: 
    $ ink = ink - 5

    show nostro neutral
    nostro "Er, sorry, but I am not really certain how that phrase is helpful in this scenario."
    jump nostro2_menu

label nostro2_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ notebook_items.remove("lying can always solve problems. Or make things better. Or if not better, more interesting.")

    show nostro happy
    nostro "Oh, I suppose that will do."
    jump nostro3

label nostro3:
    $ part3 = 3
    scene
    $ nostro_bookmark = "nostro3"
    show screen basics
    show bg castle

    show nostro veryhappy
    nostro "Now that I consider it, it does fit into the trapper's motives."

    show nostro sigh
    nostro "Oh, yes, splendid! It really is all falling into place!"

    show nostro knowing
    nostro "I can see that you are a god for a reason, Inksmith."

label nostro31:
    scene
    $ nostro_bookmark = "nostro31"
    show screen basics
    show bg castle

    show nostro happy
    nostro "That's all of the notable obstacles to completing this piece addressed, then. And at long last, I can spy the end of my journey."

    show nostro knowing
    nostro "Well, I claim that it has been long, but I suppose greater authors than I have languished much longer on their writing. I can only aspire to one day be inducted into their ranks."

    mc "There is no need to be so humble. A long time to a mortal may be a blink to us."

    show nostro smile
    nostro "Oh, you would be surprised, [name]."

label nostro32:
    scene
    $ nostro_bookmark = "nostro32"
    show screen basics
    show bg castle

    show nostro knowing
    $ notebook_items.add("We mortals can live very long. If not in life, then in spirit.")
    nostro "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}We mortals can live very long. If not in life, then in spirit.{/b}{/size}{/font} And I intend to lead a very long life indeed." 

    show nostro happy
    nostro "There is such a great deal left to accomplish. I feel as though I am filled to the brim with ideas to share with the world at large."

    show nostro worried
    nostro "It is difficult to imagine passing away before I have done so."

    show nostro veryhappy
    $ notebook_items.add("at least I will go to my own death knowing that I have not let my dreams slip idly by.")
    nostro "And in the unlikely case of failure - {font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}at least I will go to my own death knowing that I have not let my dreams slip idly by.{/b}{/size}{/font}"

label nostro33:
    scene
    $ nostro_bookmark = "nostro33"
    show screen basics
    show bg castle

    show nostro veryhappy
    mc "Of course. Your ambition is respectable, honestly."

    show nostro worried
    nostro "In truth, I am afraid. I am certainly an unorthodox writer, with unorthodox tastes. You said so yourself, upon hearing my plans for the narrative."

    nostro "My prose is hardly elegant, and as much as one may speak proudly about creation for its own sake, the practice of artistry too strange to be accepted is a lonely path."

    nostro "Ah, perhaps, [name], I must ask you to tell me honestly, although it frightens me to imagine what you may say."

label nostro3_menu:
    scene
    $ nostro_bookmark = "nostro3_menu"
    show screen basics
    show bg castle

    show nostro angry
    nostro "Do you believe my manuscript stands a chance?"
    $ wrong_answer_label = "nostro3_wrong"
    $ right_answer_label = "nostro3_right"
    $ right_answer = "We've been working so hard to make things appealing to everyone, we haven't stopped to wonder if we should."
    show screen notebook_menu
    "What should I say?"

label nostro3_wrong: 
    $ ink = ink - 5

    show nostro worried
    nostro "Er, sorry, but I am not really certain how that phrase is helpful in this scenario."
    jump nostro3_menu

label nostro3_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ notebook_items.remove("We've been working so hard to make things appealing to everyone, we haven't stopped to wonder if we should.")

    show nostro happy
    nostro "Ah. I understand."
    jump nostro41

label nostro41:
    $ part3 = 4
    scene
    $ nostro_bookmark = "nostro41"
    show screen basics
    show bg castle
    
    show nostro veryhappy
    nostro "You cannot imagine how much it means to me to hear you say so, [name]. I do not know what sort of relationship you have had with your worshippers, but I hold your opinion in the highest esteem."

    show nostro smile
    nostro "That is all that I needed your support with, but know that your instruction has been indescribably helpful."

    nostro "I will let you go for now, then. I am certain that you have wealths of followers who do still require that same instruction."

    show nostro sigh
    nostro "Do not take that to mean that I have dismissed you from my presence, of course. Please, feel free to sit here as long as you wish. My home is yours, Inksmith."

label nostro42:
    scene
    $ nostro_bookmark = "nostro42"
    show screen basics
    show bg castle

    # so that from now on, every time you jump back to Nostro, he's writing
    while True:
        show nostro angry
        "Nostro is writing with fervour - his pen scratches so quickly it threatens to shred the paper."

        show nostro worried
        "Nostro is tapping his fingers, deep in thought. An ink smudge stains his fingertips."

        show nostro veryhappy
        "Nostro takes a sip from his blood-red wine glass."





    