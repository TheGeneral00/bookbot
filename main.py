def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_counter = word_count(text)
    letter_count = get_letter_count(text)
    report(book_path, word_counter, letter_count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def get_letter_count(string): 
    lowered_string = string.lower()
    counter = {}

    for i in lowered_string:
        if i.isalpha() and i not in counter: counter[i] = 1
        elif i in counter: counter[i] += 1      
        else: pass

    counter_list = []
    for i in counter: counter_list.append({"char": i, "num": counter[i]})
    counter_list.sort(reverse = True, key=sort_on)
    return counter_list 
     

def report(book_path, word_counter, letter_count):
    print(f"--- Begin report of {book_path}  ---")
    print(f"{word_counter} words found in the document")
    
    for i in letter_count: 
        print(f"the '{i['char']}' character was found {i['num']} times")
    
    print("--- End of the report ---")

main()
