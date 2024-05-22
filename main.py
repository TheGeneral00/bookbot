def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(text)
    print(text)
    print (f"wordcount: {wc}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)

main()
