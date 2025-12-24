import sys
from stats import get_book_as_text, words_in_book, count_each_char, sort_dict

def main():
    if len(sys.argv) == 2:
        text = get_book_as_text(sys.argv[1])
        list_of_dict = sort_dict(count_each_char(text))
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(words_in_book(text))
        print("--------- Character Count -------")
        for dict in list_of_dict:
            print(f'{dict["char"]}: {dict["num"]}')
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()