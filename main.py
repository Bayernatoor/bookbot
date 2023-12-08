book_path = "books/frankenstein.txt"

with open(book_path) as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    count = 0
    for w in words:
        count += 1
    return count

def count_letters(text):
    letter_count = {}
    for l in text:
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1
    return letter_count
            
def report(book):
    word_count = count_words(book)
    letter_count = count_letters(book)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for x in letter_count:
        if x.isalpha():
            print(f"the '{x}' character was found {letter_count[x]} times")

    print()
    print("--- End Report ---")


report(file_contents.lower())
