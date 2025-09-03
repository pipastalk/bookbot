import sys
from stats import get_num_words, character_count, sort_dictionary
def get_book_text(inputPath):
    with open(inputPath) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:    
        path = sys.argv[1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------" )
    book_text = get_book_text(path)
    book_char_count = character_count(book_text)
    #print(book_text)
    print(f"Found {get_num_words(book_text)} total words")
    print(f"{character_count(book_text)}")
    print("(--------- Character Count -------)")
    #print(f"{sort_dictionary(book_char_count)}")
    sorted_characters = sort_dictionary(book_char_count)
    for k,v in sorted_characters.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")
main()