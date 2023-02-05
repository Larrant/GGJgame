define config.rollback_enabled = False

define p = Character("...")
define a = Character ("Axel", color="#A020F0")
define u = Character("That Person", color="#A020F0")

#VARIABLES#

default ticktock = 0
default funky = 0
default havepostcard = False
default havemarker = False
default havename = False

default calendarink = False
default pamphletink = False

default bikeS2 = False
default calendarS1 = False
default calendarS2 = False
default cameraS1 = False
default cameraS2 = False
default clockS1 = False
default clockS2 = False
default notebookS1 = False
default notebookS2 = False
default pamphletS1 = False
default pamphletS2 = False
default photographS1 = False
default photographS2 = False
default remembranceS1 = False
default remembranceS2 = False

#PERSISTENT VARIABLES#

init -1 python:
    if not persistent.end1:
        persistent.end1 = False
    if not persistent.end2:
        persistent.end2 = False
    if not persistent.end3:
        persistent.end3 = False

init:
    $ flash = Fade(.25, 0, .75, color="#fff")

#IMAGES#

image bg white = "#fff"
image bg black = "#000"
image bg room = im.FactorScale("mainroom.jpg", 1.2)
image ending1 = "ending1.png"
image ending2 = "ending2.png"
image ending3 = "ending3.png"

#SFX#

define cityscape = "audio/sfx/name.mp3"
define keyjangle = "audio/sfx/name.mp3"

label start:
    scene bg black
    $ renpy.pause(0.8, hard=False)
    show text "I arrive home in a hurry." at truecenter
    with dissolve
    pause
    hide text
    with dissolve
    $ renpy.pause(0.3, hard=False)
    show text "The ring of keys jostle in my palm. Work key, {w}downstairs gate key, {w}an old studio key—{i}why do I still have that{/i}—{w}the key to the main apartment—" at truecenter
    with dissolve
    pause
    hide text
    with dissolve
    $ renpy.pause(0.3, hard=False)
    show text "My room key." at truecenter
    with dissolve
    pause
    hide text
    with dissolve
    $ renpy.pause(0.3, hard=False)
    show text "I unlock the door. I enter my house. {w}I shut the door behind me." at truecenter
    with dissolve
    pause
    hide text
    with dissolve
    scene bg room
    "For a moment, everything is blank noise."
    "What am I doing."
    "The fan groans as I switch it on."
    "That's right. {w}I need to find them."
    "I need to hurry and find {glitch=59.94}them{/glitch}."
    $ renpy.pause(0.5, hard=False)
    if persistent.axelend:
            scene bg memory
            with flash
            p "..."
            p "What use is remembering. {w}If it's just a memory you can't bring back, maybe it's better to forget."
            u "{i}Is that really what you think?{/i}"
            p "..."
            p "I don't know."
            $ renpy.pause(0.5, hard=False)
            window hide
            with flash
    jump mainroom

label mainroom:
    scene bg black
    if funky == 1:
        $ renpy.pause(1, hard=False)
        "My head hurts."
        "I need to hurry."
        "I need to find them."
        $ renpy.pause(1, hard=False)
        window hide
    if funky == 2:
        $ renpy.pause(1, hard=False)
        "The sun's going to set soon."
        "On my way back, I tried to call them."
        "No. I wanted to call them."
        "I didn't know how to try."
        "I checked my phone, I scrolled down all my contacts. But none of them seemed right. {w}I don't think I saved them to my contacts list."
        "I checked all the calls I'd made this month, but there were too many. I had a feeling—"
        "I wouldn't recognise their number anyway."
        $ renpy.pause(1, hard=False)
        window hide
    if funky == 3:
        $ renpy.pause(1, hard=False)
        "It's meant to be painless, {w}but my head hurts anyway."
        $ renpy.pause(1, hard=False)
        window hide
    if ticktock == 4:
        $ renpy.pause(1, hard=False)
        "The sun is setting. {w}It's beautiful, though it doesn't reach the inside of my room well."
        "At one of my old jobs, I used to be able to look out of the service window and skim over the buildings to reach the mountains."
        "The sun would set orange at around seven in summer, and a pinkish glow would gather at my feet. {w}Always felt sort of melancholy, that."
        "Maybe it was how soft everything got, when the sun pastelled the walls of apartment blocks and sidewalks. {w}Felt like you were in a softer world, {w}a world half out of a dream."
        "A city both familiar and not."
        "I look away from the sliver of twilight through the blinds."
        p "Right. I still have to find them."
        "Even if I have a feeling...{w}it's getting too late."
        $ renpy.pause(1, hard=False)
        window hide
    if funky == 5:
        $ renpy.pause(1, hard=False)
        "funky: 5."
        $ renpy.pause(1, hard=False)
        window hide
    if ticktock == 7:
        $ renpy.pause(1, hard=False)
        "..."
        $ renpy.pause(1, hard=False)
        window hide
    if ticktock == 8:
        jump end1
    scene bg room
    $ renpy.pause(0.5, hard=False)
    menu():
        "Bike":
            jump bike
        "Calendar":
            jump calendar
        "Camera":
            jump camerascene
        "Clock":
            jump clock
        "Notebook":
            jump notebook
        "Pamphlet":
            jump pamphlet
        "Photographs":
            jump photograph
return

label bike:
    #bike stage 1
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        "My bike. Rusted. Spokes fallen off. The paint all peeling. {w}I used to use this to make deliveries."
        "It's not important right now."
        jump mainroom
    #bike stage 2
    if ticktock in range(4, 7):
        $ funky += 1
        "."
        jump mainroom

label calendar:
    #missing stage 2 new old, stage 3 new old
    #calendar stage 1
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        if calendarS1 == False:
            $ ticktock += 1
            $ calendarS1 = True
            "I move to the calendar."
            "I've marked most of the boxes on the page. January 1st. January 5th."
            "January 6th through to 15th. Etc. {w}Restaurant shifts in green, delivery shifts in blue—and then in red, because the blue marker ran out."
            "Is what I'm looking for here?"
            "There's a square I've marked in black. {w}January 21st."
            "I don't know what that means. But there's a smear of purple ink below it, glittering."
            $ calendarink = True
            "It's not from a marker. No, somehow, somehow I'm sure—{w}I'm sure it's theirs."
            "That's right, they were here. {w}They must have been here."
            "Not long ago, they were in this room and they had written something in this calendar."
            "Maybe they weren't careful enough, maybe it's gone already. {w}Just the {glitch=59.94}smear{/glitch} now, just the trail of {glitch=59.94}ink{/glitch}."
            "But as I reach out to touch this proof of life, it {glitch=59.94}goes like—{/glitch}"
            "And then—"
            "{glitch=59.94}And then—{/glitch}"
            if pamphletink == True:
                jump remembrance1
            "My thumb is pressed to the calendar. {w}Right below the square that's January 21st."
            "I've marked it in black."
            "I think I knew what it meant, only a few days ago. {w}But I don't know what it means any more."
            "There's that familiar emptiness as I lift my hand from the page."
            "Like something has been poured out, but the absence only lasts a moment. {w}It fills itself back in."
            "I fumble for a marker before I forget I've forgotten anything at all."
            "I underline January 21st in black. {w}And then for good measure, I write the date across the bottom of the calendar in broad, sweeping strokes."
            "10 + 10 + 1. {w}1."
            "That's probably fine, right? {w}After a moment, I write the date in English too."
            "I must have done something on the 21st. {w}I must have written it into this calendar. {w}Maybe it was still there a moment ago."
            "It's too late now."
            "I have to trust I've already written it down somewhere else. {w}I have to trust I used different words for it."
            "I have to trust that I can find it now."
            p "..."
            "After a moment, I turn away."
            "I think I'll hold onto the marker for now."
            $ havemarker = True
            jump mainroom
        else:
            "I move to the calendar."
            "Right, I was just here. I've marked and underlined January 21st, {w}so I know it's an important date."
            "And I have a gut feeling it's connected to {i}them{/i}."
            "I'll have to keep an eye out for anything marked with this date."
            jump mainroom
    if ticktock in range(4, 7):
        if funky in range(4, 7):
            $ funky += 1
        if calendarS2 == False:
            $ ticktock += 1
            $ calendarS2 = True
            "I move to the calendar."
            if calendarS1 == True:
                "The black marker I used to underline January 21 is still there. {w}That's good."
            "Back in December they were handing these out at the shop downstairs."
            "There's a neatly printed logo on the lower right. SPP."
            "{i}Social Progressive Party{i}. There's a politician in portrait next to it, shiny from makeup and smiling at the camera. {w}An indistinct figure swims into my mind's eye, a handsome guy with a scalp verging on male pattern baldness at thirty."
            "What was his name again? {w}Nevermind. But I think I ended up writing my name and ID to get this one."
            "The price we pay for free calendars, huh. {w}At least I got a sack of rice with it."
            "I frown."
            p "What was I looking for."
            p "Oh. It's February already."
            "I take the calendar down to turn the page to February."
            "As I hang it up again, a slip of paper slides out from between the heavy pages and flutters to the floor."
            jump mainroom
        else:
            "I move to the calendar."
            "Right, I was just here."
            jump mainroom
    if ticktock in range(7, 10):
        "."
        jump mainroom

