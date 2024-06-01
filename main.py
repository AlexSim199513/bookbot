def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    num_letters_string = return_num_letters(num_letters)
    print("Book Report for Mary Shelley's Frankenstein")
    print(f"{num_words} words found in the document \n")
    print(num_letters_string)
    print("End of Report")


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

def return_num_letters(letters):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    strings = []
    for char in alphabet:
       if char in letters:
        strings.append(f"The '{char}' character was found {letters[char]} times")
    return "\n".join(strings)

main()