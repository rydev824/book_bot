from stats import get_number_of_words, get_character_counts, chars_dict_to_sorted_list
import sys


def get_book_text(path) -> str:
    with open(path, encoding="utf-8") as f:
       return f.read()


def print_report(path_to_book, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted_list:
        if entry[0].isalpha():
            print(f"{entry[0]}: {entry[1]}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    number_of_words = get_number_of_words(book_text)
    sorted_list_of_characters = chars_dict_to_sorted_list(get_character_counts(book_text))

    print_report(book_path, number_of_words, sorted_list_of_characters)

main()