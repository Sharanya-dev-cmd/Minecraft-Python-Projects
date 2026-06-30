# Thursday, 4 June, 2026
missing_resources = ""

has_hoe = input("do you have a hoe? : ").lower()
if has_hoe == "yes" :
    print("you can successsfully till your farm")
elif has_hoe == "no" :
    missing_resources = missing_resources  + "\nhoe"
    print("you need a hoe")
else :
    print("invalid input")


has_dirt_blocks = int(input("how many dirt blocks do you have? : "))
if has_dirt_blocks >= 9 :
    print("you can build a 3x3 farm or bigger!")    # has a bug, need to fix later with better logic
elif has_dirt_blocks >= 1 and has_dirt_blocks <=8 :
    print("you can have a decent-sized farm")
else :
    missing_resources = missing_resources + "\ndirt blocks"
    print("you need dirt blocks")


has_seeds = int(input("how many seeds do you have? : "))
if has_seeds >= has_dirt_blocks :
    print("you have a decent number of seeds")
else :
    missing_resources = missing_resources + "\nseeds"
    print("you need more seeds")


has_water_bucket = int(input("how many water buckets do you have? : "))  # ill later add 'u can be near a water source too' in another version
if has_water_bucket >= 1 :   # i shall fix this game lag later
    print("you will be able to irrigate your farm")
else :
    missing_resources = missing_resources + "\nwater bucket"
    print("you need one or more water buckets")


has_light_source = input("do you have a light source? : ").lower()
if has_light_source == "yes" :
    print("you will be able to light up your farm")
elif has_light_source == "no" :
    missing_resources = missing_resources + "\nlight source"
    print("you need a light source to build your farm")
else :
    print("invalid input")


if has_hoe == "yes" and has_dirt_blocks >= 1 and has_seeds >= has_dirt_blocks and has_water_bucket >= 1 and has_light_source == "yes" :
    print("you can build a great farm!")
else :
    print("you need more resources to make your farm functional")

print("MISSING RESOURCES : ", missing_resources)

# IDEAS FOR FUTURE VERSIONS / NEW PROJECTS
# u can give a final summary of all missing resources instead of many sep. messages ✔️ Saturday, 6 June 2026
# add bone meal in later version
# add thingies for different crop types (wheat, carrots, potatoes, beetroot)
# check if player can build animal farm
# check if farm is safe from hostile mobs
# check if player has enough resources for starter base
# create a complete farm planner with building and growth advice