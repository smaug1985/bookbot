from stats import count_words
from stats import get_number_chars
from stats import sort_characters_dict
import sys

def get_book_text(path):
    content = ""
    
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    n_words = count_words(book_content)
    d_chars = get_number_chars(book_content)
    d_chars = sort_characters_dict(d_chars)
    print("============ BOOKBOT ============")
    print(f"Analying book found at {sys.argv[1]}...")
    print("--------- Word Count -------")
    print(f"Found {n_words} total words")
    print("--------- Character Count -------")
    for d in d_chars:
        if not d['char'].isalpha():
            continue
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

main()
