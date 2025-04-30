from stats import get_word_count, get_character_count, sorted_list
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    num_words = get_word_count(book_text)
    character_dict = get_character_count(book_text)
    char_list = sorted_list(character_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at " + book_location + "...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
