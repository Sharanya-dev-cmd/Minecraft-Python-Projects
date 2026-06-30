# 13 June 2026

# stage 0 = home prep (before leaving home)

score = 0

has_blocks = input("do you have blocks? : ").lower()
if has_blocks == "yes" :
    num_blocks = int(input("how many blocks do you have? : "))
    if num_blocks >= 128 :
        score = score + 1
        print("great! you can pillar up obsidian towers to break end crystals, escape angry endermen, or bridge across small islands")
    elif num_blocks < 128 :
        print("you will need 2 or more stacks of blocks to survive in the end efficiently")
    else :
        print("invalid input. please try again")
elif has_blocks == "no" :
    print("you will need 2 or more stacks of blocks to survive in the end efficiently")
else :
    print("invalid input. please try again")


has_water_buckets = input("do you have water buckets? : " ).lower()
if has_water_buckets == "yes" :
    num_buckets = int(input("how many water buckets do you have? : "))
    if num_buckets >= 3 :
        score = score + 1
        print("great! you will be able to MLG, repel endermen, and scale the towers safely")
    elif num_buckets < 3 and num_buckets >= 0 :
        print("you need water buckets to survive efficiently in the end")
    else :
        print("invalid input. please try again")
elif has_water_buckets == "no" :
    print("you need water buckets to survive efficiently in the end")
else :
    print("invalid input. please try again")


full_armor = input("do you have a full set of armor? : ").lower()
if full_armor == "yes" :
    type_armor = input("is your armor made of leather, gold, iron, diamond or netherite? : ").lower()
    if type_armor == "leather" :
        print("this is a bad choice of armor to wear to the end. carry iron armor or better")
    elif type_armor == "gold" :
        print("this is not a great choice of armor to wear to the end. carry iron armor or better, but if unable to, enchant your armor for increased survival chances")
    elif type_armor == "iron" :
        score = score + 0.3
        print("great! this is a solid, reliable choice of armor material. for the best, enchant it")
    elif type_armor == "diamond" :
        score = score + 0.7
        print("great! this is a great choice of armor material. for the best, enchant it")
    elif type_armor == "netherite" :
        score = score + 1
        print("amazing! this is the best choice of armor material. if you wish, enchant it")
    else :
        print("invalid input. please try again")
elif full_armor == "no" :
    print("WARNING : you need iron armor or better to survive in the end")
else :
    print("invalid input. please try again")


has_sword = input("do you have a sword? : ").lower()
if has_sword == "yes" :
    type_sword = input("what is your sword made up of? : ").lower()
    if type_sword == "wood" :
        print("this is a horrible choice of sword material to fight the ender dragon and other end mobs. upgrade sword")
    elif type_sword == "stone" :
        print("this is not a great choice of sword material to fight the ender dragon and other end mobs. upgrade sword")
    elif type_sword == "gold" :
        print("this is not a great choice of sword material to fight the ender dragon and other end mobs. upgrade sword or enchant it")
    elif type_sword == "iron" :
        score = score + 0.4
        print("this is a good, reliable choice of sword material to fight the ender dragon and other end mobs. if you wish, enchant it (highly recommended)")
    elif type_sword == "diamond" :
        score = score + 0.7
        print("this is a great choice of sword material to fight the ender dragon and other end mobs. if you wish, enchant it for better results")
    elif type_sword == "netherite" :
        score = score + 1
        print("this is an amazing choice of sword material to fight the ender dragon and other end mobs. if you wish, enchant it")
    else :
        print("invalid input. please try again")
elif has_sword == "no" :
    print("won't you need a sword to do hand-to-hand combat with endermen and attack the dragon from close range and stuff?!!! 😤")
else :
    print("invalid input. please try again")