label camerascene:
    #camera stage 1
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        if cameraS1 == False:
            $ ticktock += 1
            $ cameraS1 = True
            $ renpy.pause(0.5, hard=False)
            "I pick up my camera."
            "It's pretty old. {w}Uses a CF card, it's that old. {w}I got it from a friend who'd lost interest in photography."
            "He spent a week teaching me the basics. {w}Not even composition, just how to change the settings."
            "Otherwise I kept shooting pictures so underexposed the whole photograph was just black."
            "When all that...{w}started, ages ago, it was good to have a camera on hand. {w}The older the better."
            "Maybe that's just my superstition. {w}That old things aren't touched."
            "So I've never connected this camera anywhere. {w}I've never even taken out the card."
            "Maybe something inside will help me remember."
            "I check the memory card slot before turning it on. {w}The screen is dull, and cracks web up from the corner. {w}It's reassuring."
            "But when I navigate to the gallery..."
            "There aren't any pictures."
            "There's nothing at all."
            "I turn it off and check the card slot again."
            p "It's in."
            p "..."
            "That can't be right. {w}I don't have another CF card, and I wouldn't have deleted anything."
            menu():
                "Turn it on again.":
                    $ renpy.pause(0.5, hard=False)
                    "I'll try again. {w}I take out the card and reinsert it. {w}Then I switch the camera back on."
                    p "..."
                    "Still nothing."
                    "I navigate to the settings and back again."
                    "Maybe I should just accept it? {w}But that can't be, because I've always—{w}I've always been careful with this camera."
                    "I can't have taken anything that bad with it."
                    "I wouldn't have. {w}I wouldn't have."
                    p "So why is it gone."
                    "My voice sounds strange. {w}I don't like that."
                    p "..."
                    "I navigate to the settings."
                    "It's all in English, letters neatly printed across the screen."
                    "I scroll down. {w}Aimlessly."
                    "If I take the CF card out now, I can probably take it to a friend to restore. {w}Right?"
                    "As long as I don't take any other pictures."
                    p "..."
                    "But if the data is still on the card, maybe taking it to someone else will make it worse."
                    "If the data is still on the card. {w}If the data is really—somehow—wrong. {w}If not connecting the data anywhere had kept it safe after all."
                    "Kept it safe until now, at least."
                    p "..."
                    p "..."
                    "Somehow, I've navigated to the copyright information screen."
                    p "..."
                    p "Wait."
                    p "That's..."
                    "On the row where the photographer's signature goes, there's a name. {w}Only it's not my name."
                    "{i}Axel T.S Fung{/i}."
                    p "..."
                    "The recognition, or—{w}rather—{w}the non-recognition, is tasteless."
                    "Is that the name of the friend who gave me this camera?"
                    "Did I forget that too?"
                    if havepostcard == True:
                        "And—{w}I reach into my pocket and a corner of plasticky cardstock pricks my finger."
                        "{i}'A—'{/i}."
                    "Is that the person I'm trying to find?"
                    "But there's no contact information on the rest of the page."
                    "Unsettled, I scroll down the rest of the options, hunting for more information. {w}When none is forthcoming, I hesitate before turning the camera off."
                    "{i}Axel{/i}."
                    $ havename = True
                "Take out the card.":
                    $ renpy.pause(0.5, hard=False)
                    "I take out the CF card, turning it over in my hand."
                    "Nothing looks wrong with it, but...{w}it's pretty old and if it's an internal problem with the magnet, I would never know."
                    "I don't remember the last time I took a photograph with this thing."
                    "A few months ago, probably."
                    "Is it possible I was the one who deleted the pictures, and then forgot?"
                    p "..."
                    "I reinsert the card. After a moment, I try turning the camera on again."
                    "The screen stays black."
                    "Don't tell me I just broke it."
                    "For a moment I just stare at the screen. {w}My fingers are a bit white, I guess I must be gripping it pretty tightly."
                    "This isn't helping."
                    p "This always happens, just charge it."
                    "Right. {w}That's right. {w}Sometimes it gets like this, I knock it the wrong way and it just goes from full battery to nothing."
                    "I find a cable and plug it in to charge."
                    "It'll be fine."
                    "Maybe after the battery's back, the pictures will be too."
                    "..."
            jump mainroom
        else:
            $ renpy.pause(0.5, hard=False)
            "No, I've just looked at that."
            jump mainroom
    #camera stage 2
    if ticktock in range(4, 7):
        if funky in range(4, 7):
            $ funky += 1
        if cameraS2 == False:
            $ ticktock += 1
            $ cameraS2 = True
            "I go to check on my camera."
            if cameraS1 == True and havename == False:
                "I haven't charged it for very long and when I try to turn it on, it doesn't react."
                p "..."
                p "You'd better not be broken."
            if cameraS1 == False:
                "It's pretty old, like, a DSLR from two decades ago. {w}I try to turn it on, but for some reason it doesn't react. The screen stays black."
            if havename == True:
                "I try to turn the camera on again, but this time I guess it's out of battery: it stays pretty dead in my grasp."
            p "..."
            "It always gets like this, this thing loses battery like it's trying to compete with a racehorse for crossing the finishing line. {w}I'd better just let it charge."
            if remembranceS1 == True:
                $ remembranceS2 = True
                "Mouth tight, I run my thumb over the hard shell covering the lens."
                "Will the pictures I've taken be there the next time I turn this camera on?"
                p "...Axel."
                "They used to talk about how to make something permanent."
                "They used to say physical matter was a kind of proof, and matter which was permanent was a kind of truth. A true truth."
                "Say, down to the very base level of existence: the configuration of atoms."
                p "Well...these days, even science would disagree with that."
                "They were always scientific about this belief in truth. But romantically."
                "If the erasure of the present reached back to erase the very past which created it, there would still be something left behind. {w}There had to be."
                "An invisible palimpsest, they said. {w}Time and again written and drawn over, but always there. Always existant."
                "I thought it didn't matter. {w}If the eye couldn't see it, and if the hand could not return what had been erased...wasn't it just gone for good?"
                scene bg memory
                a "But it's not like that with this city, is it?"
                a "All this uprooting, it doesn't reach far enough into the past. {w}We've still got graffiti carved into the subway walls, we've still got broken pavements that won't go away."
                a "I think there's a lot that can't go away."
                a "I think you just have to gouge deep enough for it to stay. {w}You just have to write with a scalpel and not a pen."
                p "Nobody can read the graffiti any more."
                a "Eh, maybe somebody will. If there's a past, there's a future."
                p "...Sure, I guess."
                scene bg room
                "Carving memory, huh."
                "I'm still missing something."
                "...I have a feeling the answer is in this room."
            jump mainroom
        else:
            "I've just checked on my camera, I don't think it's charged enough yet."
            jump mainroom

