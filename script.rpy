# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]", color="#ffffff", what_prefix='"', what_suffix='"')
define mci = Character("[mcname]", color="#ffffff", what_italic=True)
define mcn = Character(None, what_color="ffee8c")
define nug = Character("Dago", color="ffa500", what_prefix='"', what_suffix='"')
define chill = Character("Chill Guy", color="b0e0e6", what_prefix='"', what_suffix='"')
define gig = Character("Gigachad Senpai", color="cbc3e3", what_prefix='"', what_suffix='"')
define amg = Character("Amongus Imposter", color="c51111", what_prefix='"', what_suffix='"')
define emo = Character("Edgemund", color="1c1c84", what_prefix='"', what_suffix='"')
define tom = Character("Tomato Man", color="ffc0cb", what_prefix='"', what_suffix='"')
define ksi = Character("KSI", color="c8ffc8", what_prefix='"', what_suffix='"')
define quan = Character("Quandale Dingle Fairy", color="1bfc06", what_prefix='"', what_suffix='"')
define ski = Character("Mr Skibidi Toilet", color="cabd99", what_prefix='"', what_suffix='"')
define tate = Character("Andrew Tate", color="d3d3d3", what_prefix='"', what_suffix='"')

define gyatt_coins = 0
call shop

default gyatt_coins  = 0
default mcname = "bob" ## get rid of this line afterwards
# the mcname part didn't work wtf, just past this into the bottom of sherry's code and it should work