has_bow = input("do you have a bow? : ").lower()
if has_bow == "yes" :
    has_arrows = input("do you have arrows? : ").lower()
    if has_arrows == "yes" :
        num_arrows = int(input("how many arrows do you have? : "))
        if num_arrows >= 32 :
            score = score + 1
            print("you have enough arrows to fight the ender dragon")
        elif num_arrows < 32 and num_arrows >= 0 :
            print("you will need more arrows to defeat the ender dragon")
        else :
            print("invalid input. please try again")
    elif has_arrows == "no" : 
        print("you will need arrows to use your (currently useless) bow (DUH 🙄🙄)")
    else :
        print("invalid input. please try again")

    bow_durability = input("is your bow's durability low, mid or high? : ").lower()
    if bow_durability == "low" : 
        print("you will need to craft a new one or enchant your bow")
    elif bow_durability == "mid" :
        print("you can fire a decent amount of arrows. consider enchanting or crafting a new one")
    elif bow_durability == "high" :
        score = score + 1
        print("great! you can fire a good number of arrows (around 385 uses)")
    else :
        print("invalid input. please try again")

    ask_bow = input("is your bow enchanted? : ").lower()
    if ask_bow == "yes" :
        type_enchantments = input("what is your bow enchanted with? : ").lower()
        if type_enchantments == "power" :
            power = input("is your bow power I, II, III, IV, or V? : ").upper()
            if power == "I" :
                score = score + 0.2
                print("nice! arrow damage increase =  50% , approx. total damage = 14 damage (7 hearts)")
            elif power == "II" :
                score = score + 0.4
                print("great! arrow damage increase =  +75% , approx. total damage = 16 damage (8 hearts)")
            elif power == "III" :
                score = score + 0.6
                print("spectacular! arrow damage increase =  +100% , approx. total damage = 18 damage (9 hearts)")
            elif power == "IV" :
                score = score + 0.8
                print("amazing! arrow damage increase =  +125% , approx. total damage = 20 damage (10 hearts)")
            elif power == "V" :
                score = score + 1
                print("stunning! arrow damage increase =  +150% , approx. total damage = 23 damage (11.5 hearts)")
            else :
                print("invalid input. please try again")

        elif type_enchantments == "unbreaking" :
            unbreaking = input("is your bow's unbreaking level I, II, or III? : ").upper()
            if unbreaking == "I" :
                score = score + 0.4
                print("great! this gives roughly a 30% chance that firing an arrow won't use up a durability point")
            elif unbreaking == "II" :
                score = score + 0.7
                print("wow! this gives roughly a 40% chance that firing an arrow won't use up a durability point")
            elif unbreaking == "III" :
                score = score + 1
                print("amazing!  this gives roughly a 25% chance that the bow will last about four times longer than usual.")
            else :
                print("invalid input. please try again")

        elif type_enchantments == "punch" :
            print("FYI : this enchantment only alters knockback distance, it does not increase the base damage dealt by the arrow")
            punch = input("if you bow's punch level I or II? : ").upper()
            if punch == "I" :
                print("great! you will be able to knock your target back by roughly 3 blocks")
            elif punch == "II" :
                print("wow! you can push your target back by about 6 blocks")
            else :
                print("invalid input. please try again")

        elif type_enchantments == "flame" :
            print("amazing! you can set your target on fire, inflicting ongoing damage, and ignite blocks like tnt")

        elif type_enchantments == "infinity" :
            score = score + 1
            print("stunning! this lets you shoot unlimited regular arrows as long as you have at least 1 arrow in your inventory")

        elif type_enchantments == "mending" :
            score = score + 1
            print("great! this repairs your bow using gathered experience instead of requiring another bow at an anvil")
            
    elif ask_bow == "no" :
        print("applying essential bow enchantments can drastically change your ranged combat. if you wish, enchant your bow")
    else :
        print("invalid input. please try again")
elif has_bow == "no" :
    print("you will need a bow and some arrows to defeat the ender dragon, and break end crystals with minimal risks")
else :
    print("invalid input. please try again")


has_shield = input("do you have a shield? : ").lower()
if has_shield == "yes" :
    shield_durability = input("is your shield's durability low, mid or high? : ").lower()
    if shield_durability == "low" :
        print("repair your shield or enchant it to ensure it doesn't break in the middle of combat")
    elif shield_durability == "mid" :
        print("please repair or enchant your shield for max. benefits")
    elif shield_durability == "high" :
        print("great! you will get an advantage in the end and defeat the dragon a little less painfully")
    else :
        print("invalid input. please try again")
elif has_shield == "no" :
    print("you may need a shield to defeat the dragon with minimal risks")
else :
    print("invalid input. please try again")


has_bed = input("do you have a bed? : ").lower()
if has_bed == "yes" :
    score = score + 0.5
    print("great! place your bed near the stronghold in case you die in the end. respawning at home can be a bit rough 😕")
elif has_bed == "no" :
    print("won't you need a bed to place near the stronghold?!! unless you want to respawn back at home if you die 😇 👉👈")
else :
    print("invalid input. please try again")


eyes_of_ender = input("do you have eyes of ender? : ").lower()
if eyes_of_ender == "yes" :
    num_eyes = int(input("how many eyes of ender do you have? : "))
    if num_eyes >= 20 :
        score = score + 1
        print("you have enough eyes to locate the stronghold and activate the portal")
        print("TIP : if you wish, consider carrying spare eyes as they can break while locating a stronghold")
    elif num_eyes < 20 and num_eyes >= 0 :
        print("you will need more eyes of ender to locate the stronghold and activate the end portal")
        print("TIP : after collecting a decent number of eyes, carry some spare ones as some eyes can break while locating a stronghold")
    else :
        print("invalid input. please try again")
elif eyes_of_ender == "no" :
    print("umm...how exactly are you planning to find a stronghold without eyes of ender? divine intervention?")
else :
    print("invalid input. please try again")


