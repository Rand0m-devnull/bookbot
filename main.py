import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def count_characters(text):
    count = 0
    result = {}
    uniques = set(text.lower())
    for char in text.lower():
        if char not in result:
            count = 1
            result[char] = count
        else:
            result[char] += count
    return result

def build_rapport(num_words, num_chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    alphabet = string.ascii_lowercase
    for key, value in num_chars.items():
        if key in alphabet:
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

if __name__ == '__main__':
    file = main()
    words = count_words(file)
    characters = count_characters(file)
    build_rapport(words, characters)
