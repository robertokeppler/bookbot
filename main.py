import string

with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_letters(file_contents):
    words = file_contents.lower()
    count_of_letters = {}
    for char in words:
        if char in string.ascii_lowercase:
            if char not in count_of_letters and char in string.ascii_lowercase:
                count_of_letters[char] = 1
            else:
                count_of_letters[char] += 1
    count_of_letters = list(count_of_letters.items())
    count_of_letters.sort(key= lambda x: x[1], reverse=True)
    return count_of_letters


print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{count_words(file_contents)} words found in the document")

for letter in count_letters(file_contents):
    print(f"The '{letter[0]}' character was found {letter[1]} times")

print("--- End report ---")