has_food = input("do you have food? : ").lower()
if has_food == "yes" :
    type_food = input("do you have cooked beef, cooked porkchops, golden carrots or golden apples? : ").lower()    # what if user has many types of food? fix later cuz you can't leave something so stupid existing in your code
    if type_food == "cooked beef" :
        num_beef = int(input("how much beef do you have? : "))
        if num_beef >= 64 :
            score = score + 1
            print("this is a great choice of food! you have enough food to last for a long journey in the end")
            print("TIP : if you run short on good food, salmon and bread are great substitutes")
        elif num_beef < 64 :
            print("you will need more food to survive in the end")
        else :
            print("invalid input. please try again")
    elif type_food == "cooked porkchops" :
        num_pork = int(input("how much porkchop do you have? : "))
        if num_pork >= 64 :
            score = score + 1
            print("this is a great choice of food! you have enough food to last for a long journey in the end")
            print("TIP : if you run short on good food, salmon and bread are great substitutes")
        elif num_pork < 64 :
            print("you will need more food to survive in the end")
        else :
            print("invalid input. please try again")
    elif type_food == "golden apples" :
        num_apples = int(input("how many apples do you have? : "))
        if num_apples >= 16 :
            score = score + 1
            print("wow! you will get an extra 2 hearts on consumption in case you are struggling to slay the dragon. you have enough food to last for a long journey in the end")
            print("TIP : if you run short on good food, salmon and bread are great substitutes")
        elif num_apples < 16 :
            print("you will need more food to survive in the end")
        else :
            print("invalid input. please try again")
    elif type_food == "golden carrots" :
        num_carrots = int(input("how much porkchop do you have? : "))
        if num_carrots >= 16 :
            score = score + 1
            print("great! golden carrots have extremely high saturation levels in minecraft! you have enough food to last for a long journey in the end")
            print("TIP : if you run short on good food, salmon and bread are great substitutes")
        elif num_carrots < 16 :
            print("you will need more food to survive in the end")
        else :
            print("invalid input. please try again")
    else :
        print("invalid input. please try again")
elif has_food == "no" :
    print("WON'T YOU NEED FOOD TO NOT DIE IN A PATHETIC WAY WHILE FIGHTING THE ENDER DRAGON??! geez😒")
else :
    print("invalid input. please try again")


has_pickaxe = input("do you have a pickaxe? : ").lower()
if has_pickaxe == "yes" :
    pickaxe_material = input("what is your pickaxe made up of? : ").lower()
    if pickaxe_material == "wood" :
        print("this is a terrible choice of material to take to the end. you can mine end stone, but very slowly, and you won't be able to mine most crucial blocks. that sucks, so upgrade your pickaxe")
    elif pickaxe_material == "stone" :
        print("you can mine end stone and iron rods. however, you won't be able to mine most crucial blocks. not cool. upgrade pickaxe if you want to")
    elif pickaxe_material == "gold" :
        print("you can mine end stone, end stone bricks, and purpur blocks. if you wish, upgrade pickaxe")
    elif pickaxe_material == "iron" :
        score = score + 0.6
        print("great! you can mine most important blocks. ensure the durability is high")
    elif pickaxe_material == "diamond" :
        score = score + 0.8
        print("great! you can mine the most important blocks. ensure the durability is high")
    elif pickaxe_material == "netherite" :
        score = score + 1
        print("great! you can mine the most important blocks. ensure the durability is high")
    else :
        print("invalid input. please try again")
elif has_pickaxe == "no" :
    print("you will need a pickaxe to mine crucial finds")
else :
    print("invalid input. please try again")


has_potions = input("do you have potions? : ").lower()
if has_potions == "yes" :
    type_potion = input("what type of potions do you have? : ").lower()
    if type_potion == "slow falling" :
        num_slow_falling = int(input("how many slow falling potions do you have? : "))
        if num_slow_falling >= 4 :
            score = score + 0.5
            print("great! this prevents fall damage and causes you to float down gently when knocked around")
        elif num_slow_falling < 4 :
            print("you may need slow falling potions to survive with minimal risks while fighting the ender dragon")
        else :
            print("invalid input. please try again")
    elif type_potion == "healing" :
        num_healing = int(input("how many healing potions do you have? : "))
        if num_healing >= 4 :
            score = score + 0.5
            print("great! you won't always have time to stop and eat during combat. this restores your health instantly")
        elif num_healing < 4 :
            print("you may need potions of healing to restore health instantly while fighting the ender dragon")
        else :
            print("invalid input. please try again")
    elif type_potion == "regeneration" :
        num_regeneration = int(input("how many potions of regeneration do you have? : "))
        if num_regeneration >= 3 :
            score = score + 0.5
            print("nice! this is great for keeping your health topped off while managing crowds of endermen or taking consistent damage")
        elif num_regeneration < 3 :
            print("you may need potions of regeneration to keep your health topped off during emergencies")
        else :
            print("invalid input. please try again")
    elif type_potion == "strength" :
        num_strength = int(input("how many strength potions do you have? : "))
        if num_strength >= 4 :
            score = score + 0.5
            print("nice! this speeds up taking down the ender dragon and provides an edge when swarmed by endermen")
        elif num_strength < 4 :
            print("you may need potions of strength to speed up your dragon battle")
        else :
            print("invalid input. please try again")
    else :
        print("invalid input. please try again")
