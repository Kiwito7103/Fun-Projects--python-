import random
def main():
    characters = {
"ACHERON": {"path": "Nihility", "combat_type": "Lightning"},
"ARGENTI": {"path": "Erudition", "combat_type": "Physical"},
"ARLAN": {"path": "Destruction", "combat_type": "Lightning"},
"ASTA": {"path": "Harmony", "combat_type": "Fire"},
"AVENTURINE": {"path": "Preservation", "combat_type": "Imaginary"},
"BAILU": {"path": "Abundance", "combat_type": "Lightning"},
"BLACK SWAN": {"path": "Nihility", "combat_type": "Wind"},
"BLADE": {"path": "Destruction", "combat_type": "Wind"},
"BOOTHILL": {"path": "Hunt", "combat_type": "Physical"},
"BRONYA": {"path": "Harmony", "combat_type": "Wind"},
"CLARA": {"path": "Destruction", "combat_type": "Physical"},
"DAN HENG": {"path": "Hunt", "combat_type": "Wind"},
"DAN HENG IL": {"path": "Destruction", "combat_type": "Imaginary"},
"DR. RATIO": {"path": "Hunt", "combat_type": "Imaginary"},
"FEIXIAO": {"path": "Hunt", "combat_type": "Wind"},
"FIREFLY": {"path": "Destruction", "combat_type": "Fire"},
"FU XUAN": {"path": "Preservation", "combat_type": "Quantum"},
"GALLAGHER": {"path": "Abundance", "combat_type": "Fire"},
"GEPARD": {"path": "Preservation", "combat_type": "Ice"},
"GUINAFEN": {"path": "Nihility", "combat_type": "Fire"},
"HANYA": {"path": "Harmony", "combat_type": "Physical"},
"HERTA": {"path": "Erudition", "combat_type": "Ice"},
"HIMEKO": {"path": "Erudition", "combat_type": "Fire"},
"HOOK": {"path": "Destruction", "combat_type": "Fire"},
"HUOHUO": {"path": "Abundance", "combat_type": "Wind"},
"JADE": {"path": "Erudition", "combat_type": "Quantum"},
"JIAOQIU": {"path": "Nihility", "combat_type": "Fire"},
"JING YUAN": {"path": "Erudition", "combat_type": "Lightning"},
"JINGLIU": {"path": "Destruction", "combat_type": "Ice"},
"KAFKA": {"path": "Nihility", "combat_type": "Lightning"},
"LUKA": {"path": "Nihility", "combat_type": "Physical"},
"LUOCHA": {"path": "Abundance", "combat_type": "Imaginary"},
"LYNX": {"path": "Abundance", "combat_type": "Quantum"},
"MARCH 7TH": {"path": "Preservation", "combat_type": "Ice"},
"MARCH 8TH": {"path": "Hunt", "combat_type": "Imaginary"},
"MISHA": {"path": "Destruction", "combat_type": "Ice"},
"MOZE": {"path": "Hunt", "combat_type": "Lightning"},
"NATASHA": {"path": "Abundance", "combat_type": "Physical"},
"PELA": {"path": "Nihility", "combat_type": "Ice"},
"QINGQUE": {"path": "Erudition", "combat_type": "Quantum"},
"ROBIN": {"path": "Harmony", "combat_type": "Physical"},
"RUAN MEI": {"path": "Harmony", "combat_type": "Ice"},
"SAMPO": {"path": "Nihility", "combat_type": "Wind"},
"SEELE": {"path": "Hunt", "combat_type": "Quantum"},
"SERVAL": {"path": "Erudition", "combat_type": "Lightning"},
"SILVERWOLF": {"path": "Nihility", "combat_type": "Quantum"},
"SPARKLE": {"path": "Harmony", "combat_type": "Quantum"},
"SUSHANG": {"path": "Hunt", "combat_type": "Physical"},
"TINGYUN": {"path": "Harmony", "combat_type": "Lightning"},
"TOPAZ & NUMBY": {"path": "Hunt", "combat_type": "Fire"},
"DTRAILBLAZER": {"path": "Destruction", "combat_type": "Physical"},
"PTRAIlBLAZER": {"path": "Preservation", "combat_type": "Fire"},
"HTRAILBLAZER": {"path": "Harmony", "combat_type": "Imaginary"},
"WELT": {"path": "Nihility", "combat_type": "Imaginary"},
"XUEYI": {"path": "Destruction", "combat_type": "Quantum"},
"YANQING": {"path": "Hunt", "combat_type": "Ice"},
"YUKONG": {"path": "Harmony", "combat_type": "Imaginary"},
"YUNLI": {"path": "Destruction", "combat_type": "Physical"},
"LINGSHA": {"path": "Abundance", "combat_type": "Fire"},
"RAPPA": {"path": "Erudition", "combat_type": "Imaginary"},
"SUNDAY": {"path": "Harmony", "combat_type": "Imaginary"},
"FUGUE": {"path": "Nihility", "combat_type": "Fire"} 
}

    character_names = list(characters.keys())
    selected_character = random.choice(character_names)
    selected_character_details = characters[selected_character]

    #print(f"Heres the character: {selected_character}")
    #print(f"Details: {selected_character_details}")
    print("")
    print("Hi, Welcome to Kiwito's HSR guessing game, this script includes all of the characters plus Rappa and Lingsha. To play this game you are basically required to know every characters PATH and ELEMENT because those are the only hints you get.")
    print("")
    print("There are some special commands I put:\n Use 'List' in the guess to show a list of all of the characters names.\n March The Hunt is called 'March 8th' (see 'List' command to double check) Dan Heng Imbibitor Lunae is called 'Dan Heng IL' and trailblazer is element+Name, for example Destruction Trailblazer is 'DTrailblazer', Harmony is 'HTrailblazer' and so on. \n Use 'List' command to find the correct way of spelling a character (Like damn QQ)")
    print("")
    print("Hint: Use a notepad or note down every character you used along with the path and element, it would be easier to keep track when your at 5+ guesses.")
    guess_counter = 0

    while True:
        user_guesses = input("\nGuess here: ")
        user_guesses = user_guesses.upper()

        if user_guesses == "LIST":
            character_names = [name.lower() for name in characters.keys()]
            print(f"Heres a list of all of the characters: {character_names}\n")
        if user_guesses in character_names: 
            if user_guesses == selected_character and guess_counter < 1:
                    print(f"Wow first try is crazy. GG")
                    restart = str(input("\nWould you like to restart? [y/n]: \n"))
                    if restart == 'y' or 'Y':
                        main()
                    elif restart == 'N' or 'n':
                         break
                    else:
                         print("Invalid output")
            elif user_guesses == selected_character and guess_counter >= 1:
                guess_counter +=1
                print(f"You GOT IT with {guess_counter} attempts.")
                restart = str(input("\nWould you like to restart? [y/n]: \n"))
                if restart == 'y' or 'Y':
                    main()
                elif restart == 'N' or 'n':
                     break
                else:
                     print("Invalid output")
            else:
                guessed_character_details = characters[user_guesses]
                path_correct = guessed_character_details['path'] == selected_character_details['path']
                element_correct = guessed_character_details['combat_type'] == selected_character_details['combat_type']
           
                if path_correct == True and element_correct == False:
                    guess_counter += 1
                    path_correct = selected_character_details["path"]
                    guessed_element = guessed_character_details["combat_type"]
                    print(f"Path is {path_correct}, but not its not {guessed_element}.")
           
                elif element_correct == True and path_correct == False:
                        guess_counter += 1
                        element_correct = selected_character_details["combat_type"]
                        guessed_path = guessed_character_details["path"]
                        print(f"path is not {guessed_path}, but the element is {element_correct}.")
           
                elif not path_correct and not element_correct:
                    guess_counter += 1
                    print(f"Path is wrong, and the element is wrong")
                elif path_correct and element_correct == True:
                    guess_counter += 1
                    print("You are very close, the path is right and the element is but its not the character")
        elif user_guesses != "LIST":
            print(f"who?")
if __name__ == "__main__":
     main()

#Incase you have a massive memory loss, You made a code to guess randomized hsr characters using 2 hints.
# What you have so far is it will give you a response if you guessed either path or element correct, but not both or not neither. Also if you get a character not from the game it will reset back to start.
#Current issue is that when both are incorrect you have nothing printed, as in when ur guess dosent match the path and element nothing will print instead of the last if statement
#Future problems is having it work when both are correct and display the amount of guesses it takes to guess, and having a guess that satisfies both path and element but its the wrong character (needs testing)
#Special characters/Rules: 5 star Dan Heng is called "Dan Heng IL", hunt march is called "March 8th" and theres a "List" command that will display all characters. For Trailblazer its Element+Trailblazer (ex Physical one is called DTrailblazer)
#Also run this in cmd because it likes to break the in-app one, (do cd (find the place of the code)then do python Lyub'sGuessHSR.py)