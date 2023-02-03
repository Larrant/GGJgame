define config.rollback_enabled = False

define p = Character("...")

default ticktock = 0
default funky = 0

default havepostcard = False
default havemarker = False

default bikeS2 = False
default calendarS1 = False
default calendarS2 = False
default cameraS1 = False
default cameraS2 = False
default notebookS1 = False
default notebookS2 = False
default photographS1 = False
default photographS2 = False

image bg white = "#fff"
image bg black = "#000"

label start:
    scene bg black
    $ renpy.pause(0.3, hard=False)
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
    jump mainroom

label mainroom:
    scene bg black
    if funky == 1:
        $ renpy.pause(0.5, hard=False)
        "My head hurts."
        "I need to hurry."
        "I need to find them."
        window hide
    if funky == 2:
        $ renpy.pause(0.5, hard=False)
        "The sun's going to set soon."
        "On my way back, I tried to call them."
        "No. I wanted to call them."
        "I didn't know how to try."
        "I checked my phone, I scrolled down all my contacts. But none of them seemed right. {w}I don't think I saved them to my contacts list."
        "I checked all the calls I'd made this month, but there were too many. I had a feeling—"
        "I wouldn't recognise their number anyway."
        window hide
    if funky == 3:
        $ renpy.pause(0.5, hard=False)
        "It's meant to be painless, {w}but my head hurts anyway."
        window hide
    if ticktock == 4:
        $ renpy.pause(0.5, hard=False)
        "The sun is setting. {w}It's beautiful, though it doesn't reach the inside of my room well."
        "At one of my old jobs, I used to be able to look out of the service window and skim over the buildings to reach the mountains."
        "The sun would set orange at around seven in summer, and a pinkish glow would gather at my feet. {w}Always felt sort of melancholy, that."
        "Maybe it was how soft everything got, when the sun pastelled the walls of apartment blocks and sidewalks. {w}Felt like you were in a softer world, {w}a world half out of a dream."
        "A Hong Kong both familiar and not."
        "I look away from the sliver of twilight through the blinds."
        p "Right. I still have to find them."
        "Even if I have this feeling...{w}it's getting too late."
        window hide
        #end demo here
        show text "To Be Continued (Well. To Be Finished By The 4th)" at truecenter
        with dissolve
        pause
        hide text
        with dissolve
        return
        #end of end-demo-screen teehee
    if funky == 5:
        $ renpy.pause(0.5, hard=False)
        "funky: 5."
        window hide
    if ticktock == 7:
        $ renpy.pause(0.5, hard=False)
        "..."
        window hide
    scene bg room
    menu():
        "Bike":
            jump bike
        #"Book":
        #    jump book
        "Calendar":
            jump calendar
        "Camera":
            jump camerascene
        #"Clock":
        #    jump clock
        #"Delivery receipt":
        #    jump receipt
        #"Fan":
        #    jump fan
        #"Pamphlet":
        #    jump pamphlet
        "Notebook":
            jump notebook
        "Photographs":
            jump photograph
        #"Snacks":
        #    jump snack
        #"Takeout Menu":
        #    jump takeout
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
    #bike stage 3
    if ticktock in range(7, 10):
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
            "It's not from a marker. No, I'm sure—{w}I'm sure it's theirs."
            "Right, because they always used glittery gel pens. {w}Carried one everywhere."
            "That's right, they were here. {w}Not long ago, they were here and they had written something in this calendar."
            "Maybe they weren't careful enough, maybe it's gone already. {w}Just the {glitch=59.94}smear{/glitch} now, just the trail of {glitch=59.94}ink{/glitch}."
            "But as I reach out to touch this proof of life, it {glitch=59.94}goes like—{/glitch}"
            "And then it's—"
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
                    "{i}Axel T.S Fung{/i}"
                    p "..."
                    "The recognition, or—{w}rather—{w}the non-recognition, is tasteless."
                    "Is that the name of the friend who gave me this camera?"
                    "Did I forget that too?"
                    if havepostcard == True:
                        "And—{w}I reach into my pocket and a corner of plasticky cardstock pricks my finger."
                        "{i}'A—'{/i}."
                    "Is that the person I'm trying to find?"
                    "But there's no contact information on the rest of the page."
            jump mainroom
        else:
            "I've just looked at that."
            jump mainroom
    #camera stage 2
    if ticktock in range(4, 7):
        if funky in range(4, 7):
            $ funky += 1
        if cameraS2 == False:
            $ ticktock += 1
            $ cameraS2 = True
            "."
            jump mainroom
        else:
            "."
            jump mainroom
    #camera stage 3
    if ticktock in range(7, 10):
        "."
        jump mainroom
    if ticktock == 8:
        jump end1

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
    #notebook stage 3
    if ticktock in range(7, 10):
        "."
        jump mainroom
    if ticktock == 8:
        jump end1

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
    if ticktock == 8:
        jump end1

label end1:



###
### Sound from Zapsplat.com