elif has_potions == "no" :
    print("you will need potions to gain some seriously cool advantages in combat")
else :
    print("invalid input. please try again")
# rn player can choose only one. fix later


has_totem = input("do you have a totem of undying? : ").lower()
if has_totem == "yes" :
    score = score + 0.5
    print("amazing! this saves you from lethal damage. however, it won't save you from falling into the void")
elif has_totem == "no" :
    print("that's fine. but if you want a serious advantage, obtain this. \nTO OBTAIN : \n1. defeat an evoker (found in woodland mansions) \n2. : triggering a raid in a village by obtaining the bad omen effect will cause evokers to spawn, typically during the fifth wave. raids are a much faster and renewable way to farm multiple totems (thank me later)")
else :
    print("invalid input. please try again")


print("\n----- END PREPARATION REPORT -----")

if score >= 10:
    print("outstanding preparation")
elif score >= 7:
    print("excellent preparation")
elif score >= 5:
    print("decent preparation")
else:
    print("risky expedition")

print("your final score = ", score)

# FIXES FOR DUMBLY STYLED GAME DESIGNS - stage 0
# in final check, mention what is missing
# after invalid input... the question ain't asked again. fix later
# what if user types words instead of numbers? -> num_arrows, etc : eg answer -> how many arrows? - a lot = crash

# stage 1 = finding the stronghold

if score >= 7.8 :
    print("you are ready for a good trip to the end!")
    continue_anyways = "yes"
else :
    print("you may need more resources and tools")
    continue_anyways = input("do you want to visit the end anyway? :").lower()


if continue_anyways == "yes" :
    print("love the recklessness! so...")

    num_eyes = int(input("how many eyes of ender you you have? : "))
    if num_eyes >= 20 :
        follow_eyes = input("do you know how to throw and follow eyes of ender? : ").lower()
        if follow_eyes == "yes" :
            spare_eyes = input("do you have spare eyes? : ").lower()
            if spare_eyes == "yes" :
                print("great! start following your eyes of ender and don't worry about running out :)")
            elif spare_eyes == "no" :
                print("that's fine. but be careful as eyes break sometimes when thrown")
            else :
                print("invalid input. please try again")
        elif follow_eyes == "no" :
            print("hold the eye and press the 'use' button (right click on pc, l2 on playstation, lt on xbox). it will float upwards, pointing toward the nearest hidden stronghold. follow it, throwing it periodically until it points down, which means 'start digging'")
        else :
                print("invalid input. please try again")
    elif num_eyes < 20 and num_eyes >= 15 :
        print("you have a decent number of eyes. if possible craft more, otherwise just start finding the stronghold")
    elif num_eyes < 15  and num_eyes >= 7 :
        print("errr... you will need some more eyes, but try your luck and just wing it :)")
    elif num_eyes < 7 :
        print("bro, you will not be finding the stronghold today")
    else :
        print("invalid input. please try again")
        # even if eyes < 7, the check continues. fix later

    print("let's do a final travel check before you run off to find your stronghold :) ->")
    
    has_bed = input("have a bed? : ").lower()
    if has_bed == "yes" :
        print("ensure that you place your bed near the stronghold to reset your spawn point")
    elif has_bed == "no" :
        print("err.. okay. try not to die!")
    else :
        print("invalid input. please try again")

    extra_food = input("do you have extra food for travel? : ").lower()
    if extra_food == "yes" :
        print("👍")
    elif extra_food == "no" :
        print("fine, eat sparingly or hunt some animals along the way to eat so that you don't die before you even reach the end. that would just be like -3000 aura")
    else :
        print("invalid input. please try again")

    boat_or_horse = input("do ya have a boat or a horse to travel faster on water and land respectively? : ").lower()
    if boat_or_horse == "yes" :                                                          # later distinguish between boat, horse, both, or neither
        print("good. your hunger bar will deplete slower and you shall reach faster too")
    elif boat_or_horse == "no" :
        print("that's fine. these will just help you reach faster and more efficiently")
    else :
        print("invalid input. please try again")

    print("TIP : ensure you carry weapons as well because hostile mobs will attack you and you can kill some animals if you run low on food")
    
    found_stronghold = input("did you find the stonghold? : ").lower()
    if found_stronghold == "yes" :
        empty_frames = int(input("how many frames do not have eyes of ender naturally in them? : "))
        if empty_frames <= num_eyes :
            print("great! place your eyes in the vacant frames to activate the portal")
        elif empty_frames > num_eyes :
            print("hard luck bro :| go back to the overworld, craft ", empty_frames - num_eyes , "more eyes of ender and return")
        else :
            print("invalid input. please try again")
    elif found_stronghold == "no" :
        print("that's fine. keep following your eyes of ender. if they point downwards, start digging (in a staircase to avoid falling into lava or something)")
    else :
        print("invalid input. please try again")
