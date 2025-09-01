from stats import get_num_words
def get_book_text(inputPath):
    with open(inputPath) as f:
        return f.read()
def main(): 
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    print(f"{get_num_words(book_text)} words found in the document")
main()