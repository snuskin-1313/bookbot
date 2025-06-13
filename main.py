from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    f = get_text(book_path)
    words = count_words(f)
    chars = count_chars(f)
    after_sort = sort_chars(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for d in after_sort:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["count"]}")
    print("============= END ===============")
main()