elif continue_anyways == "no" :
    print("that's okay. collect more resources and come back again :)")
else :
    print("invalid input. please try again")
# even if the player has chose to discontinue, the remaining stages still appear. thats dumb. fix later


# stage 2 = entering the end + prep for dragon fight

spawn_safely = input("did you spawn safely? : ").lower()
if spawn_safely == "yes" :
    print("perfect! start destroying the end crystals and avoid eye contact with the endermen or you'll end up as a snack")
elif spawn_safely == "no" :
    spawn_location = input("did you spawn inside the obsidian or on a tiny platform away from the island? : ").lower()
    if spawn_location == "inside obsidian" :
        print("mine your way out if you have a suitable pickaxe or else you're stuck there for a while")
    elif spawn_location == "platform" :
        print("use the blocks you have and carefully bridge your way to the main end island (TIP : use the 'shift' button so you don't fall)")
    else :
       print("invalid input. please try again")
else :
    print("invalid input. please try again")


on_main_island = input("are you now on the main end island? : ").lower()
if on_main_island == "yes" :
    looked_at_enderman = input("have you made eye contact with an enderman? : ").lower()

    if looked_at_enderman == "yes" :
        print("hurry!")
        print("use a bucket of water at your feet, or")
        print("create a 2 block high shelter and stand underneath it")
        print("or just pillar up 4 blocks, but the above point is safer as many endermen can gather underneath while you're protected")
        print("if you don't have water buckets or blocks, fight them or pray and run")
    elif looked_at_enderman == "no" :
        print("phew! avoid doing this at all costs or wear a carved pumpkin on your head as this get annoying quickly \nfocus on destroying all end crystals")
    else :
        print("invalid input. please try again")

    caged_crystals = input("are there any caged crystals? : ").lower()
    if caged_crystals == "yes" :
        print("pillar up or something and break those iron bars using your pickaxe (that is if you have one)")
    elif caged_crystals == "no" :
        print("you are very lucky. focus on slaying the dragon now")
    else :
        print("invalid input. please try again")

    destroying_crystals = input("have you started destroying all end crystals? : ").lower()
    if destroying_crystals == "yes" :
        print("great! the dragon shall sonn not be able to heal. you will be able to slay it faster")
        used_bow = input("are you using a bow to destroy the crystals? : ").lower()
        if used_bow == "yes" :
            print("great! this is usually the safest method")
        elif used_bow == "no" :
            print("be careful when climbing towers as crystals explode when destroyed. place a water bucket directly behind you as when you take the knockback force, you can travel down safely")
        else :
            print("invalid input. please try again")
    elif destroying_crystals == "no" :
        print("start destroying them first or the dragon will keep healing, making it harder to kill later (a stitch in time saves nine 🤫)")
    else :
        print("invalid input. please try again")

    knocked_off_tower = input("have you been knocked off a tower? : ").lower()
    if knocked_off_tower == "yes" :
        consumed_slow_falling = input("have you consumed a slow falling potions? : ").lower()
        if consumed_slow_falling == "yes":
            print("you're fine. you can casually float back down safely")
        elif consumed_slow_falling == "no" :
            print("hope your water bucket skills are good 😬")
        else :
            print("invalid input. please try again")
    elif knocked_off_tower == "no" :
        print("great! carefully finish destroying all the crystals")
    else :
        print("invalid input. please try again")

    slow_falling = input("do you have slow falling potions? : ").lower()
    if slow_falling == "yes" :
        print("great! being launched into the sky will not be a problem")
    elif slow_falling == "no" :
        print("be careful because dragon knockback will be dangerous")
    else :
        print("invalid input. please try again")

    final_check = input("so, have you finished destroying all end crystals? : ").lower()
    if final_check == "yes" :
        print("all crystals have been destroyed...")
        print("the dragon can no longer heal...")
        print("stage 2 complete.")
        print("entering stage 3... \nSTAGE 3 : THE DRAGON FIGHT")
    elif final_check == "no" :
        print("bruh, hurry up already!")
    else :
        print("invalid input. please try again")

elif on_main_island == "no" :
    print("ok. depending on where you are, find your way on to the main island")
else :
    print("invalid input. please try again")


dragon_perched = input("is the dragon perched on the portal? : ").lower()
if dragon_perched == "yes" :
    print("attack the dragon with a sword with as many hits as possible before it flies off")
elif dragon_perched == "no" :
    print("use a bow to attack the dragon")
else :
    print("invalid input. please try again")