# The game starts here.
label start:
    scene black
    pause 5.0
    show text "Chapter 1 - Day 2" with dissolve
    pause 1.0
    hide text with fade
    # new day, extra gyatt points
    $ gyatt_coins = gyatt_coins + 25

    #play music "audio/bgm_alarm.mp3" fadein 0.0 volume 0.5
    #stop music fadeout 1.0
    #play sound "audio/sfx_blanket.mp3"
    #play sound "audio/sfx_stairs.mp3"
    #play music "audio/neighbr.mp3" # i think you might need to look over this cause idk i named it right
    scene bg neighbr # again ill ask sherry to handle this part
    with fade
    # code the sprite into the cventre
    mc "Another skibidi Tuesday morning!"
    mc "Maybe Dago will bike with me to school again"
    mc "What a sweet 'n sour guy"
    #play sound "audio/bike bell ringing" # ill leave it to you to do sound ngl
    #play sound "audio/gegadio.mp3"
    #play sound "audio/footsteps.mp3"
    # dago sprite enters on right, so then move mc sprite to left
    nug "Sup fellow Ohio rizzler!"
    nug "Looks like vro's actually on time today."
    nug "Whaddya think of your first day at school?"
    mc "Kinda based lowkey."
    mci "We only just met yesterday but he talks like we've been \'vro's\' for like 20 seasons."
    mci "Not that I mind it though. \n\nThis whole friendship thing is . . . kinda weird to get used to."
    mcn " You can imagine upgrading your school grindset with this guy."
    #fade in of zoomed in Dago's smirk
    mcn "His off-kilter grin appears in your mind."
    mci "Hmmm, maybe hanging out together isn't too bad."
    nug "Yeah vro, y'know, like education?"
    nug "It's like a real life glitch."
    mc "Dawg . . ."
    mci "What is this guy even on about LOL."
    mci "These Ohio rizzlers . . . sigh. \nI feel like he has no idea how education works in real life."
    nug "Vro hurry up. \nWe're gonna be late for rizzonomics with Mr Skibidi again."
    mci "I wonder If I will become like this guy one day. \nSmirking 24/7 without a worry in the world."
    nug "HURRY UP XD"
    nug "At this rate, we have to Naruto run."
    mc "Wait, where's your bike???"
    nug "I forgot :)"
    mcn "You sigh."
    ## running to school sounds
    ## some sort of transition to school
    scene black
    pause 3.0
    show text "at school" with dissolve
    pause 1.0
    hide text with fade

    # BG classroom
    # classroom music
    # make sure to somehow change MC's name as accordingly
    # checkpoint, extra gyatt points
    $ gyatt_coins = gyatt_coins +25
    # lowkey, we should have a coin deposit sound
    ski "I'm sure you rizzlers heard yesterday, but our new student here, [mcname], is joining us until we graduate."
    ski "Which I hope will be before gta 6."
    mcn "You cringe."
    ski "Unfortunately, that means our class number is now uneven."
    ski "Instead of the usual pairs, I need you to split into groups of three to start our looksmaxxing lesson for today."
    mcn "You glance at Dago. \n He gets the memo and griddles over to your desk."
    mcn "He also wants to be Looksmaxxing homies, hey. \n But who will be your third wheeler?"
    mcn "By now the class has erupted into a  feud, trying to snag up their mates."
    
    default choice1 = False
    default choice2 = False
    default choice3 = False
    default choice4 = False
    label option1:
        menu:
            "Edgemund? Edgemund's highkey a mogger." if not choice1:
                jump choices1_a
            "What about Tiktok Rizz Party Tomato Boy? He be kinda bad ngl." if not choice2:
                jump choices1_b
            "Amongus - what if he's a chad braniac under that suit?" if not choice3:
                jump choices1_c
            ". . . Chill Guy?" if not choice4:
                jump choices1_d
        
        label choices1_a:
            nug "Nah, lil’ ol’ Edger over there is a bit too beta for us. Pick someone else."
            $ choice1 = True
            jump option1

        label choices1_b:
            nug "We can't have his redness cockblocking our looksmaxxing today."
            $ choice2 = True
            jump option1

        label choices1_c:
            nug "That loser? Nah vro, we're gonna be in aura debt cause of him. Bro's too much of a sussy baka."
            $ choice3 =True
            jump option1

        label choices1_d:
            $ gyatt_coins = gyatt_coins +100
            # money sound effects
            $ choice4 = True
            nug "Yeah lets do it! He's gonna mog everyone."
            nug "But idk if KSI is gonna be all gelatinous jellous though."
            jump back1
        label back1:
            mci "So Chill Guy really does go to this school as well."
            mc "KSI who?"
            mcn "Your stomach flips as the thought of Chill Guy being chummy with someone else consumes you."
            mci "Wait, what am I thinking?"
            mci " Chill guy was the one who abandoned me, I shouldn't be wanting him so bad."
            nug "KSI is Chill Guy's bestie."
            mcn "You feel your heart sink into your stomach just a little."
            nug "Let's go vro."
            nug "Ask Chill guy o'er."
            mc "M-m-m-m-me?\nA-a-asking Chill Guy Chan????"
            mcn "Butterflies dash through your stomach as your feet become glued to the ground."
            mci "I ran away from him yesterday . . . !\nThat was so baka of me, how can I face him today?"
            nug "Gyatt up and ask already!!"
            nug "He's lowkey just a chill guy!"
            mc "Yea, true that . . .\nEven if he's mad at me, I just need to remember he's lowkey just a chill guy."
            nug "Aight cus wtv sails ur ship."
            ## new scenery?
            mcn "You pull up to Chill Guy's seat, and he turns to look at you with that same unchanging expression."
            mci "Oh my god . . .\nI think my heart is about to leap out of my chest."
            mc "Hey baka. *blushes*\nWanna looksmaxx with us?"
            mci "Was that chill enough for Chill Guy?\n Please tell me he says yes."
            mci "I'm begging him. I'd sell my fortnite battlepass for him to say yes."
            mcn "Chill Guy seems surprised, but doesn't question you."
            mcn "You can't fault him for it though, since you just ghosted him irl yesterday night."
            chill "Yea, I'm chill with that.\nLet me just double check with KSI real quick."
            #bgm the thick of it
            mcn "KSI slams open the classroom door and somehow appears next to Chill Guy in a flash."
            ksi ". . ."
            ski ". . ."
            mcn "Mr Skibidi doesn't seem to care."
# thick of it fades out, BGM lofi again
            ksi "You wassup little dude?\n I could hear my name."
            chill "Me and my homies, [mcname] and Dago are gonna looksmaxx together for Skibidi's class today."
            chill "That chill with you?"
            mcn "You hear a slight growl emanating from KSI's throat."
            mci "KSI wtf? Why's he growling at me??? KYAAAAAA."
            mcn "You turn around to Dago to see if he's noticed as well, but Dago's off yapping with other classmates."
            nug "Hang on, [mcname] I totally forgot that I was gonna stack with Livvy Dunne and Grimace."
            nug "That wasn't very skibidi of me . . .\nNegative 100 aura,, mb cuh!!"
            mcn "You mentally facepalm.\nAnd curse Dago."
            mci "Does that mean me and Chill Guy are going to be alone?????"
            mci "Well, not exactly alone. \nWouldn't KSI be joining?"
            default choice11 = False
            default choice12 = False
        label back2:   
           menu:
                "Ask Mr Skibidi if you can be a pair" if not choice11:
                    mcn "You griddy up to Mr Skibidi and ask him about changing the trio to a pair."
                    ski "What the sigma?\n No, gyatt back and join KSI."
                    mcn "You walk back to Chill Guy's desk dejectedly."
                    $ choice11 = True
                    jump back2
                "Invite KSI into the trio and skip the Skibidi rage fest.":
                    $ gyatt_coins = gyatt_coins +100
# gyatt coins sound
                    $ choice12 = True
                    menu:
                        "Do a little Subway Surfer compilation, gather your balls, and ask KSI yourself.":
                            $ gyatt_coins = gyatt_coins +100