label clock:
    #clock stage 1
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        if clockS1 == False:
            $ clockS1 = True
            "Reflexively, I look to the clock."
            "It's out of battery, has been for a few weeks now."
            "I keep meaning to replace it, but..."
            "I quite literally don't have time for that right now."
            jump mainroom
        else:
            "I glance at the clock. {w}It's still broken."
            jump mainroom
    #clock stage 2
    if ticktock in range(4, 7):
        if remembranceS2 == True:
            jump end3
        if funky in range(4, 7):
            $ funky += 1
        if clockS2 == False:
            $ ticktock += 1
            $ clockS2 = True
            "."
            jump mainroom
        else:
            "."
            jump mainroom

label notebook:
    #notebook stage 1
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        if notebookS1 == False:
            $ ticktock += 1
            $ notebookS1 = True
            "Right, the notebook I've been using lately. {w}I pick it up, my teeth worrying my lower lip."
            "When I flip it open, it unfolds to a page still full with ink."
            p "..."
            "I'm relieved."
            "I thumb through, looking for anything relevant."
            "The pages shake so much, it's hard to read. {w}Even when I try to slow down."
            p "Flimsy paper."
            p "Hah."
            if havemarker == True:
                "When I reach an empty page, I uncap my marker and scrawl in the numbers: {w}{i}11 + 1, 1.{/i}"
                "Whatever I can remember, in as many places as I can leave them."
                "Even if I have no idea of its importance, {w}or if it's important at all."
                "Even if my memory is fucked beyond recognition when I come back to it, {w}I'll know I was trying."
                "That counts, doesn't it. {w}Symbols carrying meaning and shit."
                "Even when no-one knows what the symbol means any more."
                p "..."
                p "...Someone will know I tried."
                "Even if that's not me."
                "I recap the pen."
            "I turn the pages over and over. {w}Shopping lists. {w}Lines from some Brazilian poet. {w}Autograph."
            "Dairy entry, one line. {w}{i}500+ gone/crossed out/erased. Gazetted/published/announced 27-8.{/i}"
            "At least none of those descriptors had gone yet."
            "Dairy entry, two lines. {w}A 7-Eleven prize sticker. {w}I don't think I would have put an encoded message into a movie review."
            p "..."
            "I look at the paragraph. {w}Yeah, no. {w}If I had, then I still wouldn't have. {w}I would've known I was fucking myself over."
            p "!"
            "I stop at a page empty save for a couple of random straight lines."
            "Short lines. {w}Strokes that seem apart from one another."
            "A white space eating up the middle."
            p "..."
            "I know what I was trying to do here."
            "Abstracting the lines of the pen. {w}Trying to write a character without writing a character."
            "I guess it hadn't worked."
            p "Oh."
            p "That's right. I should..."
            "I should write an entry about the list gazetted today."
            "Another 500."
            "Some books stopped making sense years ago, too many spaces. {w}Too many white pages. {w}Spaces leading onto other spaces."
            "Not empty, just white."
            "Emptiness has a feeling, after all. {w}A lack. {w}But white is a fullness of its own."
            "Otherwise you wouldn't forget that you forgot."
            "And the page is white and still beneath my thumb. {w}Not even a palimpsest. {w}Though now I'll never know if it was."
            "But as I begin to reach for the words to write..."
            "My hand {glitch=59.94}jerks.{/glitch}"
            "{glitch=59.94}That's not what I need to do right now.{/glitch}"
            p "That's not what I need to do right now."
            "The paper trembles."
            p "Fuck. {w}Fuck."
            "I throw the notebook away. {w}It thumps on the ground, splays itself face down."
            "I can't waste any more time."
            jump mainroom
        else:
            "I glance at the notebook, still on the ground. No. I can't be distracted right now."
            jump mainroom
    #notebook stage 2
    if ticktock in range(4, 7):
        if funky in range(4, 7):
            $ funky += 1
        if notebookS2 == False:
            $ ticktock += 1
            $ notebookS2 = True
            "."
            jump mainroom
        else:
            "."
            jump mainroom