bro_launched = input("did the dragon launch you into the air? : ").lower()
if bro_launched == "yes" :
    consumed_slow_falling = input("have you consumed slow falling potion? : ").lower()
    if consumed_slow_falling == "yes" :
        print("you are safe. you will casually float down safely")
    elif consumed_slow_falling == "no" :
        has_water_buckets = input("do you have water buckets? : " ).lower()
        # later when you learn variables better reuse the earlier answer instead of asking again here
        if has_water_buckets == "yes" :
            print("drop it right at your feet just before you land to prevent fall damage")
        elif has_water_buckets == "no" :
            print("oh no. you will probably die or face heavy damage")
        else :
            print("invalid input. please try again")
    else :
        print("invalid input. please try again")
elif bro_launched == "no" :
    print("nice! try not to get launched, but if you do, consume slow falling or have a water bucket ready")
else :
    print("invalid input. please try again")


dragon_breath = input("are you standing in dragon breath? : ").lower()
if dragon_breath == "yes" :
    print("move away immediately. dragon breath deals heavy damage over time")
elif dragon_breath == "no" :
    print("good. keep avoiding the purple clouds")
else :
    print("invalid input. please try again")
print("TIP : if you want to brew lingering potions later, collect some dragon breath in a bottle. though do this very carefully as dragon breath deals heavy damage")


low_health = input("are you below half health? : ").lower()
if low_health == "yes" :
    print("ya should eat food, drink potion of healing or retreat for a while until you reach high to full health again")
elif low_health == "no" :
    print("great! continue reducing the dragons health instead of your own :)")
else :
    print("invalid input. please try again")


dragon_health = input("is the dragon low on health? : ").lower()
if dragon_health == "yes" :
    print("keep the pressure on! victory is close")
elif dragon_health == "no" :
    print("stay patient. keep avoiding damage and attack when you are safe")
else :
    print("invalid input. please try again")


dragon_dead = input("have you slayed the dragon already? : ").lower()
if dragon_dead == "yes" :
    print("amazing! collect all your xp and the dragon egg")
elif dragon_dead == "no" :
    print("that's okay. the dragon can be a bit tough to kill. try your best to slay it!")
else :
    print("invalid input. please try again")


# stage 4 = outer end exploration

gateway = input("did a gateway portal appear? : ").lower()
if gateway == "yes" :
    print("great! this tiny portal leads to the outer end islands")
    enter_gateway = input("how are you planning to reach the gateway to enter the portal? : ").lower()
    if enter_gateway == "ender pearl" :
        print("this is a very risky way. but if you are feeling brave, then try to aim as good as you can before throwing the pearl")
        reached_gateway_pearl = input("did you make it? : ").lower()
        if reached_gateway_pearl == "yes" :
            print("amazing! now enter the portal to reach the outer end islands")
        elif reached_gateway_pearl == "no" :
            fallen_void = input("you fell into the void, dincha? : ")
            if fallen_void == "yes" :
                print("oh well.")
            elif fallen_void == "no" :
                print("phew! aim better or use a safer method to reach the gateway")
            else :
                print("invalid input. please try again")
        else :
            print("invalid input. please try again")
    elif enter_gateway == "crawling" :
        print("this is the easiest methed. go right ahead")
    elif enter_gateway == "sprint-swim" :
        print("this is a great and reliable method. go ahead!")
    elif enter_gateway == "elytra" :
        print("since you have somehow already got you hands on elytra, go ahead! this a great way to enter the gateway")
    elif enter_gateway == "blocks" :
        print("great! use the 'shift' button to stay on blocks. it will be much safer then")
    else :
        print("invalid input. please try again")
elif gateway == "no" :
    print("uh...check near the edge of the island")
else :
    print("invalid input. please try again")


reached_gateway = input("did you reach the gateway portal? : ").lower()
if reached_gateway == "yes" :
    print("nice! enter the portal to reach the outer end islands")
elif reached_gateway == "no" :
    print("use blocks, ender pearls, or an elytra if you somehow already have one to reach there")
    run_out_pearls = input("did ya run out of ender pearls? : ").lower()
    if run_out_pearls == "yes" :
        print("use blocks to bridge your way to the portal")
    run_out_blocks = input("then did ya run outta blocks? : ")
    if run_out_blocks == "yes" :
        print("that's fine. use end stone")
else :
    print("invalid input. please try again")


outer_islands = input("did you reach the outer islands? : ").lower()
if outer_islands == "yes" :
    print("welcome to the outer end!")
elif outer_islands == "no" :
    fall_void = input("you fell into the void, dincha? : ").lower()
    if fall_void == "yes" :
        print("that's okay. try again without falling into the void next time 💀")
    else :
        print("invalid input. please try again")
else :
    print("invalid input. please try again")


# stage 5 = end cities and elytra

