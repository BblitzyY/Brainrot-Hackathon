define mc = Character(mcname, color="#ffffff", what_prefix='"', what_suffix='"')
define mci = Character("mcname", color="#ffffff", what_italic=True)
define mcn = Character(None, what_color="ffee8c")
define nug = Character("Dago", color="#ffa500", what_prefix='"', what_suffix='"')
define chill = Character("Chill Guy", color="#b0e0e6", what_prefix='"', what_suffix="'")
define gig = Character("???", color="#cbc3e3", what_prefix='"', what_suffix="'")
define amg = Character("Amongus Imposter", color="#c51111", what_prefix='"', what_suffix="'")
define emo = Character("Edgemund", color="#1c1c84", what_prefix='"', what_suffix="'")
define tom = Character("Tomato Boy", color="#ffc0cb", what_prefix='"', what_suffix="'")
define ksi = Character("KSI", color="#c8ffc8", what_prefix='"', what_suffix="'")
define quan = Character("Quandale Dingle Fairy", color="#1bfc06", what_prefix='"', what_suffix="'")
define ski = Character("Mr Skibidi Toilet", color="#cabd99", what_prefix='"', what_suffix="'")
define tate = Character("Andrew Tate", color="#d3d3d3", what_prefix='"', what_suffix="'")

# leaving gyatt coins code blank since it carries over from the very first variable definition 

