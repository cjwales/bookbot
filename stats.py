def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_times_character_appears(text):
    characters = {}
    for character in text:
        character = character.lower()
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_on(item):
    return item["num"]

def sorted_list_of_dictionaries(characters):
    dictionaries = []
    for character in characters:
        num = characters[character]
        dictionaries.append({"char": character, "num": num})
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries