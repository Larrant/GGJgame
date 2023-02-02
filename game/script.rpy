define p = Character("...")
define a = Character ("Axolotl")
define f = Character ("That Man")

default bike = 0
default fishfood = 0

label start:
    scene bg room
    play music room fadein 3.0
    $ renpy.pause(0.3, hard=False)
    "As a child, I learned to lie."
    $ renpy.pause(0.3, hard=False)
    "No-one taught me how."
    $ renpy.pause(0.3, hard=False)
    "I learned to lie as I learned to live, and the two became more or less inseparable. {w}White lies. {w}Lies of omission. {w}Lies of denial."
    $ renpy.pause(0.3, hard=False)
    "Lies I made to live."
    $ renpy.pause(0.3, hard=False)
    "Sometimes they were the only way to live."
    $ renpy.pause(0.3, hard=False)
    "Without an explanation, does that make sense? {w}It doesn't matter. {w}If I had to explain it, it wouldn't make sense anyway."
    $ renpy.pause(0.3, hard=False)
    "The phone on the table vibrates. I ignore the sound, digging into a pile of miscellanea by the door instead."
    play sound searching_desk
    $ renpy.pause(0.3, hard=False)
    "A box of tissues, unopened. A six-pack of tinned dace I've been meaning to put in the cupboard. A bunch of campaign pamphlets. {w}An empty envelope."
    $ renpy.pause(0.3, hard=False)
    "I scrunch the envelope into a rough ball and aim it at the bin. {w}It misses. Tch."
    $ renpy.pause(0.5, hard=False)
    "Where did I put that pack of pellets?"
    $ renpy.pause(0.3, hard=False)
    "In his tank, John Doe looks at me with baleful eyes."
    $ renpy.pause(0.3, hard=False)
    p"I get it, I get it, give me a break. {w}Heck, you could take a break from being so high maintenance for a change."
    $ renpy.pause(0.3, hard=False)
    "The axolotl doesn't reply."
    $ renpy.pause(0.3, hard=False)
    "My knees hurt when I stand up. {w}Old aches. {w}As I look around, the phone on the table vibrates again."
    $ renpy.pause(0.3, hard=False)
    p "I said give me a fucking break."
    jump mainroom

label mainroom:
    menu():
        extend ""
        "Click on the bike object innit":
            if bike == 0:
                $ bike += 1
                $ renpy.pause(0.3, hard=False)
                "Out of listlessness more than hopeful intent, I check the bike."
                play sound searching_desk
                $ renpy.pause(0.5, hard=False)
                "Nothing behind the brakes. {w}I haven't taped John Doe's food under the seat in a fit of maniacal disorder."
                $ renpy.pause(0.3, hard=False)
                "As I use the seat to lever myself back up, I notice a flake of blue coming off on my hand. The fabric on the saddle is starting to peel. More than that, the whole saddle is starting to peel off."
                $ renpy.pause(0.3, hard=False)
                "I keep meaning to buy fabric glue for the saddle. Or maybe some sealant."
                $ renpy.pause(0.3, hard=False)
                "I keep meaning to buy a new bike, actually."
                $ renpy.pause(0.3, hard=False)
                "It feels like I've been fixing this one for years. If it isn't the brake going nuts it's the pedal or the cogset. Last month I had to put new spokes in."
                $ renpy.pause(0.3, hard=False)
                "And it's not my bike, anyway."
                $ renpy.pause(0.3, hard=False)
                f "You're independent? You're still using this family's things."
                $ renpy.pause(0.3, hard=False)
                f "Don't joke around."
                $ renpy.pause(0.3, hard=False)
                "Tch."
                $ renpy.pause(0.3, hard=False)
                "If I buy a new bike, I'll be able to..."
                menu():
                    extend ""
                    "Return this one.":
                        $ renpy.pause(0.3, hard=False)
                        "Battered, sure, but at least I can return it. Maybe I'll even spritz it up before I dump it back on them. Give it a new paintjob, replace the cogset and oil it up."
                        $ renpy.pause(0.3, hard=False)
                        "That way they can't complain."
                        $ renpy.pause(0.3, hard=False)
                        "Petty? {w}Them, maybe. Not me."
                    "Throw this one away.":
                        $ renpy.pause(0.3, hard=False)
                        "It's trash anyway."
                        $ renpy.pause(0.3, hard=False)
                        "It was always trash. Nobody used it except for me."
                        $ renpy.pause(0.3, hard=False)
                        "Of course, they made a fuss when I took it. See, it hadn't mattered before, but it suddenly mattered."
                        $ renpy.pause(0.3, hard=False)
                        "Nobody had used it before, but it was suddenly theirs."
                        $ renpy.pause(0.3, hard=False)
                        "And suddenly everything that hadn't mattered became little points to tally up, little debts that grew into one big, insurmountable debt."
                "I turn away."
                jump mainroom
            if bike == 1:
                $ bike += 1
                $ renpy.pause(0.3, hard=False)
                "I already checked the bike."
                $ renpy.pause(0.3, hard=False)
                "I remember this bike had been bought for me."
                $ renpy.pause(0.3, hard=False)
                "A birthday gift, something like that. It was a bike, so it was supposedly meant to be shared... {w}but by then, I was the only one interested in cycling, and I was the only one who ended up using it."
                scene black with Dissolve (0.6)
                $ renpy.pause(0.3, hard=False)
                p "You promised to go with me to the trail this afternoon. Are you still coming?"
                $ renpy.pause(0.3, hard=False)
                f "That again? Not today, dad's too tired to do it today. Next week, okay."
                $ renpy.pause(0.3, hard=False)
                p "You said 'next week' last week."
                $ renpy.pause(0.3, hard=False)
                f "It's busy for me at work right now. I told you I don't have the time, I have to deal with a lot."
                $ renpy.pause(0.3, hard=False)
                f "If you want to cycle, do it yourself. Get your brother to go with you."
                $ renpy.pause(0.3, hard=False)
                p "You're going back on your word again? {w}You said you'd go with me today."
                $ renpy.pause(0.3, hard=False)
                f "Hey. Hey. Didn't you say you would cycle to school every day if we bought you the new bike? How come you're still catching the subway every day, huh?"
                $ renpy.pause(0.3, hard=False)
                p "Don't change the subject. You promised me."
                $ renpy.pause(0.3, hard=False)
                f "We already bought you the bike! Isn't that enough?"
                $ renpy.pause(0.3, hard=False)
                f "You can't have everything."
                $ renpy.pause(0.3, hard=False)
                p "..."
                $ renpy.pause(0.3, hard=False)
                p"You're busy with work? {w}Even on weekends? {w}Even right now? It's Saturday."
                $ renpy.pause(0.3, hard=False)
                p"Every weekend and you just stay home and watch TVB like an idiot. You never go out, you never do anything!"
                play sound impact_fist_on_table
                $ renpy.pause(0.3, hard=False)
                f "You shut your mouth!"
                $ renpy.pause(0.3, hard=False)
                f "I work, I put food on this family's table, do I have to work on the weekend too, just because my kid won't stop running his mouth?!"
                $ renpy.pause(0.3, hard=False)
                p "So spending time with your kid is work?"
                $ renpy.pause(0.3, hard=False)
                p "How can you call yourself a father."
                $ renpy.pause(0.3, hard=False)
                f "!"
                scene bg room
                $ renpy.pause(0.3, hard=False)
                "My jaw aches."
                $ renpy.pause(0.3, hard=False)
                "I thought I'd forgotten about that, but..."
                menu():
                    extend ""
                    "What a sorry excuse for a father.":
                        $ renpy.pause(0.3, hard=False)
                        p "It makes me angry just thinking about it."
                        $ renpy.pause(0.3, hard=False)
                        p "Haha."
                        $ renpy.pause(0.3, hard=False)
                        "He probably promised it countless times, but he never did it."
                        $ renpy.pause(0.3, hard=False)
                        "He never went biking with me, not once."
                        $ renpy.pause(0.3, hard=False)
                        "If he hadn't meant to keep his promises, he shouldn't have made them at all."
                        $ renpy.pause(0.3, hard=False)
                        "I should stop thinking about it."
                    "I shouldn't have lashed out.":
                        $ renpy.pause(0.3, hard=False)
                        "It's embarrassing. Like a small needle, like the ache of a sore tooth at the back of the mouth."
                        $ renpy.pause(0.3, hard=False)
                        "Clenching down on the molars and feeling the ache turn into a raw gash."
                        $ renpy.pause(0.3, hard=False)
                        "I knew that guy was working hard. In retrospect, I guess everyone has their own ways of coping with stress."
                        $ renpy.pause(0.3, hard=False)
                        p "I was pretty selfish when I was younger, huh."
                        $ renpy.pause(0.3, hard=False)
                        p "Haha."
                        $ renpy.pause(0.3, hard=False)
                        "..."
                    "It doesn't matter.":
                        $ renpy.pause(0.3, hard=False)
                        "Yeah. {w}It's over with. I'm not even living in the same house. It's no use feeling anything now."
                $ renpy.pause(0.3, hard=False)
                p "It's not like I can go back and change the past."
                $ renpy.pause(0.3, hard=False)
                p "..."
                jump mainroom
            if bike == 2:
                $ bike += 1
                $ renpy.pause(0.3, hard=False)
                "It's funny. The last time I spoke to that guy about it, he said he remembered going cycling with me."
                $ renpy.pause(0.3, hard=False)
                "I told him he hadn't. Not once."
                $ renpy.pause(0.3, hard=False)
                "He didn't believe me. {w}He said he was sure he had."
                $ renpy.pause(0.3, hard=False)
                "He even mentioned the name of a trail. I'd gone on that cycling trail, sure. But not with him."
                menu():
                    extend ""
                    "...Liar":
                        $ renpy.pause(0.3, hard=False)
                        "He was so confident. {w}I would have gone insane, if my mother hadn't been on my side and interjected then."
                        $ renpy.pause(0.3, hard=False)
                        "She said she was sure he hadn't gone cycling with me either. She remembered that he hadn't. Not once. {w}Not once."
                        $ renpy.pause(0.3, hard=False)
                        "Afterwards, he still wouldn't concede it."
                        $ renpy.pause(0.3, hard=False)
                        p "Because he can never be wrong, can he."
                    "...":
                        $ renpy.pause(0.3, hard=False)
                        "I'm sure that before that moment, I was the only one who remembered clearly anyway."
                        $ renpy.pause(0.3, hard=False)
                        "It hadn't been important to him, so he forgot about it."
                        $ renpy.pause(0.3, hard=False)
                        "He forgot about all of it, and when I told him he'd never gone cycling with me...{w}he couldn't believe that. He wouldn't believe me. {w}When my mother interjected, he hadn't been able to say a word."
                        $ renpy.pause(0.3, hard=False)
                        "He was always like that."
                jump mainroom
            if bike == 3:
                $ renpy.pause(0.3, hard=False)
                "..."
                jump mainroom
    return

###
### Sound from Zapsplat.com