label pamphlet:
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        if pamphletS1 == False:
            $ ticktock += 1
            $ pamphletS1 = True
            "I pick up a stray pamphlet."
            "It's a government pamphlet of some sort, I don't really recognise the people on the front enough to know. {w}Well, I've scribbled a moustache onto the woman."
            "{i}Together we build a prosperous city of the present!{/i}"
            p "...Sure."
            "Flipping it open, it's pretty funny—{w}not humorously funny, not {i}'haha'{/i} funny, just bitter—{w}it's pretty funny seeing how half the text is gone."
            "Nobody manages to weasel their way out of this communal erasure—{w}not even the guys enacting it."
            "I'm not sure why I've kept it around, but it's pretty worn and torn."
            "These days, I'm a hoarder of random junk. {w}I guess it's the unreliability of memory, I don't want to throw anything away when it could have been something important."
            "Especially something like this, it looks like I've had it around for awhile."
            "It's not that items fare any better than memory when it comes to it, but...{w}I turn the pages, somehow expectant."
            "Sometimes I find unexpected traces, messages I churned into code so I'd be able to preserve the message. {w}Code I tried to obsfucate so it wouldn't go away."
            "But most of the time, these half-messages—{w}these cryptic bits of text—{w}are too out of context to understand, to make coherent."
            "Even so, I still do it. {w}Maybe I do it because all this detritus around me tells me that's who I am."
            p "...There's nothing here."
            "I'm at the back of the pamphlet. {w}No lines, no handwritten letters, nothing."
            "If there had been in the past, they're already gone."
            "But as I flip the pamphlet over again, I stop a moment."
            "I take a closer look at the purple moustache scribbled onto the face of the woman on the front. {w}There's a bonus purple hairdo on her as well."
            $ pamphletink = True
            "It's a pretty terribly drawn moustache, curly at the ends and filled in with ink. Same with the hair."
            "Only—{w}and before I can question how I trust this self-knowledge—{w}I know I don't draw. I didn't even doodle in school."
            "And now I could swear that—"
            p "They always do that."
            "They?"
            "I frown."
            "Right, {glitch=59.94}they—{/glitch}"
            if calendarink == True:
                jump remembrance1
            "{glitch=59.94}They—{/glitch}"
            $ renpy.pause(0.8, hard=False)
            "For some reason, I'm breathing a little heavily."
            "I look down at the pamphlet in my hand, and turn it over again."
            p "..."
            p "...Just now, I lost something."
            "But I don't know what that 'something' is."
            "I go through the pamphlet again, but like on my previous flip-through, there's nothing written in or around the pages."
            "..."
            "I look at my hands, but there's nothing on them either."
            "Whatever I missed, it's already gone."
            p "..."
            "I put down the pamphlet before I can crumple it."
            jump mainroom
        else:
            "No, I've just looked at the pamphlet."
            jump mainroom
    #pamphlet stage 2
    if ticktock in range(4, 7):
        $ funky += 1
        "."
        jump mainroom