found_city = input("did you find an end city? : ").lower()
if found_city == "yes" :
    found_chorus_fruit = input("do you see weird purple stick thingies anywhere? : ").lower()
    if found_chorus_fruit == "yes" :
        print("great! this is an amazing type of food! it can...")
        print("teleport you 8 blocks in any direction (even through walls!)")
        print("eating the fruit immediately after starting to fall will safely teleport you to the ground, allowing you to survive big drops")
        print("it's edible. you can eat those if you run low on food")
        print("it is used to craft purpur blocks and end rods")
    elif found_chorus_fruit == "no" :
        print("try to find some. it has great importance later on")
    else :
        print("invalid input. please try again")

    eat_chorus_fruit = input("did you eat a chorus fruit? : ").lower()
    if eat_chorus_fruit == "yes" :
        teleported = input("did you teleport near the edge of the island, fell into the void, or are safe? : ").lower()
        if teleported == "edge of island" :
            print("don't panic. press the 'shift' button to crouch and carefully back away from the edge")
        elif teleported == "void" :
            print("oh well. that's unfortunate 💀")
        elif teleported == "safe" :
            print("phew! ensure you avoid eating this when you are close to the edge of the islands")
        else :
            print("invalid input. please try again")
    elif eat_chorus_fruit == "no" :
        print("ok. ensure you avoid eating this when you are close to the edge of the islands")
    else :
        print("invalid input. please try again")

    shulkers = input("are there shulkers nearby? : ").lower()
    if shulkers == "yes" :
        print("be careful. levitation and the void are a terrible combination")
        levitating = input("are you levitating? : ").lower()
        if levitating == "yes" :
            print("don't panic. wait until the effect wears off and prepare to land safely")
            location_levitation = input("where are you levitating? : ").lower()
            if location_levitation == "near void" :
                print("try to get to land using ender pearls, otherwise bub-bye")
            elif location_levitation == "over island" :
                print("prepare for fall damage, eat some food to regain hearts")
                fall_damage = input("did you take fall damage? : ").lower()
                if fall_damage == "yes" :
                    print("eat food and retreat for a while till you regain full hearts")
                elif fall_damage == "no" :
                    print("phew! you are luckily safe. continue whatever you were doing")
                else :
                    print("invalid input. please try again")
            elif location_levitation == "indoors" :
                print("try to land on a nearby ledge, or prepare for some fall damage")
                fall_damage = input("did you take fall damage? : ").lower()
                if fall_damage == "yes" :
                    print("eat food and retreat for a while till you regain full hearts")
                elif fall_damage == "no" :
                    print("phew! you are luckily safe. continue whatever you were doing")
                else :
                    print("invalid input. please try again")
            elif location_levitation == "safe" :
                print("ok! continue whatever you were doing")
            else :
                print("invalid input. please try again")
        elif levitating == "no" :
            print("phew! avoid shulkers if possible, but if you are smart, you can use this effect to your benefit (think!)")
        else :
            print("invalid input. please try again")
    elif shulkers == "no" :
        print("phew! avoid shulkers if possible, but if you are smart, you can use this effect to your benefit (think!)")
    else :
        print("invalid input. please try again")
elif found_city == "no" :
    print("that's okay. search for it a bit longer")
else :
    print("invalid input. please try again")


good_loot = input("did you find good loot? : ").lower()
if good_loot == "yes" :
    print("nice! collect all the useful loot you can find")
elif good_loot == "no" :
    print("that's fine. that happens sometimes. try again")
else :
    print("invalid input. please try again")


shulker_shells = input("did you collect the shulker shells? : ").lower()
if shulker_shells == "yes" :
    print("great! future you will appreciate those shulker boxes")
elif shulker_shells == "yes" :
    print("collect them if you can. shulker boxes are very useful later on")
else :
    print("invalid input. please try again")
 

end_ship = input("does the city have an end ship? : ").lower()
if end_ship == "yes" :
    ship_location = input("is the ship floating mid air or can you get in safely? : ").lower()
    if ship_location == "floating" :
        print("ender pearl you way in or bridge your way in")
    elif ship_location == "safe" :
        print("great! you can enter safely")
    else :
        print("invalid input. please try again")

    print("you are in luck! you will find some of minecraft's rarest items here")
    elytra = input("did you collect the elytra? : ").lower()
    if elytra == "yes" :
        print("congrats! you can now fly 😎")
    elif elytra == "no" :
        print("gurl, you travelled across dimensions and forgot the main prize")
    else :
        print("invalid input. please try again")

    dragon_head = input("did you collect the dragon head? : ").lower()
    if dragon_head == "yes" :
        print("yay! you can now keep this as a showpiece and show off to your homies")
    elif dragon_head == "no" :
        print("it's not mandatory to collect it, but it's great for showoff purposes")
    else :
        print("invalid input. please try again")

elif end_ship == "no" :
    print("hard luck! search some more, then try a new game server later")
else :
    print("invalid input. please try again")


print("INVENTORY CHECK : ")

