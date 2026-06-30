# 9 June, 2026

num_obsidian = 0
flint_and_steel = "nah"
has_obsidian = input("do you have obsidian blocks? : ").lower()
if has_obsidian == "yeah" :
    num_obsidian = int(input("how many blocks of obsidian do you have? : "))
    if num_obsidian < 10 :
        print("WARNING : you need more obsidian to build a functional portal")
    elif num_obsidian == 10:
        flint_and_steel = input("do you have a flint and steel? : ").lower()
        if flint_and_steel == "yeah" :
            print("great! you can build a standard, functional portal")
        elif flint_and_steel == "nah" :
            print("WARNING : you need a flint and steel to activate your portal to enter the nether")
        else :
            print("invalid input. please try again") 
    elif num_obsidian > 10 and num_obsidian < 14 :
        print("you can build a functional portal and have extra obsidian blocks. save those resources or fill in the corner gaps")
        flint_and_steel = input("do you have a flint and steel? : ").lower()
        if flint_and_steel == "yeah" :
            print("great! you can build a standard, functional portal")
        elif flint_and_steel == "nah" :
            print("WARNING : you need a flint and steel to activate your portal to enter the nether")
        else :
            print("invalid input. please try again") 
    elif num_obsidian == 14 : 
        flint_and_steel = input("do you have a flint and steel? : ").lower()
        if flint_and_steel == "yeah" :
            print("you can activate your classic, rectangular portal and enter the nether")
        elif flint_and_steel == "nah" :
            print("WARNING : you need a flint and steel to activate your portal to enter the nether")
        else :
            print("invalid input. please try again")
    elif num_obsidian > 14 :
        print("you may be able to build more than one functional nether portal")
        flint_and_steel = input("do you have a flint and steel? : ").lower()
        if flint_and_steel == "yeah" :
            print("great! you can build a standard, functional portal")
        elif flint_and_steel == "nah" :
            print("WARNING : you need a flint and steel to activate your portal to enter the nether")
        else :
            print("invalid input. please try again") 
    else :
        print("you have lots of obsidian. you can build one or more portals")
elif has_obsidian == "nah" :
    print("WARNING : you need obsidian blocks (you need 10 or 14 obsidian blocks to build 1 functional nether portal)")
else :
    print("invalid input. please try again")

print("TIP: consider placing fences or gates around your portal to prevent mobs from interchanging their worlds")