label photograph:
    #photograph stage 1
    if ticktock in range(0, 4):
        if funky in range(0, 4):
            $ funky += 1
        if photographS1 == False:
            $ ticktock += 1
            $ photographS1 = True
            "There has to be something on that corkboard that's useful."
            "On the wall, I've pinned up photographs and a couple of postcards. Some newspaper clippings. {w}Most of the photographs are of other people, but there are a couple with me in it."
            "Some of the photographs are just paper, images I printed and cut out."
            "I don't know who I'm looking for—{w}and that had better help me out right now."
            "Most of the pictures are old, from years ago. {w}I've heard that old stuff lasts longer."
            "Doesn't erase the same."
            "Doesn't erase as fast as memory."
            "I skim haphazardly, going over the photographs one by one. {w}Or two by two. {w}Just quickly. {w}Sure, they say it doesn't erase as fast..."
            "But maybe that's a wrong memory too."
            "Near the top of the board right there's a picture of me and some other guys standing on top of a mountain ridge. {w}I'm making a V sign at the camera."
            "Another picture of me and a couple of friends surfing. {w}Photographs from that one trip we took to Hokkaido. {w}I recognise all the people in the photographs."
            "This isn't helping. This isn't what I'm looking for."
            "There's one print I pause at, some wasted guy vomiting down a sewer drain. {w}The camera's shaky, the man's face is blurred."
            "But I remember the context for this picture, and a second later I recognise the drunk guy after all—{w}one of my old coworkers from that shaved ice place, Rocky."
            "I can't remember which asshole who took the picture and handed out prints though. {w}Guess I'm an asshole too for sticking it up."
            "I stop on a postcard that looks a little out of place."
            "A postcard with a drawing of a Japanese shrine-looking place. Temple, maybe. {w}Looks like it's from a show or something."
            "But it's new. {w}No dust and just one tack, gone right through the middle. {w}I usually pin with two tacks, top left and top right."
            "I unpick the postcard from the board and turn it over in my hand."
            "On the back of the postcard, there's just a single letter. {w}It's followed by a swoop. {w}It's sloppy. {w}It's in my handwriting. {w}{i}A—{/i}."
            "I don't remember writing this."
            "'{i}A—{/i}.'"
            "I don't know who that is."
            if havename == True:
                "Is that 'Axel'?"
                "It's the same first letter, but..."
            "Going off gut feeling actually just feels like being in the dark, groping with both hands for the wall. {w}Any wall. {w}Any marker of time or place."
            "And you're trying to get somewhere, yeah. {w}But how do you get there if you don't know where you are."
            "If this is a direction, at least someone's gotta tell me my place on the map."
            p "..."
            "I take the postcard anyway. Even just so I can shove it in my pocket and feel it there, {w}a corner of card moving against my thumb."
            $ havepostcard = True
            jump mainroom
        else:
            "I glance at the corkboard again."
            "Nothing new there. {w}A sense of urgency drives me away."
            jump mainroom
    #photograph stage 2
    if ticktock in range(4, 7):
        if funky in range(4, 7):
            $ funky += 1
        if photographS2 == False:
            $ ticktock += 1
            $ photographS2 = True
            "."
            jump mainroom
        else:
            "."
            jump mainroom

