import random
import sys
def main():
    characters = {  #A list of all of the characters that are listen on the hsr wiki/fandom. Will needed to be manually updated.
    "Acheron": {"path": "Nihility", "combat_type": "Lightning"},
    "Argenti": {"path": "Erudition", "combat_type": "Physical"},
    "Arlan": {"path": "Destruction", "combat_type": "Lightning"},
    "Asta": {"path": "Harmony", "combat_type": "Fire"},
    "Aventurine": {"path": "Preservation", "combat_type": "Imaginary"},
    "Bailu": {"path": "Abundance", "combat_type": "Lightning"},
    "Black Swan": {"path": "Nihility", "combat_type": "Wind"},
    "Blade": {"path": "Destruction", "combat_type": "Wind"},
    "Boothill": {"path": "Hunt", "combat_type": "Physical"},
    "Bronya": {"path": "Harmony", "combat_type": "Wind"},
    "Clara": {"path": "Destruction", "combat_type": "Physical"},
    "Dan Heng": {"path": "Hunt", "combat_type": "Wind"},
    "Dan Heng IL": {"path": "Destruction", "combat_type": "Imaginary"},
    "Dr. Ratio": {"path": "Hunt", "combat_type": "Imaginary"},
    "Feixiao": {"path": "Hunt", "combat_type": "Wind"},
    "Firefly": {"path": "Destruction", "combat_type": "Fire"},
    "Fu Xuan": {"path": "Preservation", "combat_type": "Quantum"},
    "Gallagher": {"path": "Abundance", "combat_type": "Fire"},
    "Gepard": {"path": "Preservation", "combat_type": "Ice"},
    "Guinaifen": {"path": "Nihility", "combat_type": "Fire"},
    "Hanya": {"path": "Harmony", "combat_type": "Physical"},
    "Herta": {"path": "Erudition", "combat_type": "Ice"},
    "Himeko": {"path": "Erudition", "combat_type": "Fire"},
    "Hook": {"path": "Destruction", "combat_type": "Fire"},
    "Huohuo": {"path": "Abundance", "combat_type": "Wind"},
    "Jade": {"path": "Erudition", "combat_type": "Quantum"},
    "Jiaoqiu": {"path": "Nihility", "combat_type": "Fire"},
    "Jing Yuan": {"path": "Erudition", "combat_type": "Lightning"},
    "Jingliu": {"path": "Destruction", "combat_type": "Ice"},
    "Kafka": {"path": "Nihility", "combat_type": "Lightning"},
    "Luka": {"path": "Nihility", "combat_type": "Physical"},
    "Luocha": {"path": "Abundance", "combat_type": "Imaginary"},
    "Lynx": {"path": "Abundance", "combat_type": "Quantum"},
    "March 7th": {"path": "Preservation", "combat_type": "Ice"},
    "March 8th": {"path": "Hunt", "combat_type": "Imaginary"},
    "Misha": {"path": "Destruction", "combat_type": "Ice"},
    "Moze": {"path": "Hunt", "combat_type": "Lightning"},
    "Natasha": {"path": "Abundance", "combat_type": "Physical"},
    "Pela": {"path": "Nihility", "combat_type": "Ice"},
    "Qingque": {"path": "Erudition", "combat_type": "Quantum"},
    "Robin": {"path": "Harmony", "combat_type": "Physical"},
    "Ruan Mei": {"path": "Harmony", "combat_type": "Ice"},
    "Sampo": {"path": "Nihility", "combat_type": "Wind"},
    "Seele": {"path": "Hunt", "combat_type": "Quantum"},
    "Serval": {"path": "Erudition", "combat_type": "Lightning"},
    "Silver Wolf": {"path": "Nihility", "combat_type": "Quantum"},
    "Sparkle": {"path": "Harmony", "combat_type": "Quantum"},
    "Sushang": {"path": "Hunt", "combat_type": "Physical"},
    "Tingyun": {"path": "Harmony", "combat_type": "Lightning"},
    "Topaz & Numby": {"path": "Hunt", "combat_type": "Fire"},
    "DTrailblazer": {"path": "Destruction", "combat_type": "Physical"},
    "PTrailblazer": {"path": "Preservation", "combat_type": "Fire"},
    "HTrailblazer": {"path": "Harmony", "combat_type": "Imaginary"},
    "Welt": {"path": "Nihility", "combat_type": "Imaginary"},
    "Xueyi": {"path": "Destruction", "combat_type": "Quantum"},
    "Yanqing": {"path": "Hunt", "combat_type": "Ice"},
    "Yukong": {"path": "Harmony", "combat_type": "Imaginary"},
    "Yunli": {"path": "Destruction", "combat_type": "Physical"},
    "Lingsha": {"path": "Abundance", "combat_type": "Fire"},
    "Rappa": {"path": "Erudition", "combat_type": "Imaginary"}
}

    character_names = list(characters.keys())
    selected_character = random.choice(character_names)
    selected_character_details = characters[selected_character] #This is where the code grabs a random characters from the list, and randomizes it, AND to grabs their corrisponding hints.

    #print(f"Heres the character: {selected_character}") THIS WILL TELL U THE CHARACTER (used for testing)
    #print(f"Details: {selected_character_details}") THIS WILL TELL U THE HINTS (used for testing)
    #print("")
    print("\nHi, Welcome to Kiwito's HSR guessing game, this script includes all of the characters plus Rappa and Lingsha. To play this game you are basically required to know every characters PATH and ELEMENT because those are the only hints you get.")
    #print("")
    print("\nThere are some special commands I put:\n Use 'List' in the guess to show a list of all of the characters names.\n March The Hunt is called 'March 8th' (see 'List' command to double check) Dan Heng Imbibitor Lunae is called 'Dan Heng IL' and trailblazer is element+Name, for example Destruction Trailblazer is 'DTrailblazer', Harmony is 'HTrailblazer' and so on. \n Use 'List' command to find the correct way of spelling a character (Like damn QQ)")
    #print("")
    print("\nHint: Use a notepad or note down every character you used along with the path and element, it would be easier to keep track when your at 5+ guesses.")
    print("\nYou can reach me out in discord, Kiwito7103 for any questions permissions or ideas to make this better. GL gamer.")
    guess_counter = 0

    while True:
        user_guesses = input("\nGuess here: ")
        if user_guesses == "List":
            print(f"Heres a list of all of the characters: {character_names}\n") # Simply prints all of the characters when the input is 'List'.
        if user_guesses in character_names: 
            if user_guesses == selected_character and guess_counter < 1:
                    print(f"Wow first try is crazy. GG")
                    restart = input("\nWould you like to restart? [y/n]: \n").strip().lower()
                    if restart == 'y':
                     main()
                    else:
                        sys.exit() #Theres two of these restarts, this one is just when you guess the character first try.
                    
                        
            elif user_guesses == selected_character and guess_counter >= 1:
                guess_counter +=1
                print(f"You GOT IT with {guess_counter} attempts.")
                restart = input("\nWould you like to restart? [y/n]: \n").strip().lower()
                if restart == 'y':
                    main()
                else:
                    sys.exit() #Heres a the second one if ur did not guess it first try, both do the same thing of asking you if u want to resert or no.
             
            else:
                guessed_character_details = characters[user_guesses] #This will match the characters you wrote with the ones in the list and will grab their corrisponding hints.
                path_correct = guessed_character_details['path'] == selected_character_details['path'] # Made a new variable here to check if path (like their type) if its correct with the randomized character.
                element_correct = guessed_character_details['combat_type'] == selected_character_details['combat_type'] #same thing as last one but with their element.
           
                if path_correct == True and element_correct == False:
                    guess_counter += 1
                    path_correct = selected_character_details["path"]
                    guessed_element = guessed_character_details["combat_type"]
                    print(f"Path is {path_correct}, but not its not {guessed_element}.") #This one took me a while, but this only runs when you have guessed the same path as the randomized character, but not their element.
           
                elif element_correct == True and path_correct == False:
                        guess_counter += 1
                        element_correct = selected_character_details["combat_type"]
                        guessed_path = guessed_character_details["path"]
                        print(f"path is not {guessed_path}, but the element is {element_correct}.") #This one is the same as the last 'if string' but only with correct element.
           
                elif not path_correct and not element_correct:
                    guess_counter += 1
                    print(f"Path is wrong, and the element is wrong")
                elif path_correct and element_correct == True:
                    guess_counter += 1
                    print("You are very close, the path is right and the element is but its not the character") #This one is made exclusively for those characters who have the same element and path as the randomized character but not the that character (kinda like when theres 2 pokemon who are both flying and fire, its the right type but not the right characters, makes senes?) 
        elif user_guesses != "List": #If you misspell a character name it says responds with invalid, or in this case its who?.
            print(f"who?")
if __name__ == "__main__":
     main()
