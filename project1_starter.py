""""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Ramiyah Davidson]
Date: [10/30/25]

AI Usage: I did use Ai for assistance with syntax, and with walking me through the assignment.
"""

import os  # this lets us do stuff with files and folders

def create_character(name, character_class):
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric" ]  # list of classes the game allows

    # this checks if the user typed a valid class, if not it tells them to pick again
    if character_class not in valid_classes:
        print("Invalid class, Choose from valid classes")
        return None  # stop making character if class is wrong

    level = 1  # all new characters start at level 1
    gold = 100 + (level * 10)  # start gold formula

    strength, magic, health = calculate_stats(character_class, level)  # get the character stats based on class and level

    # make a dictionary with all the character info
    return  {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength ,
        "magic": magic,
        "health": health,
        "gold": gold
    }

def calculate_stats(character_class, level):
    # each class has different formulas for stats
    if character_class == "Warrior":
        strength = 10 * level * 3
        magic = 10 * level
        health = 15 * level * 2
    elif character_class == "Mage":
        strength = 7 * level * 3
        magic = 5 * level
        health = 5 * level * 1
    elif character_class == "Rogue":
        strength = 5 * level * 3
        magic = 4 * level
        health = 9 * level * 3
    elif character_class == "Cleric":
        strength = 9 * level * 1
        magic = 5 * level
        health = 5 * level * 2
    else:
        strength = magic = health = 0  # if class doesn't exist, stats are zero

    return strength, magic, health  # return all the stats to use later

def save_character(character, filename):
    directory = os.path.dirname(filename)  # this gets the folder part of the path (so we can check if it exists)

    if directory and not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")  # tells user if the folder isn't real
        return False  # stop function if folder doesn't exist

    # open the file in write mode ("w") and use encoding="utf-8" so special characters work (AI told me to use this)
    with open(filename, "w", encoding= "utf-8") as file:
        file.write(f"Character Name: {character['name']}\n")  # write character name to file
        file.write(f"Class:  {character['class']} \n")  # write class
        file.write(f"Level: {character['level']} \n")  # write level
        file.write(f"Strength: {character['strength']} \n")  # write strength
        file.write(f"Magic: {character['magic']}\n")  # write magic
        file.write(f"Health: {character['health']}\n")  # write health
        file.write(f"Gold:  {character['gold']}\n")  # write gold
        return True  # if we got here, save worked

    file.close()  # close file (not really needed with 'with' but doesn't hurt)
    return True  # extra return just in case

def load_character(filename):
    if not os.path.exists(filename):
        print(f"Error: '{filename}' not found.")  # tell user if file doesn't exist
        return None  # stop function so it doesn't crash

    # open file to read, encoding utf-8 so special characters load correctly
    with open(filename, "r",  encoding= "utf-8") as file:
        lines = file.readlines()  # get all lines from file
        character = {}  # make empty dictionary to store character info
        for line in lines:  # go through each line
            if ':' in line:  # make sure line has a colon so we can split it
                key, value = line.strip().split(':')  # split into key and value at colon
                value = value.strip()  # remove spaces from value

                # put value into dictionary depending on key
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)  # convert number strings to int
                elif key == "Strength":
                    character["strength"] = int(value)
                elif key == "Magic":
                    character["magic"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)

        return character  # give back the character dictionary

    file.close()  # close file (not needed with 'with')
    # the bottom return with 'data' is not used so it won't run

def display_character(character):
    print("=== CHARACTER SHEET ===")  # header
    print(f"Name: {character['name']}")  # print name
    print(f"Class: {character['class']}")  # print class
    print(f"Level: {character['level']}")  # print level
    print(f"Strength: {character['strength']}")  # print strength
    print(f"Magic: {character['magic']}")  # print magic
    print(f"Health: {character['health']}")  # print health
    print(f"Gold: {character['gold']}")  # print gold

def level_up(character):
    character["level"] += 1  # increase level by 1

    # recalc stats based on new level
    strength, magic, health = calculate_stats(
        character["class"],
        character["level"]
    )

    # update stats in the dictionary
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # tell the user character leveled up
    print(f"Character {character['name']} has leveled up to level {character['level']}")