# money sound
                            ksi "UGH."
                            ksi "wot in the Rizz Ohio do you want . . .\nBro thinks he's Carti."
                            mci "I think he thinks I can't hear him . . ."
                            mci "He doesn't seem to be declining though. Let me ask again."
                            mcn "You watch as KSI turns up the boombox, repeatedly playing his own voice in a song."
                            # increase music, thick of it
                            mcn "Your domain collapses under KSI's alpha male energy."
                            mc "Ummm, yeah! Do you want to join me and Chill Guy?"
                            mcn "KSI looks at you for 1 nanosecond, scoffs, then looks away."
                            mci "He was so nice to Chill Guy just then!!! What's up with him changing moods so quick, damn."
                            mcn "Chill Guy interrupts for a second, and is finally able to grab KSI's attention."
                            jump back3
                        "Pull a non-nonchalant dreadhead and let Chill Guy ask KSI instead.":
                            jump back3
        label back3:
            chill "Hey KSI, we should form a trio then."
            mcn "KSI nods, and hence ends up joining your looksmaxxing empire."
            mcn "You notice that he keeps staring at Chill Guy and singing Kiki under his breath."
            # short sfc, kiki do you love me
            chill "Blud, calm down a bit.That loud boom box isn't very chill."
            # thick of it fades out, BGM - lofi again
            chill "Also, meet [mcname]! You weren't here yesterday, but they just moved here."
            ksi "What kind of sore loser moves here in the middle of the term?"
            ksi "That was soooooo last year."
            mcn "You notice that damn, KSI already thinks you're a gooner."
            mcn "He T-poses on the spot."
            mci "What in the goofy ahh is the 2016 ahh pose? That is so not poggers."
            mci "At least Chill Guy Chan hasn't mentioned anything about yesterday yet . . ."
            chill "Chill my guy. [mcname] is lowkey just a chill guy too bro."
            mci "Why's Chill Guy sticking up for me? What if he's . . ."
            mci "Am I delulu to think I could rizz him up??"
            mcn "Your thoughts are interrupted by KSI blowing spitballs at your level 1000 gyatt."
            # bgm thick of it
            ksi "Get L ratioed you bozo. How does one even achieve that build? That's some sort of chungus shit."
            menu:
                "H-h-h-hey stob it. Thats not very sigma of you!!":
                    mcn "As you are about to respond, Chill Guy interrupts."
                    # thick of it fades out
                    chill "Chillax guys, it's not that deep."
                    chill "we should be working on looksmaxxing before Mr Skibidi comes around and flushes us down his toilets."
                    chill "I mean I'm chill wsith that, but I dont know about you, KSI."
                    mcn "Chill Guy furrows his brows."
                    jump back4
                "Go sit in a corner and cry.":
                    mcn "As you try leave, Chill Guy takes his hands out of his pockets for the first time, and grabs yours."
                    chill "Hey [mcname], it's not that deep."
                    chill "Come back and I'll talk to KSI about it. He wasn't being very chill and that's not how we do things around here."
                    jump back4
        label back4:
            mcn "Both of you reluctantly return to do looksmaxxing homework with Chill Guy, but your mind keeps wandering to how swag he looked earlier."
            mcn "You could say that he saved you, in a way."
            mci "KSI was a bit cringle just now."
            mci "Like some sort of sussy baka, an not ina  good way like the nerd Amongus guy. I wonder what's up with him?"
            # bg fades to black

            # break time, bg cafeteria, sfx bell rings, bgm change lofi
            $ gyatt_coins = gyatt_coins +25
            mc "Whopper Whopper Whopper Whopper!!"
            mcn "You pull out your lunchbox."
            mci "MMMMM. Thsi glizzy smells like it could be fanum taxed at any moment."
            mci "I mean . . . If this was someone else's sandwich, I would totally fanum tax it."
            #sfx gegadigendiago
            nug "Heya [mcname], how was class? How ya feel about our Rizz academy so far?"
            nug "Two lessons in two days, and you got to hang out with Chill Guy, the chillest vro, of all people!"
            mc "Yeah Chill Guy is pretty poggers."
            mc "I don't know about KSI though. There's something a bit funny about him, lowkey gassed up or something. And he's already against me for no reason."
            mc "A-anyways, what do you mean \'Chill Guy, of all people\'?"
            nug "OMG OMG OMG you don't know????"
            nug "Haven't you noticed that he's so chill?"
            mci "Well yeah. What a captain obvious."
            nug "Barely anyone gets to speak with him cause KSI is always around. Him and his delulu ahh are always stuck together like buttcheeks."
            mc ". . . Do you know why that is?"
            nug "Why you askin'?\nYou interested?"
            menu:
                "I-i-interested in Chill Guy???? I mean . . . just maybe . . .":
                    $ gyatt_coins = gyatt_coins+25
                    mc "I used to know him before cooming to Ohio . . ."
                    nug "What in the fortnite battle pass are you on about vro? . . ."
                    jump back5
                "You mean there's something going on between KSI and Chill guy????":
                    nug "All my fellas find it strnge too. He's always staring and always knows hwere Chill Guy's massive gyatt is."
                    jump back5
                "No, not interested. That sounds like something a beta would ask!"
                    nug "Oh."
                    nug "I thought you would be up for some gossip. Go piss girl."
                    jump back5
        label back5:
            mcn "You quickly scarf down your glizzy as lunch ends."
            mci "Time to looksmaxx again with Chill Guy and his buddy KSI . . ."
            mcn "You're kind of dreading losing braincells with KSI, but at lest Chill Guy will be there again."
            mci "Is he ever going to bring up our childhood . . .?"

# fade tp black
    label subconscious:
        $ gyatt_coins = gyatt_coins +25
        tate "So . . . you're ogling Chill Guy's gyatt, huh?"
        tate "You zesty for Chill Guy?"
        mc "???"
        mc "Ummm, I mean . . ."
        mc "I haven't fully forgiven him yet. I need to know why he left me all those years ago."
        tate ". . ."
        tate "Life is but a walking skibidi.\n You better griddy as hard as you can."
        scene black
        pause 5.0
        show text "End of Chapter 2" with dissolve
        pause 1.0
        hide text with fade
        show text "Starting Chapter 3" with dissolve
        
        #bg fade to black. 
        # player returns to main screen?
        $ gyatt_coins = gyatt_coins +25

# cursor now says "Go o shool (day 3) fpr tje door"





    return