inventory_full = input("is your inventory full? : ").lower()
if inventory_full == "yes" :
    print("discard useless items, or craft ender chests or shulker boxes")
elif inventory_full == "no" :
    print("great! if you wanna save some space, craft ender chests or shulker boxes or something")
else :
    print("invalid input. please try again")

print("------x------")


print("SUPPLIES CHECK : ")

food_low = input("is your food running low? : ").lower()
if food_low == "yes" :
    print("eat sparingly and try to find chorus fruit. those are edible, but you can teleport on consumption. be careful")
elif food_low == "no" :
    print("ok! but you can eat chorus fruit too, as well, but with some side effects")
else :
    print("invalid input. please try again")


armor_durability_low = input("is you armor durability low? : ").lower()
if armor_durability_low == "yes" :
    print("avoid mobs that can cause damage to you")
elif armor_durability_low == "no" :
    print("great! you can continue fighting mobs that are present in the end cities")
else :
    print("invalid input. please try again")


pickaxe_durability_low = input("is your pickaxe's durability low? : ").lower()
if pickaxe_durability_low == "yes" :
    print("use it till it breaks and craft or use another one. if you don;t have enough resources, avoid mining alot")
elif pickaxe_durability_low == "no" :
    print("great! you can continue mining for a decent amount of time")
else :
    print("invalid input. please try again")


shield_breaks = input("did your shield break? : ").lower()
if shield_breaks == "yes" :
    print("oh no! craft a new one, or avoid hostile mobs")
elif shield_breaks == "no" :
    print("nice! you can resume using your shield to protect yourself")
    shield_status = input("is you shield's durability low, mid or high? : ").lower()
    if shield_status == "low" :
        print("fix your shield, enchant it, or craft a new one (i doubt you have the tools required for doing any of these)")
    elif shield_status == "mid" :
        print("use your shield sparingly")
    elif shield_status == "high" :
        print("great! you can continue using your shield")
    else :
        print("invalid input. please try again")
else :
    print("invalid input. please try again")

print("------x------")


# stage 6 = returning home

ready_leave = input("are you ready to leave the end? : ").lower()
if ready_leave == "yes" :
    print("great! let's get outta here")
    walk_or_fly = input("will you walk or fly you way outta here? : ").lower()
    if walk_or_fly == "walk" :
        print("ok! though it it will take a bit longer")
        fell_void = input("did you fall into the void? : ").lower()
        if fell_void == "yes" :
            print("well... that's unfortunate 💀")
        elif fell_void == "no" :
            print("great! avoid this at all costs")
            finds_gateway = input("did ya find the gateway? : ").lower()
            if finds_gateway == "yes" :
                print("great! enter the portal to get back to the overworld soon")
            elif finds_gateway == "no" :
                print("go on, keep searching!")
            else :
                print("invalid input. please try again")
        else :
            print("invalid input. please try again")
    elif walk_or_fly == "fly" :
        fireworks = input("do you have fireworks? : ").lower()
        if fireworks == "yes" :
            num_fireworks = int(input("how many foreworks do you have? : "))
            if num_fireworks >= 7 :
                print("great! you will be able to reach your gateway in the fastest way possible")
            elif num_fireworks < 7 and num_fireworks >= 1 :
                print("you can travel at a decent speed anyways")
            else :
                print("invalid input. please try again")
        elif fireworks == "no" :
            print("that's okay. you are travelling at a decent speed anyways")
        else :
            print("invalid input. please try again")
    else :
        print("invalid input. please try again")
elif ready_leave == "no" :
    print("okay. finish whatever you are doing before leaving")
else :
    print("invalid input. please try again")


returned_overworld = input("did you return to the overworld after using the portal? : ").lower()
if returned_overworld == "yes" :
    print("great! return back to your base and admire your new items!")
elif returned_overworld == "no" :
    void = input("ya fell into the void right? : ").lower()
    if void == "yes" :
        print("hard luck homie! try again later")
    else :
        print("invalid input. please try again")
else :
    print("invalid input. please try again")

if returned_overworld == "yes" :
    print("FANTASTIC! YOU SURVIVED THE END!")


# FIXES
# after invalid input, the input isn't asked again -> loops will fix this : LEARN IT
# make it more detailed later
# what if user enters text instead of a number in obsidian, arrows, food amounts, blocks, potions, water buckets and cauldrons? -> ValueError
# stop user from entering negative numbers
# even if the user doesn't meet the previous categories, the next question is asked anyways
# clean code + fix repetition
# better handling of invalid inputs
# apparently i need to learn error handling like 'try:' and 'accept:' or something like that. this will fix comment 3 (under 'fixes')

# and omg this is my first project ive made that's this long! it took 5 days to make this! im so feeling like a genius rn 😎

# oh and imma learn functions and dictionaries next so i can stop relying of conditionals and too many variables so much
# also i think it'll  help if i learn lists and loops too