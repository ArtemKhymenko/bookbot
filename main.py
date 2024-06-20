def main(path_to_file="books/frankenstein.txt"):
    file_contents = read_file()
    words = count_words(file_contents)
    characters = count_characters(file_contents)
    # list of tuples
    list_of_characters = list(characters.items())
    list_of_characters.sort(key=lambda x: x[1], reverse=True)
    print(f'--- Begin report of {path_to_file} ---\n{words} words found in the document\n')
    for pair in list_of_characters:
        print(f'The "{pair[0]}" character was found {pair[1]} times')
    print(f"--- End report ---")

def read_file(path_to_file="books/frankenstein.txt"):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_contents):
    list_of_words = file_contents.split()
    words = len(list_of_words)
    return words


def count_characters(file_contents):
    dict_of_characters = {}
    file_contents = file_contents.lower()
    for character in file_contents:
        if character.isalpha():
            if character in dict_of_characters:
                dict_of_characters[character] += 1
            else:
                dict_of_characters[character] = 1
    return dict_of_characters

if __name__ == "__main__":
    main()