label remembrance1:
    scene bg memory with Dissolve (0.5)
    $ remembranceS1 = True
    p "..."
    "I have to take a step back, clenching my eyes shut."
    scene bg black with Dissolve (0.1)
    scene bg room with Dissolve (0.1)
    scene bg black with Dissolve (0.1)
    scene bg room with Dissolve (0.1)
    scene bg black with Dissolve (0.1)
    scene bg memory with Dissolve (0.5)
    u "...you feel like you're living in a 'city of the present'?"
    p "..."
    p "Huh? {w}What's that you're looking at again."
    u "Here you go."
    "Something rustled."
    p "Thanks for just brandishing it in my general direction."
    p "..."
    p "...Huh. {w}Is that the lady running for election this year?"
    u "Look at the slogan."
    p "Yeah I'm looking at the slogan. {w}It's pretty short I guess."
    u "So I was saying, this place? {w}It's more like a city without a past, or maybe a city with the past burned clean out."
    u "No roots, no nothing. {w}You ever thought what a tree without roots would look like?"
    p "Hadn't thought about it before."
    u "In my head? I think it'd look like a skyscraper without any piers. No steel beams, just a mass of brick piled up above ground."
    p "Might look fine, but then say, a strong wind comes along. {w}And the wind goes whoosh, and after that..."
    p "Dude, just...{w}I get it, let's talk about something else."
    u "Sure, sure."
    scene bg room with Dissolve (0.5)
    "..."
    "Yeah, they always used purple gel pens for some reason. {w}Wouldn't say they carried them everywhere, but..."
    "What was it? Their sister had accidentally bought 400 or so in bulk one time? {w}Either way, enough stock to last a primary school class for a year."
    p "...When were they here."
    "..."
    "I think, though I can't be sure, the answer is...'not long ago'. {w}They were here not long ago."
    "It's not only my head that's aching."
    "I can feel something sharp and heavy at the back of my throat."
    "And I don't need to look to know the purple ink is already gone."
    jump mainroom
