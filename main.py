def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_count_dict = counting_chars(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    processing_data(chars_count_dict, book_path)
    print("--- End report ---")
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def counting_chars(text):
    chars_dict = {}
    for char in text.lower():
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

def sort_on(dict):
    return dict["amount"]

def processing_data(dict, book):
    list_of_dicts = [{'letter': k, 'amount': v} for k, v in dict.items() if k.isalpha()]
    list_of_dicts.sort(reverse= True, key=sort_on)
    for dict in list_of_dicts:
        print(f'The "{dict["letter"]}" character was found {dict["amount"]} times in the book {book}')


main()