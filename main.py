import sys
from stats import word_count, char_count, sorter

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count(filepath)
    print("--------- Character Count -------")
    sorter(char_count(filepath))
    print("============= END ===============")

main()