import sys
from stats import number_of_words
from stats import number_of_times_character_appears
from stats import sorted_list_of_dictionaries

def get_book_text(file_path):
    with open(file_path) as f:
        return(f.read())
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = number_of_words(text)
    characters = number_of_times_character_appears(text)
    sorted_chars = sorted_list_of_dictionaries(characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

main()