define p = Character("...")
define a = Character ("Axolotl")
define f = Character ("That Man")

default bike = 0

label start:
    scene bg room
    window show
    "As a child, I learned to lie."
    "No-one taught me how."
    "I learned to lie as I learned to live, and the two became more or less inseparable. {w}White lies. {w}Lies of omission. {w}Lies of denial."
    "Lies I made to live."
    "Sometimes they were the only way to live."
    "Without an explanation, does that make sense? {w}It doesn't matter. {w}If I had to explain it, it wouldn't make sense anyway."
    "The phone on the table vibrates. I ignore the sound, digging into a pile of miscellanea by the door instead."
    "A box of tissues, unopened. A six-pack of tinned dace I've been meaning to put in the cupboard. A bunch of campaign pamphlets. {w}An empty envelope."
    "I scrunch the envelope into a rough ball and aim it at the bin. {w}It misses. Tch."
    "Where did I put that pack of pellets?"
    "In his tank, John Doe looks at me with baleful eyes."
    p"I get it, I get it, give me a break. {w}Heck, you could take a break from being so high maintenance for a change."
    "The axolotl doesn't reply."
    "My knees hurt when I stand up. {w}Old aches. {w}As I look around, the phone on the table vibrates again."
    p "I said give me a fucking break."
    jump mainroom

label mainroom:
    menu():
        extend ""
        "Click on the bike object innit":
            if bike == 0:
                $ bike += 1
                "Out of listlessness more than hopeful intent, I check the bike."
                "Nothing behind the brakes. {w}I haven't taped John Doe's food under the seat in a fit of maniacal disorder."
                "As I use the seat to lever myself back up, I notice a flake of blue coming off on my hand. The fabric on the saddle is starting to peel. More than that, the whole saddle is starting to peel off."
                "I keep meaning to buy fabric glue for the saddle. Or maybe some sealant."
                "I keep meaning to buy a new bike, actually."
                "It feels like I've been fixing this one for years. If it isn't the brake going nuts it's the pedal or the cogset. Last month I had to put new spokes in."
                "And it's not my bike, anyway."
                f "You're independent? You're still using this family's things."
                f "Don't joke around."
                "Tch."
                "If I buy a new bike, I'll be able to..."
                menu():
                    extend ""
                    "Return this one.":
                        "Battered, sure, but at least I can return it. Maybe I'll even spritz it up before I dump it back on them. Give it a new paintjob, replace the cogset and oil it up."
                        "That way they can't complain."
                        "Petty? {w}Them, maybe. Not me."
                    "Throw this one away.":
                        "It's trash anyway."
                        "It was always trash. Nobody used it except for me."
                        "Of course, they made a fuss when I took it. See, it hadn't mattered before, but it suddenly mattered."
                        "Nobody had used it before, but it was suddenly theirs."
                        "And suddenly everything that hadn't mattered became little points to tally up, little debts that grew into one big, insurmountable debt."
                "I turn away."
                jump mainroom
            if bike == 1:
                $ bike += 1
                "I already checked the bike."
                "The bike had been bought for me."
                "A birthday gift, something like that. It was a bike, so it was supposedly meant to be shared... {w}but by then, I was the only one interested in cycling, and I was the only one who ended up using it."
                scene black with Dissolve (0.6)
                p "You promised to go with me to the trail this afternoon. Are you still coming?"
                f "That again? Not today, dad's too tired to do it today. Next week, okay."
                p "You said 'next week' last week."
                f "It's busy for me at work right now. I told you I don't have the time, I have to deal with a lot."
                f "If you want to cycle, do it yourself. Get your brother to go with you."
                p "You're going back on your word again? {w}You said you'd go with me today."
                f "Hey. Hey. Didn't you say you would cycle to school every day if we bought you the new bike? How come you're still catching the subway every day, huh?"
                p "Don't change the subject. You promised me."
                f "We already bought you the bike! Isn't that enough?"
                f "You can't have everything."
                p "..."
                p"You're busy with work? {w}Even on weekends? {w}Even right now? It's Saturday."
                p"Every weekend and you just stay home and watch TVB like an idiot. You never go out, you never do anything!"
                f "You shut your mouth!"
                f "I work, I put food on this family's table, do I have to work on the weekend too, just because my kid won't stop running his mouth?!"
                p "So spending time with your kid is work?"
                p "How can you call yourself a father."
                f "!"
                scene bg room
                "My jaw aches."
                "I thought I'd forgotten about that, but..."
                menu():
                    extend ""
                    "What a sorry excuse for a father.":
                        p "It makes me angry just thinking about it."
                        p "Haha."
                        "He probably promised it countless times, but he never did it."
                        "He never went biking with me, not once."
                        "If he hadn't meant to keep his promises, he shouldn't have made them at all."
                        "I should stop thinking about it."
                    "I shouldn't have lashed out.":
                        "It's embarrassing. Like a small needle, like the ache of a sore tooth at the back of the mouth."
                        "Clenching down on the molars and feeling the ache turn into a raw gash."
                        "I knew that guy was working hard. In retrospect, I guess everyone has their own ways of coping with stress."
                        p "I was pretty selfish when I was younger, huh."
                        p "Haha."
                        "..."
                    "It doesn't matter.":
                        "Yeah. {w}It's over with. I'm not even living in the same house. It's no use feeling anything now."
                p "It's not like I can go back and change the past."
                p "..."
                jump mainroom
            if bike == 2:
                $ bike += 1
                "It's funny. The last time I spoke to that guy about it, he said he remembered going cycling with me."
                "I told him he hadn't. Not once."
                "He didn't believe me. {w}He said he was sure he had."
                "He even mentioned the name of a trail. I'd gone on that cycling trail, sure. But not with him."
                menu():
                    extend ""
                    "...Liar":
                        "He was so confident. {w}I would have gone insane, if my mother hadn't been on my side and interjected then."
                        "She said she was sure he hadn't gone cycling with me either. She remembered that he hadn't. Not once. {w}Not once."
                        "Afterwards, he still wouldn't concede it."
                        p "Because he can never be wrong, can he."
                    "...":
                        "I'm sure that before that moment, I was the only one who remembered clearly anyway."
                        "It hadn't been important to him, so he forgot about it."
                        "He forgot about all of it, and when I told him he'd never gone cycling with me...{w}he couldn't believe that. He wouldn't believe me. {w}When my mother interjected, he hadn't been able to say a word."
                        "He was always like that."
                jump mainroom
            if bike == 3:
                "..."
                jump mainroom
    window hide
    return
