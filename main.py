from stats import get_num_words
from stats import get_char_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    my_dict = get_char_count(text)
    print(my_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
