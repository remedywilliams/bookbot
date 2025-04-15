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

def sort_on(dict):
    return dict["num"]

def sorter(chardict):
    sortlistdict = []
    for char in chardict:
        if char.isalpha():
            sortlistdict.append({"char": char, "num": chardict[char]})
    sortlistdict.sort(reverse=True, key=sort_on)
    for item in sortlistdict:
        print(f"{item['char']}: {item['num']}")

"""
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
"""

'''
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
'''
