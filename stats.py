def word_count(filepath):
    wordcount = 0
    with open(filepath) as book:
        splitbook = book.read().split()
        for word in splitbook:
            wordcount += 1
    print(f"Found {wordcount} total words")

def char_count(filepath):
    chardict = {}
    with open(filepath) as book:
        for char in book.read():
            if char.lower() in chardict:
                chardict[char.lower()] += 1
            else:
                chardict[char.lower()] = 1
    return chardict
    # print(chardict)

def sorter(chardict):
    sortlistdict = []
    for char in chardict:
        if char.isalpha():
            count = chardict[char]
            sortlistdict.append("{char}" "{count}")
        else:
            pass
        print(f"{char}, {count}")
    sortlistdict.sort(reverse=True, key=count)
    print(sortlistdict)