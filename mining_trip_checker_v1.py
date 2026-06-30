# this shall determine whether a player is ready for a mining trip

has_pickaxe = input("do you have a pickaxe? : ").lower()

if has_pickaxe == "yes" :          # later check pickaxe enchantments too
    print("great! you will be able to mine faster and more efficiently")
    pickaxe_durability = input("is your pickaxe's durability low, medium or high? : ").lower() # just trying this for logic practice
    if pickaxe_durability == "high" :
        print("your pickaxe can be used for a long mining session")
    elif pickaxe_durability == "medium" :
        print("you can mine for a decent amount of time")                         # try later to judge durability using scale of 1 to 10
    elif pickaxe_durability == "low" :
        print("you won't be able to mine for a long time. craft another pickaxe")
    else :
        print("invalid input. please try again")
elif has_pickaxe == "no" :
    print("you need a pickaxe to mine")
else :
    print("invalid input. please try again")      # maybe later u can check what material the pickaxe is made of n judge efficiency and speed

    
has_torches = int(input("how many torches do you have? : "))

if has_torches <= 15 and has_torches >= 0 : 
    print("you need more torches")
else :
    print("you have a good number of torches")


has_food = input("do you have food? : ").lower()    # later try to add that how much each food type can fill the player's hunger bar

if has_food == "yes" :
    amount_of_food = int(input("enter the number of food you have : "))
    if amount_of_food <= 3 and amount_of_food >= 0 : 
        print("you may not have enough food")       # will fix lag later(food = 0 can't print 'u may not have enough food')
    else :
        print("you have enough food")
elif has_food == "no" :
    print("you need food to fill your hunger bar and regenerate hearts when you take damage")
else :
    print("invalid input. please try again")


has_empty_inventory_slots = input("do you have empty inventory slots? : ").lower()

if has_empty_inventory_slots == "yes" :
    num_of_empty_inventory_slots = int(input("how many empty inventory slots do you have? : "))
    if num_of_empty_inventory_slots >= 0 and num_of_empty_inventory_slots <= 5 :
        print("you may not have enough empty slots in you inventory. free some space or carry a chest")
    elif num_of_empty_inventory_slots >= 6 :
        print("you have enough space in your inventory")
    else :
        print("invalid input. please try again")
elif has_empty_inventory_slots == "no" :
    print("you need empty slots to carry you mining finds and drops")
else :
    print("invalid input. please try again")


has_weapons = input("do you have any weapons? : ").lower()

if has_weapons == "yes" :
    type_of_weapons = input("what type of weapons do you have? : ").lower()     # maybe later check weapon enchantments
    if type_of_weapons == "sword" or type_of_weapons == "bow and arrows" :      # maybe later if user types 'bow and arrows' count the arrows as well in the code
        print("you will be able to fend off hostile mobs that sneak up on you when you are mining")
    else :
        print("you may need weapons to kill hostile mobs on your mining journey")
elif has_weapons == "no" :
    print("you may need weapons to kill hostile mobs on your mining journey")   
else :
    print("invalid input. please try again")


has_water_bucket = input("do you have a water bucket? : ").lower()

if has_water_bucket == "yes" :
    num_of_water_buckets = int(input("how many water buckets do you have? : "))
    if num_of_water_buckets >= 3 :
        print("you have enough water to extinguish lava and travel downwards safely and efficiently without taking fall damage")
    else :
        print("you may need some (more) water buckets for an efficient mining session")
elif has_water_bucket == "no" : 
    print("you may need some water buckets for an efficient mining session")
else :
    print("invalid input. please try again")


if has_pickaxe == "yes" and has_torches > 16 and has_food == "yes"  and amount_of_food >= 4 and has_empty_inventory_slots == "yes" and has_weapons == "yes" and has_water_bucket == "yes" :
    print("you are ready for your mining trip!")
else :
    print("you don't have enough resources and tools for a safe and successful mining trip")


# FUTURE IDEAS
# diamond hunting simulator
# mining in the Nether
# guide on what to do in the End
# tnt mining