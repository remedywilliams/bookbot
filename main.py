from stats import word_count, char_count, sorter

def main():
    filepath = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count(filepath)
    print("--------- Character Count -------")
    sorter(char_count(filepath))
    print("============= END ===============")

main()