has_sword = input("do you have a sword? : ").lower()
if has_sword == "yeah" : 
    sword_material = input("is your sword made up of gold, wood, stone, iron, diamond or netherite? : ").lower()
    if sword_material == "gold" :
        print("this is not a great choice of material for fighting. however, this is extremely useful for enchantments")
        durability_of_gold_sword = input("is your sword's durability low, mid or high? : ").lower()
        if durability_of_gold_sword == "low" :
            print("you will need 2-4 more swords of this material for fighting (without enchantments)")
        elif durability_of_gold_sword == "mid" :
            print("you will be able to fight 2-4 mobs. keep spare swords")
        elif durability_of_gold_sword == "high" :
            print("you can fight around 8 mobs. but with an unenchanted gold sword, consider carrying spare swords")
        else :
            print("invalid input. please try again")
    elif sword_material == "wood" :
        print("you may need one or two extra swords in the nether")
        durability_of_wooden_sword = input("is your sword's durability low, mid or high? : ").lower()
        if durability_of_wooden_sword == "low" :
            print("you will need two or three more durable swords to survive")
        elif durability_of_wooden_sword == "mid" :
            print("you will be able to fight around 3-5 mobs. consider carrying more swords too")
        elif durability_of_wooden_sword == "high" :
            print("you can fight around 10 mobs. but with a wooden sword, consider carrying spare swords")
        else :
            print("invalid input. please try again")
    elif sword_material == "stone" :
        print("you have a small upgrade in sword material. though consider carrying another sword too")
        durability_of_stone_sword = input("is your sword's durability low, mid or high? : ").lower()
        if durability_of_stone_sword == "low" :
            print("you will need one or two more durable swords to survive")
        elif durability_of_stone_sword == "mid" :
            print("you will be able to fight around 5-8 mobs. consider carrying another sword as well")
        elif durability_of_stone_sword == "high" :
            print("you can fight around 15-20 mobs. if you are going on a long adventure, carry another sword")
        else :
            print("invalid input. please try again")
    elif sword_material == "iron" :
        print("you have a great upgrade in sword material!")
        durability_of_iron_sword = input("is your sword's durability low, mid or high? : ").lower()
        if durability_of_iron_sword == "low" :
            print("you will need one more durable sword to survive")
        elif durability_of_iron_sword == "mid" :
            print("you will be able to fight a good number of mobs. if you wish, keep another sword of your choice of material")
        elif durability_of_iron_sword == "high" :
            print("love the upgrade! you can fight a fine number of mobs")
        else :
            print("invalid input. please try again")
    elif sword_material == "diamond" :
        print("you have a great sword material!")
        durability_of_diamond_sword = input("is your sword's durability low, mid or high? : ").lower()
        if durability_of_diamond_sword == "low" :
            print("if you are going on a long expedition, you may need one more durable sword to survive")
        elif durability_of_diamond_sword == "mid" :
            print("you will be able to fight a great number of mobs. if you wish, keep another sword of your choice of material")
        elif durability_of_diamond_sword == "high" :
            print("love the upgrade! you can fight lots of mobs")
        else :
            print("invalid input. please try again")
    elif sword_material == "netherite" :
        print("you have amazing sword material!")
        durability_of_netherite_sword = input("is your sword's durability low, mid or high? : ").lower()
        if durability_of_netherite_sword == "low" :
            print("if you are going on a long expedition, you may need one more durable sword to survive")
        elif durability_of_netherite_sword == "mid" :
            print("you will be able to fight LOTS mobs. if you wish, keep another sword of your choice of material")
        elif durability_of_netherite_sword == "high" :
            print("you can fight countless mobs. don't worry about it breaking during combat")
        else :
            print("invalid input. please try again")
    else :
        print("invalid input. please try again")
elif has_sword == "nah" :
    print("WARNING : you need swords to survive hand-to-hand combat in the nether")
else :
    print("invalid input. please try again")


has_shield = input("do you have a sheild? : ").lower()
if has_shield == "yeah" :
    print("great! you will be able to block melee strikes, fireballs, arrows and explosions")
    durability_of_shield = input("how durable if your shield- low, mid or high? : ").lower()
    if durability_of_shield == "low" :
        print("repair or enchant your shield. it is crucial to protect yourself from damage in the nether")
    elif durability_of_shield == "mid" :
        print("consider repairing your shield or enchanting it")
    elif durability_of_shield == "high" :
        print("nice! if you wish, you can enchant it too for better results, if not done already!")
    else :
        print("invalid input. please try again")
elif has_shield == "nah" :
    print("WARNING : you will a shield for increased survival chances in the nether")
else :
    print("invalid input. please try again")


num_arrows = 0
has_bow = input("do you have a bow? : ").lower()
if has_bow == "yeah" :
    print("great! you can now deal ranged damage")
    arrows = input("do you have arrows? : ").lower()
    if arrows == "yeah" :
        num_arrows = int(input("how many arrows do you have? : "))
        if num_arrows <= 20 :
            print("you need more arrows")
        else :
            print("you have sufficient arrows")
    elif arrows == "nah" :
        print("you need arrows to actually use the bow (duh)")
    else :
        print("invalid input. please try again")
elif has_bow == "nah" :
    print("WARNING : you will need a bow and arrows to defend yourself against ghasts, blazes, and wither skeletons and defeat them")
else :
    print("invalid input. please try again")


