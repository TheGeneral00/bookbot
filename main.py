def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(text)
    letter_count = get_letter_count(text)
    print(text)
    print (f"wordcount: {wc}")
    print (f"total letter: {letter_count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)

def get_letter_count(string):
    lowered_string = string.lower()
    counter = {}

    for i in lowered_string:
        if i not in counter: counter[i] = 1
        elif type(i) != str: pass
        else: counter[i] += 1

    return counter
            
main()