label start: 
    scene black 
    pause 1.0 
    show text "Chapter 1 - Day 3" with dissolve
    pause 1.0 
    hide text with fade 
    play music "audio/bgm_buckle.mp3" fadein 1.0 volume 0.5 
    scene bg neighbourhood with dissolve

    mci "Ugh, Monday left me broken."
    mci "Tuesday, I was through with hoping."
    mci "And today I hope Chill Guy is at gym class this morning." 

    play sound "audio/sfx_dago" fadein 1.0 volume 1 
    show dago neutral
    nug "Ermmm, what the sigma, vro."
    nug "Are you late to class again?"

    menu:
        "There’s nothing I can say.": 
            mc "Yes. . ."
            nug "Then hurry up."
            nug "We’re going to be late."
            jump d3_cont_1
        "Wdym? I already went.": 
            gyatt += 100 
            mc "I bedwars built my way to school and back."
            nug "You can't be caught lacking like that."
            nug "Stop capping cuh."
            jump d3_cont_1 

    label d3_cont_1: 
        nug "Come on now."
        nug "We’re actually going to be late to morning gym class and you know how Mr Skibidi doesn’t fw that."
    
    mc "It’s not like {i}you’re{/i} on time every day."
    hide dago
    mcn "Dago was pretty quick to clear up my joke, huh."
    mcn "Not even a level 1000 mafia boss could make it to school in 10 minutes when we live 19.69 minutes away."
    show dago
    nug "Whatcha thinking, ya chicken nugget?"
    nug "Are you gonna skip class?"

    menu:
        "No, what if I miss out on Chill Guy’s master rizzin- I MEAN, nothing—uh I didn’t say anything.":
            mc "I just …kinda want to see him today." 
            hide dago
            mci "I can’t tell Dago the details about our past. . ."
            show dago
            nug "Yeah vro, wtv that means."
            nug "Hurry up, and let’s cue the Subway Surfers vibes already!"
            mc "Goofy ahh chicken nugget. Of course."
            hide dago
            mci "There's no way I’m already going to skip season 1 of Chill guy x Me!!"
            jump gym_class

        "Yuh, the thought of skipping class is already edging me.": 
            nug "Are you sure vro?"
            nug "There’s no going back from that."
            menu:
                "Yeah \'\vro\'\. It's like wtvs.":
                    mc "Let’s go to Sin City instead."
                    mc "I don’t feel like touching grass."
                    scene black with dissolve
                    jump sin_city
                "Hmm, no, actually skipping doesn’t sound like it has aura points anymore.":
                    mc "Let’s go to the gym and see if Chill Guy is around."
                    mc "You seem like you wanna hang with him too, so why not?"
                    scene black with dissolve
                    jump gym_class
    
    stop music fadeout 1.0

    label gym_class:
        scene bg gym with dissolve
        play music "audio/bgm_dti" fadein 1.0 volume 0.5
        hide dago

        mcn "Mr Skibid has instructed the whole class to play ball games."
        mcn "You see Chill Guy absolutely Duke Dennis-ing the court."
        mci "Look at his goddamn aura over there. . . !"
        mci "I’m so envious of his positive rizz."
        mci ". . .Kinda glad I came to school today."
        mci "Oh wait."
        stop music fadeout 1.0
        
        mci "What is {i}blud{/i} doing there?"
        play music "audio/bgm_thickofit" fadein 1.0 volume 0.5 

        show ksi at left
        ksi "Watch me!"
        mcn "KSI bounces volleyball up and down violently on the floor."
        show chill guy neutral at right with dissolve
        chill "Chill down KSI." 
        chill "You’re a big bomboclat with a boombox; so not bing chilling rn."
        hide ksi
        hide chill guy neutral
        with dissolve
        
        show dago
        dago "DAWG SCHMLAWG, YEAH!!"
        dago "We should totally, literally, ackshually go up and mew with them frfr."
        hide dago 

        mcn "A ball comes whizzing through the air and then some strange blob blocks your vision." with hpunch
        mcn "Is it a bird?"
        mcn "Is it a plane?"
        show chill guy neutral with dissolve
        mcn "OMG, IT'S CHILL GUY!!"
        hide chill with dissolve
        stop music fadeout 1.0
        
        play music "audio/bgm_dti"
        mcn "Evidently you've only just noticed that everyone’s playing volleyball."
        mci "Omg, is this my haikyuu moment??"
        mcn "You gasp in hinata senpai and blush with the thrill of opportunism."

        show chill guy neutral with dissolve
        chill "Dawg, you’re a bit too chill, you almost got hit and I wouldn’t be very chill with that."
        hide chill guy neutral with dissolve
        
        mci "I wonder which bomboclat would do that." 
        mci "He aimed right at my toes, huh. . ."
        mci "Does he have a foot fetish?" 

        show ksi with dissolve
        mcn "You look at KSI, who is hunched in the corner, seemingly listening in on their conversation."
        mci "Was it him?"

        default bandaid_scene = False
        menu:
            "Confront KSI.":
                gyatt += 100 
                mc "That was so beta of you, KSI."
                mc "You're acting kinda sus ngl."
                ksi "Womp womp, what a loser."
                jump d3_cont_2
            "Ignore it and fe!n pain.":
                ksi "Stop the cap, I didn’t do anything to you."
                ksi "I swear on a knee surgery tmr."
                $ bandaid_scene = True
                jump d3_cont_2

        label d3_cont_2: 
            mc "What is my mans on about?"
            mc "Is this a hidden biden trump love story??"
            mc "He keeps popping up whenever Chill Guy chan shows up." 
            hide ksi with dissolve 
            mcn "Chill Guy continues to berate KSI."
            show ksi at left
            show chill guy neutral at right
            with dissolve
            chill "Vro, that was so unchill of you. Negative social points for real."
            chill "What’s been up with you recently?"

            if bandaid_scene == True:
                chill "[mcname]"
                chill "Are you locked in rn, or nah?"
                chill "I'll come w/ you to sick bay 'cause you're not looking too skibidi."
                mcn "You notice a big gash on Chill Guy’s arm."
                mcn "There are bandaids in your backpack since you bring them every day, and you offer them."
                hide chill guy neutral
                mcn "I hope these band aids are able to fix my heart, too. . ."
                mcn "It’s beating lowk strangely."
                show chill guy neutral 
                chill "Hmm."
                chill "Thanks, [mcname]."
            scene black 
            with dissolve 
            stop music fadeout 1.0
        
        play sound "audio/sfx_bell.mp3" fadein 1.0 volume 0.5
        scene bg cafeteria with dissolve 
        play music "audio/bgm_cafeteria.mp3" fadein 1.0 volume 0.4 
        mcn "After gym class, everyone is hella knocked out."
        mcn "Mr Skibidi gives y\’\all lunch credit since it\’\s his birthday today."
        
        show dago with dissolve
        dago "[name] you weren’t capping when you said Chill Guy got a gigantic enormous boo boo!!"
        mcn "Dago dramatically looks around."
        dago "OMG it’s Chill Guy chan again!"
        mcn "He waves Chill Guy over, much to your chagrin."
        dago "Yo Chill guy?!!! You should come chug jug with me and my gang."
        hide dago with dissolve

        mci "I think I’m tripping."
        mci "Did Dago just invite Chill Guy to chug with us?"
        mci "Also what does he mean by \‘\my gang\’\?"
        mci "I’m the only one here???"
        mci "Am I tripping too???"

        show chill guy neutral with dissolve
        mcn "There’s a whole crowd close surrounding Chill Guy now, and its highkey making you anxious."
        hide chill with dissolve
        mcn "Was he always that popular, or did you just fail to notice?"
        mcn "Chill guy notices you and Dago, and slowly turns around."
        show chill guy neutral with dissolve
        mcn "His nonexistent hair dances in the nonexistent wind, and nonexistent cherry blossoms blow around him like he’s in a shojo manga."

        play sound "audio/sfx_shalala.mp3" fadein 1.0 volume 0.3 
        chill "What’s up dawgs?"
        chill "You guys feeling cool?"
        chill "'Cos I'm feeling pretty cool in here."
        
        show dago at right
        dago "Is vro feeling better?"
        dago "I typed F in the chat just for you."
        chill "I’m gassed."
        chill "But we ball. Didn’t hurt."

        play sound "audio/sfx_fein.mp3" fadein 1.0 volume 0.3
        chill "Looks pretty fe!n to me."
        hide dago 
        hide chill 
        mcn "Chill Guy nonchalantly sits down next to you."
        stop music fadeout 1.0

        mci "OMG OMG OMG he’s so close. . ."
        mci "I could literally whisper ‘I like your cut G’ in his ear rn."

        show dago
        dago "Where’s that mouth breather that’s normally in your gang?"
        dago "Is he grounded yet?"
        hide dago 

        play music "audio/bgm_thickofit.mp3" fadein 1.0 volume 0.5
        mcn "KSI suddenly pulls up to the lunch table and shoves you to the side, dumping a grimace shake onto your head."
        show ksi 
        ksi "Oh, my bad unc."
        ksi "I could smell your yappuccino from the lunch line."
        show chill guy neutral with dissolve at right 
        chill "Zesty ahh mf."
        chill "That’s not very chill of you KSI, you jelly of [mcname] or something?"
        chill "[mcname], you feeling swagger?"
        chill "I can have a chat with KSI for you."
        hide chill with dissolve

        mcn "You frown at KSI."
        mc "Yeah, you crusty foot licker."
        mc "Can you even see where you’re going with that big ahh forehead."
        mc "I could dock a plane there and still have space lef-"
        stop music fadeout 1.0

        mcn "A shadow appears over your shoulder."
        play music "audio/bgm_skibidi" fadein 1.0 volume 0.5
        show skibidi angry
        ski ". . ."
        ski "Y’all gotta stop gooning during lunch."
        ski "Detention, all of you."
        show dago at right
        dago "Ermmm Sensei, I didn’t do anything though."

        menu:
            "Stand up for Dago.":
                gyatt += 100 
                mc "Yeah KSI’s always capping."
                mc "Swear on my knee surgery tomorrow that Dago’s clean."
                jump d3_cont_3
            "Try to sneak away.":
                jump d3_cont_3
            "Hide behind Chill Guy.":
                jump d3_cont_3
        
        label d3_cont_3:
            ski "Nuh uh. Can't be doing it like that."
            ski "Minus 10,000 bands."
            ski "Like I said, detention. All of you."
            hide skibidi
            mci "F in the chat. . ."
            mci "He really just pulled an uno reverse on all of us."
            scene black with dissolve 
            jump detention 

    label sin_city:
        show dago 
        dago "So. . . where do you wanna use your Fortnite Battle Pass today?"
        mc "Are we gonna go touch grass?"
        dago "Nah, vro, we can go to Sin City though?"
        dago "Or take a visit to the Backrooms?"
        dago "Just gotta be back before GTA 6 comes out."

        menu: 
            "Sin City. Then maybe I can build up more alpha aura.":
                dago "Let’s go back to my gronk cave and shift from there."
                jump sin_city_2 
            "Backrooms? What in the skibidi is that? We could check it out. . .":
                dago "Actually nahh, the Backrooms have like negative aura points lowkey."
                dago "I can’t be seen with a negative social credit."
                dago "Let’s just go Sin City instead."
                dago "But good on ya for having the guts."
                jump sin_city_2 
        
        label sin_city_2:
            hide dago 
            mcn "You follow Dago back to his house obediently, but then you notice some sort of force pulling you towards the lake nearby."
            scene bg lake with dissolve 
            play music "audio/bgm_usher.mp3" fadein 1.0 volume 0.5 

            mci "This is… Lake Reddit."
            mci "I think I’ve heard about this before."
            mci "A lake so abundant of incel energy that it repels actual celibates."

            show dago
            dago "Wait, whose immense aura is this?"
            dago "It's coming from that direction."
            mc "Is it just me, or do we feel more chill now?"
            mcn "You feel some kind of chilly breeze blanket you, but it’s not to the point of freezing."
            mcn "It’s like pressing a slightly chilled bottle of Prime to your face."
            dago "Vro. . ."
            dago "Is that Chill Guy over there on the park bench? He’s so based."

            show chill guy neutral
            mcn "You notice that Chill Guy has fallen asleep on the grass next to the lake."
            menu: 
                "Give him your jacket.":
                    gyatt += 100
                    mcn "You start stripping and give him your trench coat, shrinking you to just a petit kid."
                    mcn "Dago turns to whispering to avoid waking Chill Guy up."
                    show dago with dissolve
                    dago "Damn vro, that was so straightforward. So skibidi even."
                    dago "Whatchu gon’ do now?"
                    jump d3_cont_4

                "Wake him up with your sweet singing.":
                    mc "Zao Shang HAo zhongguo."
                    mc "Shen zai wo you bing chilling!!"
                    hide chill guy neutral with dissolve
                    mcn "Chill Guy stirs, and through a languid fog realises that he is surrounded by you and Dago."
                    show chill guy neutral with dissolve 
                    chill ". . ."
                    mc ". . ."
                    chill "Ayo, the pizza here."
                    mc "Evidently Chill guy isn’t in his right mind."
                    jump d3_cont_4
            
            label d3_cont_4:
                mc "Dago, don’t you think he’s being a little baka rn?"
                # independent event
                menu: 
                    "Should we griddy him back to school?":
                        dago "Yeah, good idea vro."
                        jump d3_cont_5 
                    "Take Chill Guy back to your house and see how freaky you get…":
                        mcn "Just joking. Or are you?"
                        jump chill_crib

            label d3_cont_5:
                play sound "audio/sfx_footsteps.mp3" fadein 1.0 volume 0.5
                scene bg hallway1 with fade 
                play music "audio/bgm_skibidi.mp3" fadein 1.0 volume 0.5
                mcn "As the two of you heave a half-conscious Chill Guy back into school, you spot Mr Skibidi patrolling the hallways."
                mcn "You feel a tingling sensation in your neck."
                mcn "Your alpha energy is detecting something sus."

                scene bg hallway2 with fade
                show ksi with dissolve at left 
                mcn "You look behind you and you see KSI peeking out behind a corner."
                hide ksi with dissolve
                mcn "You ignore it, but find it strange anyways that he’d stalk you instead of just talking."
                mcn "Then comes an authoritative tap on your shoulder."

                show skibidi neutral with dissolve
                ski "Skipping class again, [mcname]?"
                ski "That is like the opposite of having goated glizzies with the sauce."
                ski "Detention. All of you."

                show dago with dissolve at left 
                dago ":("
                hide dago 
                scene black 
                with dissolve 
                stop music fadeout 1.0
                jump detention
                   
        label detention:
            scene bg basement with dissolve 
            show skibidi neutral with dissolve
            ski "Aight yall smurf cats."
            ski "Y’all know what detention is, right?"
            ski "You will now have to sit here and practice for your Mewing 101 test tomorrow."
            play music "audio/bgm_exam.mp3" fadein 1.0 volume 0.5 
            hide skibidi
            
            mcn "Reluctantly, you start doing your looksmaxxing homework, even as your mind starts drifting away."
            mcn "Your eyes subconsciously come to rest on Chill Guy’s figure in the seat next to you, who is now fully conscious."
            show chill guy neutral with dissolve 
            chill "Uh [mcname], why are you staring at me like that?"
            chill "You jelly of my mewing skills?"
            hide chill guy neutral with dissolve

            mcn "You feel some burning eyes on the back of your neck."
            mcn "Someone is draining your aura." 
            mcn "You peer around the room, and see KSI at the window slit of the door, who magically avoided this goon cave you all were trapped in."

            show ksi with dissolve 
            mci "Is he spying on us? Some stalker type shit. . ." 
            hide ksi with dissolve 

            show dago neutral with dissolve 
            dago "I’m gonna take a quick nap."
            dago "It's okay, I can mew in my sleep."
            hide dago 

            show chill guy neutral with dissolve 
            mcn "Slowly, Chill Guy’s calm aura next to you slows you down and you end up falling asleep as well."
            hide chill guy neutral with dissolve 
            mci "Shit. . . how is his aura able to make me so calm?"
            mci "Shouldn’t he be losing brain cells over me trying to ignore him sometimes. . . ?"
            mci ". . ."
            mci "Whatever. . ."
            scene black with dissolve 
            play sound "audio/sfx_snore.mp3" volume 1.0 
            pause 1.0 
            mcn "After about ate minutes, you’re somehow awoken by a burst of sigma energy nearby."
            
            scene bg nighttime streets with dissolve 
            play music "audio/bgm_meow.mp3" fadein 0.5 volume 0.5
            mcn "You’re being carried. . . princess style."
            show chill guy neutral with dissolve 
            mcn "You’re being carried princess style back home BY CHILL GUY."
            mc ". . . !!!!"
            mcn "Chill Guy doesn’t seem fazed, as per usual."
            chill "You okay?"
            chill "You seemed so chill I didn’t want to wake you when it ended, and Dago’s off cooking for the Tiktok Rizz Party tomorrow."
            chill "We have detention again too, for falling asleep."

            mci "I-I-I’m being carried?" 
            mci "By you??? Chill Guy???"
            mci "What a smurf cat type dream. . ."
            hide chill guy neutral with dissolve 
            mci "Uh- what? Wait, is that the guy from the convenience store?" 
            mci "Or am I just tripping?" 
            mcn "You feel yourself seeping slowly back into a state of subconsciousness."

            stop music fadeout 0.5
            scene black with dissolve 
            play music "audio/bgm_gigachad.mp3" fadein 1.0 volume 0.5 
            show gigachad with dissolve 
            mcn "The chad man who you assume works part-time at night at the local convenience store somehow magically appears out of thin air in front of you."
            gig "A gigachad is the master of his own destiny."
            gig "Become a gigachad today. Better call Saul."
            hide gigachad 
            scene bg nighttime streets 
            with dissolve 
            stop music fadeout 0.5
            pause 1.0 
            
            play music "audio/bgm_meow.mp3" fadein 1.0 volume 0.5
            mc ". . ."
            mcn "You think you might be hallucinating."
            show chill guy neutral with dissolve 
            chill "Go back to sleep, sweet cheeks."
            chill "What’s your addy?"
            mci "Did he just call me \‘\sweet cheeks\’\???"
            mci "What on earth. . ."
            mc "Uh, it’s 420 Kumalala Savesta Road. . ."
            pause 1.0
            mci "How am I knocked out this bad to be turning into a simp?"
            hide chill guy neutral with dissolve 
            
            scene black with fade 
            stop music fadeout 1.0 
            mcn "You fall back asleep, only to be woken again by a familiar voice."
            mci "God."
            mci "This day is {i}intense{/i}."

            show tate with dissolve 
            tate "The problem is, this is basically all women’s fault!"
            tate "Whatever you’re doing wrong, it sounds like a skill issue."
            mci "Um. . ."
            mci "This isn't even my dream???"
            tate "Sounds like a skill issue."
            hide tate 
            scene bg bedroom 
            with dissolve 

            play music "audio/bgm_symphony.mp3" fadein 1.0 volume 0.5 
            mcn "You wake up on your bed with a semblance of consciousness, just remembering how Chill Guy helped you hobble into your own home."
            mci "Maybe he has his own reasons for leaving me in Florida. . ."
            mci "Otherwise, why would he be so nice to me when I’ve done nothing nice for him?"

            mci "But. . ."
            mci "I wonder what Chill Guy thought of me today, kyaaaah."
            mci "Just thinking about him makes me nervous."
            mci "Maybe I can let the ship sail, and rizz him up after all." 
            mci "After my leg surgery, maybe. . ."
            jump end_screen

        label chill_crib:
            show dago neutral with dissolve 
            dago "You’re gonna lose aura points if you get us lost."
            dago "Your goon cave’s legitimately that way, right?"
            hide dago neutral with dissolve 

            mci "Kyaaaah, I'm about to have a sugar crash."
            mci "Crush- I mean, Chill Guy is. . ."
            mci "Wait. . ."
            mci "CHILL GUY IS COMING TO MY HOUSE?"

            show chill guy neutral with dissolve 
            chill "Hey vro are you afk?"
            chill "Blud, looks like you gonna have trouble griddying." 
            mc "Yeah, yeah I’m doing fine."
            mc "But something feels a bit uncanny right now, innit?"
            mc "Feels lowkey like smth is gonna change."

            show dago neutral with dissolve at left 
            dago "YOU GRONKATRONS HAVE LORE????"
            hide dago neutral with dissolve at left 
            mcn "You feel a sudden cold blast coming from Chill Guy’s direction."
            mc ". . . ?"
            mc "Hey Chill Guy. . ."
            mc "Did you just fart?"
            mc "On me?"
            mci "Did he just try rizz me up with a fart?"
            mci "Ohio must have really changed him." 
            mcn "Another cold wind blows, and you shiver a bit."
            mcn "Chill Guy unexpectedly takes off his grey hoodie, and wraps it around your shoulders."

            menu:
                "Ask if you all can griddy a bit faster home.":
                    gyatt += 100 
                    mcn "You just picked up +100 gyatt coins."
                    mc "I don’t want you to catch a cold because of me."
                    jump d3_cont_6

                "Ask Chill guy for his jacket too, cause evidently Dago doesn’t have one.":
                    mc "Errrm, Chill Guy, could you give your comfy warm jumper over?"
                    mcn "Chill Guy takes off his jumper too for Dago."
                    mcn "You kinda regret asking him now. Can he withstand this much cold?"
                    mcn "You feeling like you’re cooking now?"
                    mcn "Not really?"
                    mcn "Thought so." 
                    jump d3_cont_6

            label d3_cont_6:
                mcn "Dago faces you."
                show dago neutral with dissolve 
                dago "We should really get inside quick"
                dago "I didn’t know Ohio weather could get this bad."

                mcn "As you look at Dago, you spot the shadowed silhouette of a person near an alleyway."
                mcn "Is that. . ."
                mcn "KSI stalking us?"

    label end_screen:
                scene black 
                pause 2.0 
                stop music fadeout 1.0
                mcn "More chapters coming soon!"
                mcn "Thanks for playing the beta."
                jump main_screen

    return 