food_ready = False
food = input("do you have food? : ").lower()
if food == "yeah" : 
    type_food = input("do you have steak, bread or golden apple? : ").lower()
    if type_food == "steak" :
        ask_steak = int(input("how many steaks do you have? : "))       # later add logic for if player has some of each type of food
        if ask_steak >= 4 :
            food_ready = True
            print("you have anough food for a long expedition")
        else :
            print("you need more food")
    elif type_food == "bread" :
        ask_bread = int(input("how much bread do you have? : "))
        if ask_bread >= 5 :
            food_ready = True
            print("you have enough food for a long expedition")
        else :
            print("you need more food")
    elif type_food == "golden apple" :
        ask_golden_apple = int(input("how many golden apples do you have? : "))
        if ask_golden_apple >= 4 :
            food_ready = True
            print("great! you will gain extra hearts to continue combat")
        else :
            print("you need more food")
    else :
        print("invalid input. please try again")
elif food == "nah" :
    print("WARNING : you need food to survive when you are far away from home")
else :
    print("invalid input. please try again")


num_of_blocks = 0
has_blocks = input("do you have blocks? : ").lower()
if has_blocks == "yeah" :
    num_of_blocks = int(input("how many blocks do you have? : "))
    if num_of_blocks <= 5 :
        print("you need more blocks, otherwise, you can just collect netherrack \nWARNING : you may need emergency blocks immediately")
    else :
        print("you have enough blocks for bridging, pillaring, and blocking tunnels. if you fall short, just collect some netherrack")
elif has_blocks == "nah" :
    print("WARNING : you will need blocks for bridging, blocking tunnels and pillaring. collect blocks from the overworld or collect netherrack \nWARNING : you may need emergency blocks immediately")
else :
    print("invalid input. please try again")


pickaxe = input("do you have a pickaxe? : ").lower()
if pickaxe == "yeah" :
    pickaxe_material = input("what is you pickaxe made up of? : ").lower()
    if pickaxe_material == "wood" :
        print("you can mine netherrack, nether gold ore, nether quartz ore and glowstone, but very slowly. your pickaxe will break fast")
    elif pickaxe_material == "stone" :
        print("you can mine netherrack, magma blocks, soul sand, basalt, blackstone and nether gold ore effectively")
    elif pickaxe_material == "gold" :
        print("you can mine nether gold ore, nether quartz ore, netherrack, basalt, blackstone and magma blocks")
    elif pickaxe_material == "iron" :
        print("you can mine nether quartz ore, nether gold ore, glowstone, magma blocks, basalt, natherrack, blackstone and soul sand")
    elif pickaxe_material == "diamond" :
        print("you can mine ancient debris and all other low tier blocks")
    elif pickaxe_material == "netherite" :
        print("you can mine every single mineable block in the nether")
    else :
        print("invalid input. please try again")
elif pickaxe == "nah" :
    print("WARNING : you need a pickaxe to mine useful blocks")
else :
    print("invalid input. please try again")
# here, wooden pickaxe counts the same as netherite pickaxe. thats just stupid. fix later with better skill


num_potions = 0
fire_resistance_potions = input("do you have fire resistance potions? : ").lower()
if fire_resistance_potions == "yeah" :
    num_potions = int(input("how many potions do you have? : "))
    if num_potions >= 4 :
        print("you will be able to swim across small pools of lava, and survive accidents while combat and travel")
    elif num_potions <= 3 :
        print("you will need more fire resistant potions. you can find nether wart, magma cream and blaze powder in the nether to brew this")
    else :
        print("invalid input. please try again")
elif fire_resistance_potions == "nah" :
    print("WARNING : you need fire resistance potions to prevent accidents")
else :
    print("invalid input. please try again")


