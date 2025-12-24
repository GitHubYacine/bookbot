def get_book_as_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def words_in_book(full_book):
    return f"Found {len(full_book.split())} total words"

def count_each_char(text):
    result = {}
    for word in text.lower(): 
        for char in word:
            if char not in result:
                result[char] = 1 
            else:
                result[char] += 1
    return result

def sort_on(items):
    return items["num"]

def sort_dict(dict_of_chars):
    result = []
    
    for char, number in dict_of_chars.items():
        if char.isalpha():
            final_dict = {"char": char, "num": number}
            result.append(final_dict)
        else:
            continue
        
    result.sort(reverse=True, key=sort_on)
    return result