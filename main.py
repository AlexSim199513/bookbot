def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lowered_text = text.lower()
    letters = []
    for letter in lowered_text:
        letters.append(letter)

    letter_count = {}

    for i in range (len(letters)):
        if letters[i] not in alphabet:
            pass
        elif letters[i] in letter_count:
            letter_count[letters[i]] += 1
        else:
            letter_count[letters[i]] = 1

    return letter_count



main()