water_ready = False
water_buckets = input("do you have water buckets? : ").lower()
if water_buckets == "yeah" :
    num_water_buckets = int(input("how many water buckets do you have? : "))
    if num_water_buckets >= 2 :
        has_cauldron = input("do you have cauldrons? : ").lower()
        if has_cauldron == "yeah" :
            num_cauldrons = int(input("how many cauldrons do you have? : "))
            if num_cauldrons == num_water_buckets :
                water_ready = True
                print("you will be a able to avoid accidents and prevent fall damage")
            elif num_cauldrons > num_water_buckets :
                print("you will need more water buckets to fill cauldrons to use water in the nether")
            elif num_water_buckets > num_cauldrons :
                print("you will need more cauldrons that you can fill to use water in the nether")
            else :
                print("invalid input. please try again")
        elif has_cauldron == "nah" :
            print("you need cauldrons to use water in the nether for various reasons")
        else :
            print("invalid input. please try again")
    elif num_water_buckets <=1 and num_water_buckets >= 0 :
        print("you need more water buckets and cauldrons to use water efficiently in the nether")
    else :
            print("invalid input. please try again")
elif water_buckets == "nah" :
    print("you need water buckets or cauldrons filled with water to use water in the nether")
else :
    print("invalid input. please try again")


gold_armor = input("do you have gold armor? : ").lower()
if gold_armor == "yeah" :
    amt_of_armor = input("do you have gold boots, chestplate, leggings or helmet? : ").lower()    # later add if player has one or more pieces of armor
    if amt_of_armor == "boots" :
        print("great! the piglins will not attack you on sight")
    elif amt_of_armor == "chestplate" :
        print("great! the piglins will not attack you on sight")
    elif amt_of_armor == "leggings" :
        print("great! the piglins will not attack you on sight")
    elif amt_of_armor == "helmet" :
        print("great! the piglins will not attack you on sight")
    else :
        print("invalid input. please try again")
elif gold_armor == "nah" :
    print("WARNING : piglins will attack you on sight. consider carrying atleast one piece of gold armor")    
else :
    print("invalid input. please try again")
# one piece of armor is treated the same as the full set. dumb error. fix later with better skill


gold_ingots = input("do you have gold ingots to barter with piglins? : ").lower()
if gold_ingots == "yeah" :
    print("great! you can barter this with piglins to recieve amazing items in return")
elif gold_ingots == "nah" :
    print("if you want amazing loot in exchange for gold ingots, consider carrying some with you")
else :
    print("invalid input. please try again")


if num_obsidian >= 10 and flint_and_steel == "yeah" and has_sword == "yeah" and has_shield == "yeah" and has_bow == "yeah" and num_arrows > 20 and food_ready == True and num_of_blocks > 5 and pickaxe == "yeah" and num_potions >= 4 and water_ready == True and gold_armor == "yeah" and gold_ingots == "yeah":
    # later add all the logic for a proper check
    print("you are ready for a decent journey into the nether")
else :
    print("you may face some difficulties in the nether")


# line 316 -> have not filled all logic. later, with better skill, fill in all the logic
# fix later : if you get 'invalid input...', the question is not asked again
# what if user enters text instead of a number in obsidian, arrows, food amounts, blocks, potions, water buckets and cauldrons? -> ValueError


# VERSION 2 (of this project)
# better handling of invalid inputs
# try to score readiness instead of pass/fail
# check armor quality
# check enchantments of tools and weapons
# distinguishing wooden vs netherite gear in code and final readiness
# allow many food types
# stop user from entering negative numbers
# clean code + fix repetition


# FUTURE IDEAS
# later check enchantments for all tools and weapons
# create a nether guide on all mobs and drops
# create an end expedition checker ✔️ 13 June 2026
# make a directory on all mobs, drops, elytra and ender dragon head of the end
# create a code on readiness checker of how ready the player if to beat the ender dragon
# readiness checker on how ready the player is to beat the boss mob (wither)
# finding the deep dark
# readiness checker on how ready the player is to beat the warden
# finding amethyst caves + find, drops and their usefulness
# minecraft biome directory - mobs, drops, trees, unique finds
# guide to brewing potions
# locating a stronghold 
# village safety checker
# check if player has enough resources to start a starter base